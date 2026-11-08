# Archive — Starlight v0

> ⚠️ **Version archivée, non maintenue.** Ne pas s'en servir comme base de développement.
> L'état exact de cette version est aussi marqué par le tag Git `v0-legacy`.

## Ce que c'est

Première version de Starlight, réalisée en juin 2026 comme **preuve de faisabilité** :
un événement Twitch (follow) allume une LED RVB avec la bonne séquence.

## Contenu

| Dossier | Rôle |
|---|---|
| `Python/` | Authentification OAuth Twitch, abonnement EventSub par WebSocket, passerelle événement → commande série vers l'Arduino |
| `Arduino/DriverLight/` | Firmware : réception de commandes série, pilotage d'une LED RVB (broches 9, 10, 11), couleurs et clignotement |
| `Architecture/` | Diagramme d'architecture de cette première version |

## Ce qu'on en retient

- La chaîne complète Twitch → PC hôte → microcontrôleur → LED fonctionne.
- Les identifiants Twitch étaient dans des fichiers de configuration versionnés : désormais, aucun secret n'est commité (voir le `.gitignore` à la racine).

## Lancer cette version (pour mémoire)

Les scripts lisent un fichier `Python/CONFIG.txt` (non versionné) au format :

```
CLIENT_ID=...
CLIENT_SECRET=...
REDIRECT_URL=...
ARDUINO_PORT=COM3
```
