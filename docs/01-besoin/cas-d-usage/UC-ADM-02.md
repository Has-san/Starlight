# UC-ADM-02 : Gérer les secteurs (créer, modifier, supprimer)

*Statut : validé.*

| Champ | Contenu |
|---|---|
| **Acteur principal** | Administrateur |
| **Objectif** | Regrouper des étoiles en secteurs pour pouvoir les désigner d'un coup (dans une ambiance, une séquence ou un mode). |
| **Déclencheur** | L'Administrateur ouvre la configuration des secteurs. |
| **Préconditions** | En mode Stream, la configuration n'est pas verrouillée (voir UC-ADM-09). En mode Lounge, aucune condition. |

## Ce qu'est un secteur

- Un **nom**, choisi par l'Administrateur et unique.
- Des **étoiles**, choisies dans la liste des étoiles annoncées par le pilote (y compris une étoile indisponible, voir UC-ADM-01).
- Une étoile peut appartenir à plusieurs secteurs. Un secteur ne contient **pas** d'autre secteur.
- Un secteur ne connaît pas les modes : c'est le mode qui indique les secteurs qu'il utilise (voir UC-ADM-10).

## Scénario nominal : créer un secteur

1. L'Administrateur demande la création d'un secteur.
2. Il saisit un nom.
3. Il choisit les étoiles du secteur.
4. Starlight vérifie que le nom n'est pas déjà utilisé.
5. Starlight enregistre le secteur et consigne la création dans le journal (acteur, secteur, étoiles).

Un secteur peut être créé sans étoile : cela déclenche l'alerte « secteur sans étoile », non bloquante.

Comme toute configuration, les modifications passent par un aperçu, puis une validation ou une annulation (UC-ADM-11).

## Scénarios alternatifs

- **A1, nom déjà utilisé** : la création ou le changement de nom est refusé, rien n'est enregistré.
- **A2, modifier un secteur** : l'Administrateur peut changer le nom et ajouter ou retirer des étoiles. La modification est consignée (acteur, secteur, ancien et nouvel état). Les ambiances, séquences et modes qui désignent ce secteur suivent sa nouvelle composition (voir QO-52 pour le moment où cela prend effet).
- **A3, supprimer un secteur désigné par une ambiance, une séquence ou une réaction** : refusé. L'Administrateur doit d'abord modifier ce qui l'utilise (voir QO-46).
- **A4, supprimer un secteur qui n'est utilisé que par des modes** : autorisé. Le secteur est retiré de ces modes et la suppression est consignée. Si un mode se retrouve sans secteur, l'alerte « mode sans secteur » s'applique.
- **A5, configuration verrouillée en mode Stream** : toute création, modification ou suppression est refusée. L'Administrateur peut lever le verrou (UC-ADM-09).
- **A6, alertes** : Starlight alerte l'Administrateur, sans le bloquer, quand un secteur n'a aucune étoile. L'alerte est affichée dans la configuration et consignée, à chaque modification de la configuration et au démarrage (les autres alertes sont dans UC-ADM-01 et UC-ADM-10).

## Postconditions

- La liste des secteurs reflète la demande, ou reste inchangée si elle est refusée.
- Le journal indique l'acteur et l'opération.

## Points non tranchés

Aucun. L'affichage de l'ambiance courante suit la modification en aperçu, puis la configuration validée (QO-52, tranchée).

## Questions liées

QO-46, QO-48, QO-52
