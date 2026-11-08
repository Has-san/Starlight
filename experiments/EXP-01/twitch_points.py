#!/usr/bin/env python3
"""EXP-01 : essais sur les points de chaîne Twitch.

Script JETABLE, voir README.md (fiche de l'expérience) et MODE-EMPLOI.md.

ATTENTION : ce script n'a PAS été exécuté contre Twitch quand il a été écrit.
Seuls la syntaxe et la logique de lecture des messages ont été vérifiées hors
ligne. Les adresses de l'API (Helix, EventSub) sont celles que l'auteur
connaissait : à confirmer sur la documentation officielle de Twitch au premier
essai. En cas d'erreur, le message HTTP de Twitch est affiché tel quel.

Configuration, par variables d'environnement (jamais dans un fichier du dépôt) :
    TWITCH_CLIENT_ID        identifiant de l'application
    TWITCH_CLIENT_SECRET    secret de l'application
    TWITCH_REDIRECT_URI     facultatif, défaut http://localhost:3000
                            (doit être déclaré à l'identique dans la console
                            développeur de Twitch)

Les jetons sont rangés dans .tokens.json (ignoré par Git) et jamais affichés.
"""

import argparse
import asyncio
import http.server
import json
import os
import re
import secrets
import sys
import time
import urllib.parse
import webbrowser
from datetime import datetime, timezone
from pathlib import Path

import requests

HERE = Path(__file__).resolve().parent
TOKEN_FILE = HERE / ".tokens.json"
OUT_DIR = HERE / "out"

AUTH_URL = "https://id.twitch.tv/oauth2/authorize"
TOKEN_URL = "https://id.twitch.tv/oauth2/token"
VALIDATE_URL = "https://id.twitch.tv/oauth2/validate"
HELIX = "https://api.twitch.tv/helix"
EVENTSUB_WS = "wss://eventsub.wss.twitch.tv/ws"
EVENT_TYPE = "channel.channel_points_custom_reward_redemption.add"

# Gestion des récompenses et des échanges. À confirmer : la lecture seule des
# échanges serait possible avec channel:read:redemptions (voir EXP-01).
SCOPES = ["channel:manage:redemptions"]
TIMEOUT = 15


class ApiError(Exception):
    def __init__(self, status, text):
        super().__init__(f"HTTP {status} : {text}")
        self.status = status
        self.text = text


# --------------------------------------------------------------------------
# Configuration et jetons
# --------------------------------------------------------------------------

def env(name, default=None):
    value = os.environ.get(name, default)
    if not value:
        sys.exit(f"Variable d'environnement manquante : {name}")
    return value


def mask(value):
    return (value[:4] + "…") if value else "(vide)"


def save_tokens(payload):
    data = {
        "access_token": payload["access_token"],
        "refresh_token": payload.get("refresh_token"),
        "expires_at": time.time() + int(payload.get("expires_in", 0)),
        "scope": payload.get("scope", []),
    }
    TOKEN_FILE.write_text(json.dumps(data), encoding="utf-8")
    try:
        TOKEN_FILE.chmod(0o600)
    except OSError:
        pass  # Windows : pas de chmod significatif
    return data


def load_tokens():
    if not TOKEN_FILE.exists():
        sys.exit("Pas de jeton. Lancer d'abord : python twitch_points.py auth")
    return json.loads(TOKEN_FILE.read_text(encoding="utf-8"))


def refresh_tokens():
    tokens = load_tokens()
    if not tokens.get("refresh_token"):
        sys.exit("Pas de jeton de rafraîchissement. Relancer : auth")
    r = requests.post(
        TOKEN_URL,
        data={
            "grant_type": "refresh_token",
            "refresh_token": tokens["refresh_token"],
            "client_id": env("TWITCH_CLIENT_ID"),
            "client_secret": env("TWITCH_CLIENT_SECRET"),
        },
        timeout=TIMEOUT,
    )
    if not r.ok:
        raise ApiError(r.status_code, r.text)
    return save_tokens(r.json())


def ensure_token():
    tokens = load_tokens()
    if tokens["expires_at"] - time.time() < 120:
        tokens = refresh_tokens()
    return tokens


# --------------------------------------------------------------------------
# Autorisation (E0)
# --------------------------------------------------------------------------

class _CallbackHandler(http.server.BaseHTTPRequestHandler):
    result = {}

    def do_GET(self):
        query = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        if "code" in query or "error" in query:
            type(self).result.update({k: v[0] for k, v in query.items()})
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(
            "<p>Autorisation reçue. Vous pouvez fermer cette page.</p>".encode("utf-8")
        )

    def log_message(self, *args):
        pass  # pas de journal HTTP : l'adresse contient le code d'autorisation


def cmd_auth(_args):
    redirect = env("TWITCH_REDIRECT_URI", "http://localhost:3000")
    parsed = urllib.parse.urlparse(redirect)
    if parsed.scheme != "http" or parsed.hostname not in ("localhost", "127.0.0.1"):
        sys.exit("TWITCH_REDIRECT_URI doit être de la forme http://localhost:PORT")
    state = secrets.token_urlsafe(16)
    url = AUTH_URL + "?" + urllib.parse.urlencode({
        "client_id": env("TWITCH_CLIENT_ID"),
        "redirect_uri": redirect,
        "response_type": "code",
        "scope": " ".join(SCOPES),
        "state": state,
    })
    _CallbackHandler.result = {}
    server = http.server.HTTPServer((parsed.hostname, parsed.port or 80), _CallbackHandler)
    server.timeout = 1
    print("Ouverture du navigateur. Sinon, ouvrir cette adresse :\n" + url + "\n")
    webbrowser.open(url)
    deadline = time.time() + 180
    while not _CallbackHandler.result and time.time() < deadline:
        server.handle_request()
    server.server_close()
    result = _CallbackHandler.result
    if not result:
        sys.exit("Délai dépassé sans réponse de Twitch.")
    if "error" in result:
        sys.exit(f"Autorisation refusée : {result.get('error_description', result['error'])}")
    if result.get("state") != state:
        sys.exit("Paramètre state invalide : abandon.")
    r = requests.post(
        TOKEN_URL,
        data={
            "client_id": env("TWITCH_CLIENT_ID"),
            "client_secret": env("TWITCH_CLIENT_SECRET"),
            "code": result["code"],
            "grant_type": "authorization_code",
            "redirect_uri": redirect,
        },
        timeout=TIMEOUT,
    )
    if not r.ok:
        raise ApiError(r.status_code, r.text)
    data = save_tokens(r.json())
    print(f"Jeton enregistré ({TOKEN_FILE.name}). Autorisations : {data['scope']}")


def cmd_whoami(_args):
    tokens = ensure_token()
    r = requests.get(
        VALIDATE_URL,
        headers={"Authorization": f"OAuth {tokens['access_token']}"},
        timeout=TIMEOUT,
    )
    if not r.ok:
        raise ApiError(r.status_code, r.text)
    info = r.json()
    print(f"Compte : {info.get('login')} (id {info.get('user_id')})")
    print(f"Autorisations : {info.get('scopes')}")
    print(f"Expire dans : {info.get('expires_in')} s")


def cmd_refresh(_args):
    data = refresh_tokens()
    print(f"Jeton rafraîchi. Expire dans {int(data['expires_at'] - time.time())} s.")


# --------------------------------------------------------------------------
# Appels à l'API Helix
# --------------------------------------------------------------------------

def api(method, path, params=None, body=None, retry=True):
    tokens = ensure_token()
    r = requests.request(
        method,
        HELIX + path,
        params=params,
        json=body,
        headers={
            "Authorization": f"Bearer {tokens['access_token']}",
            "Client-Id": env("TWITCH_CLIENT_ID"),
        },
        timeout=TIMEOUT,
    )
    if r.status_code == 401 and retry:
        refresh_tokens()
        return api(method, path, params, body, retry=False)
    if not r.ok:
        raise ApiError(r.status_code, r.text)
    return r.json() if r.content else None


_broadcaster_id = None


def broadcaster_id():
    global _broadcaster_id
    if _broadcaster_id is None:
        tokens = ensure_token()
        r = requests.get(
            VALIDATE_URL,
            headers={"Authorization": f"OAuth {tokens['access_token']}"},
            timeout=TIMEOUT,
        )
        if not r.ok:
            raise ApiError(r.status_code, r.text)
        _broadcaster_id = r.json()["user_id"]
    return _broadcaster_id


def str_to_bool(value):
    if value.lower() in ("true", "1", "oui", "yes"):
        return True
    if value.lower() in ("false", "0", "non", "no"):
        return False
    raise argparse.ArgumentTypeError("attendu : true ou false")


def print_reward(r):
    print(
        f"{r.get('id')}  {r.get('title')!r}  coût={r.get('cost')}  "
        f"actif={r.get('is_enabled')}  pause={r.get('is_paused')}  "
        f"saute_la_file={r.get('should_redemptions_skip_request_queue')}"
    )


def cmd_reward_create(args):
    body = {
        "title": args.title,
        "cost": args.cost,
        "is_enabled": True,
        "should_redemptions_skip_request_queue": args.skip_queue,
    }
    if args.prompt:
        body["prompt"] = args.prompt
    res = api("POST", "/channel_points/custom_rewards",
              params={"broadcaster_id": broadcaster_id()}, body=body)
    for r in res.get("data", []):
        print("Récompense créée :")
        print_reward(r)


def cmd_reward_list(args):
    res = api("GET", "/channel_points/custom_rewards", params={
        "broadcaster_id": broadcaster_id(),
        "only_manageable_rewards": "true" if args.manageable else "false",
    })
    rewards = res.get("data", [])
    if not rewards:
        print("Aucune récompense.")
    for r in rewards:
        print_reward(r)


def cmd_reward_update(args):
    body = {}
    if args.paused is not None:
        body["is_paused"] = args.paused
    if args.enabled is not None:
        body["is_enabled"] = args.enabled
    if args.cost is not None:
        body["cost"] = args.cost
    if args.title is not None:
        body["title"] = args.title
    if not body:
        sys.exit("Rien à modifier : donner --paused, --enabled, --cost ou --title.")
    res = api("PATCH", "/channel_points/custom_rewards",
              params={"broadcaster_id": broadcaster_id(), "id": args.id}, body=body)
    for r in res.get("data", []):
        print("Récompense modifiée :")
        print_reward(r)


def cmd_reward_delete(args):
    if not args.yes and input(f"Supprimer la récompense {args.id} ? [o/N] ").lower() != "o":
        sys.exit("Annulé.")
    api("DELETE", "/channel_points/custom_rewards",
        params={"broadcaster_id": broadcaster_id(), "id": args.id})
    print("Récompense supprimée.")


def cmd_redemptions(args):
    res = api("GET", "/channel_points/custom_rewards/redemptions", params={
        "broadcaster_id": broadcaster_id(),
        "reward_id": args.reward_id,
        "status": args.status,
    })
    items = res.get("data", [])
    if not items:
        print("Aucun échange.")
    for it in items:
        print(f"{it.get('id')}  {it.get('user_login')}  {it.get('status')}  "
              f"{it.get('redeemed_at')}")


def cmd_redemption_set(args):
    res = api("PATCH", "/channel_points/custom_rewards/redemptions", params={
        "id": args.id,
        "broadcaster_id": broadcaster_id(),
        "reward_id": args.reward_id,
    }, body={"status": args.status})
    for it in res.get("data", []):
        print(f"Échange {it.get('id')} : statut {it.get('status')}")
    print("Vérifier maintenant les points du compte spectateur (essai E6 / E7).")


# --------------------------------------------------------------------------
# Écoute des échanges (EventSub, WebSocket)
# --------------------------------------------------------------------------

def parse_ts(value):
    """Lit un horodatage RFC 3339 de Twitch (jusqu'à 9 chiffres de fraction)."""
    if not value:
        return None
    value = re.sub(r"(\.\d{6})\d+", r"\1", value).replace("Z", "+00:00")
    return datetime.fromisoformat(value)


def delay_ms(ts, now):
    parsed = parse_ts(ts)
    return None if parsed is None else (now - parsed).total_seconds() * 1000


def parse_message(raw, seen):
    """Lit un message EventSub ; signale les messages déjà vus (essai E9)."""
    msg = json.loads(raw)
    meta = msg.get("metadata", {})
    message_id = meta.get("message_id")
    duplicate = message_id in seen if message_id else False
    if message_id:
        seen.add(message_id)
    return {
        "type": meta.get("message_type", "unknown"),
        "id": message_id,
        "duplicate": duplicate,
        "timestamp": meta.get("message_timestamp"),
        "payload": msg.get("payload", {}),
    }


def subscribe(session_id, reward_id):
    condition = {"broadcaster_id": broadcaster_id()}
    if reward_id:
        condition["reward_id"] = reward_id
    return api("POST", "/eventsub/subscriptions", body={
        "type": EVENT_TYPE,
        "version": "1",
        "condition": condition,
        "transport": {"method": "websocket", "session_id": session_id},
    })


class Stats:
    def __init__(self):
        self.events = 0
        self.duplicates = 0
        self.delays = []

    def summary(self):
        print(f"\nÉvénements reçus : {self.events}  doublons : {self.duplicates}")
        if self.delays:
            print(f"Délai échange → réception (ms) : min {min(self.delays):.0f}  "
                  f"moyen {sum(self.delays) / len(self.delays):.0f}  "
                  f"max {max(self.delays):.0f}")
            print("(approximatif : dépend de l'horloge de cette machine)")


def log_event(record):
    OUT_DIR.mkdir(exist_ok=True)
    with open(OUT_DIR / "events.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def show_notification(parsed, stats):
    now = datetime.now(timezone.utc)
    event = parsed["payload"].get("event", {})
    reward = event.get("reward", {})
    stats.events += 1
    stats.duplicates += 1 if parsed["duplicate"] else 0
    d_redeem = delay_ms(event.get("redeemed_at"), now)
    d_msg = delay_ms(parsed["timestamp"], now)
    if d_redeem is not None:
        stats.delays.append(d_redeem)
    flag = "  [DOUBLON]" if parsed["duplicate"] else ""
    print(
        f"{now.strftime('%H:%M:%S.%f')[:-3]}  récompense={reward.get('title')!r} "
        f"(id {reward.get('id')})  par={event.get('user_login')}  "
        f"statut={event.get('status')}  échange={event.get('id')}  "
        f"délai={d_redeem if d_redeem is None else round(d_redeem)} ms  "
        f"(depuis l'envoi Twitch : {d_msg if d_msg is None else round(d_msg)} ms){flag}"
    )
    log_event({
        "received_at": now.isoformat(),
        "message_id": parsed["id"],
        "duplicate": parsed["duplicate"],
        "delay_ms": d_redeem,
        "event": event,
    })


async def listen(reward_id):
    import websockets  # importé ici : les autres commandes n'en ont pas besoin

    stats = Stats()
    seen = set()
    url = EVENTSUB_WS
    need_subscribe = True
    print("Écoute des échanges. Ctrl+C pour arrêter.")
    try:
        while True:
            try:
                async with websockets.connect(url) as ws:
                    keepalive = 15
                    while True:
                        raw = await asyncio.wait_for(ws.recv(), timeout=keepalive + 10)
                        parsed = parse_message(raw, seen)
                        kind = parsed["type"]
                        if kind == "session_welcome":
                            session = parsed["payload"]["session"]
                            keepalive = session.get("keepalive_timeout_seconds") or 15
                            if need_subscribe:
                                await asyncio.to_thread(subscribe, session["id"], reward_id)
                                need_subscribe = False
                                print(f"Abonné ({EVENT_TYPE}).")
                            else:
                                print("Reconnecté, abonnement conservé.")
                        elif kind == "notification":
                            show_notification(parsed, stats)
                        elif kind == "session_reconnect":
                            url = parsed["payload"]["session"]["reconnect_url"]
                            print("Twitch demande de se reconnecter.")
                            break
                        elif kind == "revocation":
                            print(f"Abonnement révoqué : {parsed['payload']}")
                            return stats
                        # session_keepalive : rien à faire
            except (asyncio.TimeoutError, OSError,
                    websockets.exceptions.ConnectionClosed) as exc:
                print(f"Connexion perdue ({type(exc).__name__}). Nouvelle tentative dans 3 s.")
                url = EVENTSUB_WS
                need_subscribe = True
                await asyncio.sleep(3)
    except asyncio.CancelledError:
        pass
    return stats


def cmd_listen(args):
    stats = Stats()
    try:
        stats = asyncio.run(listen(args.reward_id)) or stats
    except KeyboardInterrupt:
        pass
    stats.summary()


# --------------------------------------------------------------------------
# Ligne de commande
# --------------------------------------------------------------------------

def build_parser():
    p = argparse.ArgumentParser(description="EXP-01 : points de chaîne Twitch (script jetable)")
    sub = p.add_subparsers(dest="command", required=True)

    sub.add_parser("auth", help="E0 : obtenir un jeton").set_defaults(func=cmd_auth)
    sub.add_parser("whoami", help="E0 : vérifier le jeton").set_defaults(func=cmd_whoami)
    sub.add_parser("refresh", help="E10 : forcer le rafraîchissement du jeton").set_defaults(func=cmd_refresh)

    s = sub.add_parser("reward-create", help="E1 / E7 : créer une récompense")
    s.add_argument("--title", required=True)
    s.add_argument("--cost", type=int, default=1)
    s.add_argument("--prompt")
    s.add_argument("--skip-queue", action="store_true",
                   help="récompense qui saute la file de demandes (essai E7)")
    s.set_defaults(func=cmd_reward_create)

    s = sub.add_parser("reward-list", help="E3 / E5 : lister les récompenses")
    s.add_argument("--manageable", action="store_true",
                   help="seulement celles que cette application peut modifier")
    s.set_defaults(func=cmd_reward_list)

    s = sub.add_parser("reward-update", help="E4 / E5 / E11 : pause, activation, coût, titre")
    s.add_argument("id")
    s.add_argument("--paused", type=str_to_bool)
    s.add_argument("--enabled", type=str_to_bool)
    s.add_argument("--cost", type=int)
    s.add_argument("--title")
    s.set_defaults(func=cmd_reward_update)

    s = sub.add_parser("reward-delete", help="supprimer une récompense créée par ce script")
    s.add_argument("id")
    s.add_argument("--yes", action="store_true")
    s.set_defaults(func=cmd_reward_delete)

    s = sub.add_parser("redemptions", help="E6 / E7 : lister les échanges d'une récompense")
    s.add_argument("--reward-id", required=True)
    s.add_argument("--status", default="UNFULFILLED",
                   choices=["UNFULFILLED", "FULFILLED", "CANCELED"])
    s.set_defaults(func=cmd_redemptions)

    s = sub.add_parser("redemption-set", help="E6 / E7 : valider ou annuler (rembourser) un échange")
    s.add_argument("--reward-id", required=True)
    s.add_argument("--id", required=True, help="identifiant de l'échange")
    s.add_argument("--status", required=True, choices=["FULFILLED", "CANCELED"])
    s.set_defaults(func=cmd_redemption_set)

    s = sub.add_parser("listen", help="E2 / E3 / E8 / E9 / E10 : écouter les échanges en direct")
    s.add_argument("--reward-id", help="se limiter à une récompense (sinon toutes)")
    s.set_defaults(func=cmd_listen)
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    try:
        args.func(args)
    except ApiError as exc:
        sys.exit(f"Erreur : {exc}")
    except requests.RequestException as exc:
        sys.exit(f"Erreur réseau : {exc}")


if __name__ == "__main__":
    main()
