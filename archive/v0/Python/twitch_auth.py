from urllib.parse import urlencode, urlparse, parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import webbrowser
import time
import serial
from twitch_api import get_current_user
from twitch_websocket import start


AUTH_CODE = None


def load_config(path: str) -> dict:
    config = {}

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if "=" not in line:
                continue

            key, value = line.split("=", 1)
            config[key.strip()] = value.strip()

    return config


def validate_config(config: dict) -> bool:
    required_keys = ["CLIENT_ID", "CLIENT_SECRET", "REDIRECT_URL", "ARDUINO_PORT"]

    for key in required_keys:
        if not config.get(key):
            print(f"Configuration manquante : {key}")
            return False

    return True


def build_auth_url(client_id: str, redirect_url: str, scopes: list[str]) -> str:
    base_url = "https://id.twitch.tv/oauth2/authorize"

    params = {
        "client_id": client_id,
        "redirect_uri": redirect_url,
        "response_type": "code",
        "scope": " ".join(scopes),
    }

    return f"{base_url}?{urlencode(params)}"


class OAuthCallbackHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global AUTH_CODE

        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)

        if "code" in query_params:
            AUTH_CODE = query_params["code"][0]

            self.send_response(200)
            self.end_headers()
            self.wfile.write(
                b"Connexion Twitch reussie. Vous pouvez fermer cette fenetre."
            )
        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(
                b"Erreur : aucun code OAuth recu."
            )

    def log_message(self, format, *args):
        pass


def wait_for_auth_code(port: int = 3000) -> str:
    server = HTTPServer(("localhost", port), OAuthCallbackHandler)

    print("En attente du retour Twitch...")
    server.handle_request()

    if AUTH_CODE is None:
        raise RuntimeError("Aucun code OAuth recu.")

    return AUTH_CODE


def exchange_code_for_token(
    client_id: str,
    client_secret: str,
    redirect_url: str,
    code: str,
) -> dict:
    response = requests.post(
        "https://id.twitch.tv/oauth2/token",
        data={
            "client_id": client_id,
            "client_secret": client_secret,
            "code": code,
            "grant_type": "authorization_code",
            "redirect_uri": redirect_url,
        },
        timeout=10,
    )

    response.raise_for_status()
    return response.json()


def main() -> None:
    print("Démarrage...")

    config = load_config("config.txt")

    if not validate_config(config):
        print("Config invalide.")
        return

    client_id = config["CLIENT_ID"]
    client_secret = config["CLIENT_SECRET"]
    redirect_url = config["REDIRECT_URL"]
    arduino_port = config["ARDUINO_PORT"]

    scopes = [
        "channel:read:redemptions",
        "moderator:read:followers",
        "channel:read:subscriptions",
    ]

    auth_url = build_auth_url(client_id, redirect_url, scopes)
    print("Ouvre ce lien si le navigateur ne s'ouvre pas :")
    print(auth_url)

    webbrowser.open(auth_url)

    code = wait_for_auth_code(port=3000)
    print("Code OAuth recu.")

    token_data = exchange_code_for_token(
        client_id=client_id,
        client_secret=client_secret,
        redirect_url=redirect_url,
        code=code,
    )

    print("Access token recu.")

    user = get_current_user(client_id, token_data["access_token"])
    print(f"Connecte en tant que : {user['display_name']} (id: {user['id']})")

    with serial.Serial(arduino_port, 9600, timeout=1) as arduino:
        time.sleep(2)
        print("Arduino connecte.")

        start(
            client_id=client_id,
            access_token=token_data["access_token"],
            user_id=user["id"],
            arduino=arduino,
        )


if __name__ == "__main__":
    main()
