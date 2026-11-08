# EXP-01 : mode d'emploi du script

Script **jetable** pour l'expérience [EXP-01](README.md) : que peut faire Starlight avec les récompenses de points de chaîne Twitch (lecture, pause, annulation avec remboursement).

> **Ce script n'a pas été exécuté contre Twitch.** Seules la syntaxe et la logique de lecture des messages sont testées hors ligne. Les adresses de l'API sont celles connues au moment de l'écriture : les confirmer sur la documentation officielle au premier essai. Un échec fait partie de l'expérience : il se note dans le tableau d'EXP-01.

Ce dossier n'est pas du code de production. Il ne doit jamais être importé depuis `host/`.

## Mise en place

Python 3.11 ou plus.

```
cd experiments/EXP-01
python -m venv .venv
source .venv/bin/activate          # Windows : .venv\Scripts\activate
pip install -r requirements.txt
```

Variables d'environnement (ne jamais les écrire dans un fichier du dépôt) :

```
export TWITCH_CLIENT_ID="..."
export TWITCH_CLIENT_SECRET="..."
export TWITCH_REDIRECT_URI="http://localhost:3000"   # facultatif
```

Dans la console développeur de Twitch, déclarer l'adresse de redirection **à l'identique** (`http://localhost:3000` par défaut).

## Commandes et essais

| Commande | Essai d'EXP-01 |
|---|---|
| `python twitch_points.py auth` puis `whoami` | E0 : obtenir et vérifier le jeton |
| `python twitch_points.py reward-create --title "Starlight test" --cost 1` | E1 : créer une récompense |
| `python twitch_points.py listen` | E2, E3, E8, E9, E10 : écouter les échanges en direct (délais, doublons, reconnexion) |
| `python twitch_points.py reward-list` ; `reward-list --manageable` | E3, E5 : voir quelles récompenses l'application peut modifier |
| `python twitch_points.py reward-update ID --paused true` | E4, E5, E11 : pause, ou `--enabled false` |
| `python twitch_points.py redemptions --reward-id ID` | E6, E7 : lister les échanges à traiter |
| `python twitch_points.py redemption-set --reward-id ID --id ECHANGE --status CANCELED` | E6, E7 : annuler (rembourser) un échange |
| `python twitch_points.py reward-create --title "Saute la file" --skip-queue` | E7 : récompense qui saute la file de demandes |
| `python twitch_points.py refresh` | E10 : forcer le rafraîchissement du jeton |

Laisser `listen` tourner dans un terminal pendant que le compte spectateur échange des points dans un autre.

## Fichiers produits (ignorés par Git)

- `.tokens.json` : jetons de l'application. **Ne jamais le partager ni le committer.**
- `out/events.jsonl` : un événement reçu par ligne. Il contient les pseudos des spectateurs : ne pas le publier.

## Tests hors ligne

```
python -m unittest test_twitch_points -v
```

## Après l'expérience

Reporter les résultats dans le tableau d'EXP-01 (sans aucun secret), puis mettre à jour les questions ouvertes concernées (QO-41, QO-42, QO-23, QO-22, QO-25, QO-19).
