# Documentation de Starlight

La documentation est rédigée en **français**. Le code, les noms de dossiers et les identifiants sont en **anglais** : le [glossaire](glossaire.md) donne la correspondance entre les deux.

## Organisation

Les dossiers numérotés suivent les phases du projet, dans l'ordre de lecture.

| Dossier | Contenu |
|---|---|
| [`01-besoin/`](01-besoin/) | Expression du besoin : acteurs, cas d'usage |
| [`02-specifications/`](02-specifications/) | Exigences fonctionnelles et non fonctionnelles |
| [`03-architecture/`](03-architecture/) | Architecture logicielle et matérielle |
| [`04-conception/`](04-conception/) | Conception détaillée des modules |
| [`05-validation/`](05-validation/) | Plans de test d'intégration et de validation, résultats |
| [`decisions/`](decisions/) | Décisions structurantes (ADR) |

Documents transverses, à la racine de `docs/` :

- `glossaire.md` — vocabulaire du projet (français ↔ anglais)
- `questions-ouvertes.md` — registre des questions ouvertes (QO-xx)
- `idees.md` — idées gardées pour plus tard

## Conventions

- Identifiants stables, jamais réutilisés : `UC-CON-01`, `QO-12`, `ADR-0001`, `EXP-01`.
- Un fichier par cas d'usage, nommé par son identifiant (`UC-STR-02.md`).
- Schémas au format `.drawio.svg`, à côté du document qu'ils illustrent : GitHub les affiche, draw.io les édite.
