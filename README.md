# Starlight

Système de lumières pilotables. Chaque source de lumière est une **étoile** ; on les pilote une par une, par secteur ou toutes ensemble, au moyen d'ambiances, de séquences et de réactions.

Starlight fonctionne en deux modes :

- **Lounge** : ambiances pour le salon, choisies par les personnes présentes.
- **Stream** : les lumières réagissent aux événements d'une plateforme de streaming (Twitch en premier lieu).

## État du projet

Phase actuelle : **expression du besoin**. Aucun code de production n'est encore écrit.

Le projet avance par étapes : besoin, spécifications, architecture logicielle et matérielle, conception, développement modulaire, validation.
Une première version (preuve de faisabilité : un follow Twitch allume une LED) est archivée dans [`archive/v0/`](archive/v0/README.md) et marquée par le tag `v0-legacy`.

## Pour commencer la lecture

1. [Glossaire](docs/glossaire.md) : le vocabulaire du projet, et son équivalent anglais dans le code
2. [Acteurs](docs/01-besoin/acteurs.md) et [inventaire des cas d'usage](docs/01-besoin/cas-d-usage/)
3. [Questions ouvertes](docs/questions-ouvertes.md) et [idées](docs/idees.md)

## Organisation du dépôt

| Dossier | Contenu |
|---|---|
| [`docs/`](docs/) | Documentation (en français), organisée par phase |
| [`host/`](host/) | Logiciel du PC hôte (Python) : cœur du projet |
| [`firmware/`](firmware/) | Logiciel du microcontrôleur qui pilote les étoiles |
| [`simulator/`](simulator/) | Étoiles simulées, pour développer et tester sans matériel |
| [`hardware/`](hardware/) | Matériel : dimensionnement, câblage, nomenclature |
| [`experiments/`](experiments/) | Expériences techniques jetables, jamais importées par le reste du code |
| [`archive/`](archive/) | Anciennes versions, non maintenues |

## Contribuer

Voir [CONTRIBUTING.md](CONTRIBUTING.md).

## Licence

Distribué sous licence MIT : voir [`LICENSE`](LICENSE).
