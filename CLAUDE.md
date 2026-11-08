# Starlight : consignes pour Claude

Starlight est un système de lumières pilotables (les « étoiles »), avec deux modes : Lounge et Stream. Le projet est en **phase de besoin** : il n'y a pas encore de code de production.

## À lire avant de travailler

- `docs/glossaire.md` : vocabulaire à employer tel quel, avec son équivalent anglais pour le code.
- `CONTRIBUTING.md` : langues, conventions de commit, de branches et de modules.
- `docs/questions-ouvertes.md` : questions non tranchées. Ne pas les trancher seul.
- `docs/01-besoin/cas-d-usage/README.md` : inventaire et statut des cas d'usage.

## Où ranger quoi

- Documentation par phase dans `docs/01-besoin/` à `docs/05-validation/` ; décisions structurantes dans `docs/decisions/`.
- Documents transverses à la racine de `docs/` : glossaire, questions ouvertes, idées.
- Un fichier par cas d'usage, nommé par son identifiant stable (`UC-STR-02.md`) ; mettre à jour l'inventaire en même temps.
- Schémas au format `.drawio.svg`, à côté du document qu'ils illustrent.
- Expériences dans `experiments/EXP-XX/` (fiche `README.md` et scripts).

## Règles

- Ne jamais committer directement sur `main` : branche courte `type/nom-court`, puis pull request.
- Messages de commit et titres de pull request en **français**, au format Conventional Commits (`docs: ajouter …`).
- Code, identifiants et commentaires en **anglais**, avec les termes de la colonne « Terme anglais » du glossaire.
- Ne jamais faire de push forcé sur `main`. Ne pousser que sur demande explicite.
- Ne pas modifier le titulaire dans `LICENSE`.
- Ne jamais écrire de secret (clé d'application, jeton, mot de passe) ni de donnée de spectateur dans un fichier suivi par Git, un commit, un document ou une conversation. Les secrets passent par des variables d'environnement.
- Le firmware (`firmware/`) ne dépend jamais du code de l'hôte (`host/`).
- Le code de `experiments/` est jetable : il n'est jamais importé depuis `host/`, `firmware/` ou `simulator/`.
- Une ambiguïté nouvelle se consigne dans `docs/questions-ouvertes.md` (numéro suivant, jamais réutilisé) ; une idée non retenue dans `docs/idees.md`.

## Façon de travailler

- Avancer pas à pas : une étape à la fois, sans produire la solution complète d'un coup.
- Donner un avis critique et proposer des idées, au lieu d'exécuter sans discuter.
- À résultat satisfaisant égal, préférer la maintenabilité.
