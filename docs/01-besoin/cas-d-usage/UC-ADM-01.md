# UC-ADM-01 : Consulter et nommer les étoiles

*Statut : validé.*

| Champ | Contenu |
|---|---|
| **Acteur principal** | Administrateur |
| **Objectif** | Savoir quelles étoiles existent, si elles sont disponibles, et leur donner un nom parlant. |
| **Déclencheur** | L'Administrateur ouvre la liste des étoiles. |
| **Préconditions** | Le pilote a annoncé ses étoiles à Starlight. Pour **nommer** en mode Stream, la configuration n'est pas verrouillée (voir UC-ADM-09) ; **consulter** reste toujours possible. |

## Principe

Les étoiles viennent du pilote : il annonce à Starlight le matériel qu'il embarque, avec un **identifiant stable** pour chaque étoile. Starlight ne crée ni ne supprime d'étoile. Ajouter du matériel demande du développement du pilote.

La liste montre, pour chaque étoile :
- son **identifiant** (donné par le pilote, qui ne change pas) ;
- son **nom** (donné par l'Administrateur ; par défaut, l'identifiant) ;
- sa **disponibilité** : disponible ou indisponible ;
- les **secteurs** auxquels elle appartient.

## Scénario nominal : nommer une étoile

1. L'Administrateur ouvre la liste des étoiles.
2. Starlight affiche les étoiles annoncées par le pilote, avec leur nom, leur disponibilité et leurs secteurs.
3. L'Administrateur choisit une étoile et saisit un nom.
4. Starlight vérifie que le nom n'est pas déjà utilisé, l'enregistre et consigne le changement dans le journal (acteur, étoile, ancien et nouveau nom).

## Règles

- Les modifications passent par un aperçu, puis une validation ou une annulation (UC-ADM-11).
- **Une étoile indisponible reste dans la liste**, signalée comme indisponible. Le retrait d'une étoile définitivement absente n'est pas prévu pour l'instant (voir QO-47).
- **Une nouvelle étoile annoncée par le pilote** apparaît dans la liste avec l'identifiant pour nom. Si elle ne fait partie d'aucun secteur d'un mode, l'Administrateur en est alerté (alerte non bloquante, affichée dans la configuration et consignée ; voir QO-48).
- Une étoile peut appartenir à plusieurs secteurs ; l'appartenance se règle dans UC-ADM-02.

## Scénarios alternatifs

- **A1, nom déjà utilisé** : refusé, rien n'est enregistré.
- **A2, le pilote n'annonce plus une étoile connue** : elle passe à « indisponible » et le changement est consigné (voir QO-14).
- **A3, une étoile indisponible redevient disponible** : son état est mis à jour et consigné.
- **A4, pilote injoignable** : la liste connue est conservée et toutes les étoiles apparaissent comme indisponibles.
- **A5, configuration verrouillée en mode Stream** : renommer est refusé ; consulter reste possible. L'Administrateur peut lever le verrou (UC-ADM-09).

## Postconditions

- Les noms reflètent la demande, ou restent inchangés si elle est refusée.
- Le journal indique l'acteur et le changement.

## Points non tranchés

- Retrait d'une étoile définitivement absente (QO-47).
- Un seul pilote aujourd'hui. Si d'autres arrivent, un module unique sera seul à connaître leur pluralité et les présentera au reste du système comme un seul pilote (QO-47).

## Questions liées

QO-04, QO-14, QO-47, QO-48
