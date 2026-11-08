# Contribuer à Starlight

Merci de l'intérêt porté au projet. Ce document fixe les règles de base ; il évoluera avec le projet.

## Principes

- **Maintenabilité d'abord** : à résultat satisfaisant égal, on préfère le code et la documentation les plus lisibles.
- **Vocabulaire commun** : les termes du [glossaire](docs/glossaire.md) s'emploient tels quels, en français dans la documentation et avec leur équivalent anglais (colonne « Terme anglais ») dans le code.
- **Décisions tracées** : une question non tranchée est consignée dans le [registre des questions ouvertes](docs/questions-ouvertes.md) ; une idée non retenue va dans les [idées](docs/idees.md).

## Langues

| Élément | Langue |
|---|---|
| Documentation (`docs/`, README) | français |
| Messages de commit, titres et descriptions de pull request | français |
| Code, identifiants, commentaires, noms de dossiers et de fichiers de code | anglais |

## Messages de commit

Format [Conventional Commits](https://www.conventionalcommits.org/fr/) : `type: description courte`, à l'infinitif, sans point final.

| Type | Usage |
|---|---|
| `feat` | nouvelle fonctionnalité |
| `fix` | correction de défaut |
| `docs` | documentation |
| `test` | ajout ou modification de tests |
| `refactor` | réécriture sans changement de comportement |
| `chore` | maintenance, outillage, structure du dépôt |

Exemple : `docs: ajouter le cas d'usage UC-CON-03`

## Branches et pull requests

- `main` est protégée : aucune modification directe, aucun push forcé.
- Chaque évolution se fait sur une branche courte, nommée `type/nom-court` (`feat/…`, `fix/…`, `docs/…`, `test/…`, `refactor/…`, `chore/…`), intégrée par pull request.
- Une pull request traite un seul sujet.
- Le titre de la pull request suit le format des commits : il devient le message du commit sur `main`.
- Les pull requests sont fusionnées en **« Squash and merge »** : un commit par pull request sur `main`. La branche est supprimée automatiquement après la fusion.

## Secrets et données personnelles

- Aucun secret (clé d'application, jeton, mot de passe) dans un fichier suivi par Git, un commit, une pull request ou un document. Les secrets passent par des variables d'environnement.
- Aucune donnée de spectateur (pseudo, identifiant) dans le dépôt.
- Configurez Git avec votre adresse masquée GitHub (`…@users.noreply.github.com`) si vous ne voulez pas publier votre adresse.

## Séparation des modules

- Le logiciel hôte (`host/`) et le firmware (`firmware/`) ont chacun leur chaîne d'outils. **Le firmware ne dépend jamais du code de l'hôte** : ils communiquent uniquement par le contrat de communication, documenté dans `docs/`.
- Le simulateur (`simulator/`) joue le rôle du matériel : il respecte le même contrat que le firmware.
- Le code de `experiments/` est jetable : il n'est jamais importé depuis `host/`, `firmware/` ou `simulator/`.

## À définir

- Règles de codage et niveau d'exigence.
- Stratégie de tests et intégration continue.
