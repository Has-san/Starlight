# UC-ADM-11 : Valider ou annuler une configuration en cours (aperçu)

*Statut : validé.*

| Champ | Contenu |
|---|---|
| **Acteur principal** | Administrateur (le Streamer pour son choix des secteurs du mode Stream, UC-STR-05) |
| **Objectif** | Voir l'effet d'une configuration sur les étoiles avant de l'appliquer, puis la valider ou l'annuler. |
| **Déclencheur** | L'acteur commence une modification dans un cas d'usage de configuration (UC-ADM-01 à 04, 07 et 10 pour l'Administrateur ; UC-STR-05 pour le Streamer). |
| **Préconditions** | En mode Stream, la configuration n'est pas verrouillée (voir UC-ADM-09). |

Schéma : [UC-ADM-11.drawio.svg](UC-ADM-11.drawio.svg).

## Vocabulaire

- **Session d'édition** : suite de modifications faites avant de valider ou d'annuler.
- **Aperçu** : application provisoire, sur les étoiles, de la configuration en cours d'édition, qui n'est pas encore enregistrée.

## Interrupteur de l'aperçu

Chaque acteur (Administrateur, Streamer) peut **activer ou désactiver l'aperçu à tout moment**, avec un interrupteur qui lui est propre (l'ouverture à d'autres rôles est une évolution possible, voir ID-11). Valeur par défaut : activé, pour tous.

Si l'acteur coupe l'aperçu alors qu'il a des modifications en attente, Starlight lui demande d'abord de les valider ou de les annuler : rien n'est appliqué en silence.

Aperçu désactivé : les étapes 2 et 3 du scénario n'ont pas lieu, donc les étoiles ne bougent pas et la file n'est pas mise en pause. La validation reste obligatoire et la configuration validée s'applique ensuite comme d'habitude. Cela permet de modifier une séquence en mode Stream sans que les spectateurs voient quoi que ce soit.

## Scénario nominal

1. L'acteur commence à modifier la configuration : une session d'édition s'ouvre.
2. À chaque modification dont l'effet est visible, Starlight montre l'**aperçu** sur les étoiles concernées, sans tenir compte des secteurs du mode (comme un test manuel).
3. Pendant l'aperçu, la **file de réactions est en pause** et aucune réaction n'est perdue. Starlight alerte l'Administrateur quand des réactions attendent, en indiquant leur nombre.
4. L'Administrateur peut poursuivre ses modifications (les étapes 2 et 3 se répètent).
5. L'Administrateur **valide**. Starlight vérifie la configuration, l'enregistre en une fois et l'applique au système, puis consigne les modifications dans le journal (acteur, ancien et nouvel état). L'affichage suit tout de suite la configuration validée et la file reprend.

## Règles

- **Rien n'est appliqué au reste du système avant la validation.** Les événements, les ambiances et les réactions utilisent la configuration validée.
- Les événements qui arrivent pendant un aperçu sont mis en file avec la configuration validée à leur arrivée (voir QO-44). Il n'y a pas de taille maximale de la file pour l'instant.
- **Une réaction en cours n'est pas coupée** : l'aperçu commence quand elle se termine (voir QO-24).
- L'aperçu ne change pas l'ambiance courante : elle reste celle d'avant la session.
- Une modification sans effet visible (renommer une étoile, associer une réaction à un événement) n'a pas d'aperçu, mais passe par la même validation.
- **Même avec l'aperçu désactivé**, l'Administrateur peut lancer un essai explicite d'une séquence sur une étoile ou un secteur de son choix (voir UC-ADM-04).
- **Une seule session d'édition à la fois**, tous acteurs confondus : si une session est ouverte, l'autre acteur reçoit le message « une édition est déjà en cours ».
- Le choix du Streamer pour les secteurs du mode Stream (UC-STR-05) suit le même mécanisme (aperçu, validation ou annulation) ; il n'est pas touché par le verrou de UC-ADM-09.
- En mode Stream, un aperçu agit sur les vraies étoiles, visibles des spectateurs : c'est la raison d'être du verrou de UC-ADM-09.

## Scénarios alternatifs

- **A1, annulation** : l'Administrateur annule. Les modifications sont abandonnées, rien n'est enregistré, l'affichage revient à l'ambiance courante et la file reprend. L'annulation est consignée.
- **A2, validation refusée** : la configuration viole une règle (par exemple supprimer un secteur désigné par une ambiance). Starlight l'explique, rien n'est enregistré et la session reste ouverte.
- **A3, session interrompue** (fermeture de l'application, perte de liaison) : la session est abandonnée comme une annulation ; la configuration validée reste en place et la file reprend.
- **A4, session oubliée ouverte** : voir « Points non tranchés ».

## Postconditions

- Validation : la configuration est enregistrée et appliquée, le journal l'indique, l'affichage suit la configuration et la file reprend.
- Annulation ou interruption : la configuration est inchangée, l'affichage est celui de l'ambiance courante et la file reprend.

## Points non tranchés

- **Durée maximale d'une session** : une session oubliée ouverte laisserait la file en pause et les étoiles bloquées. Proposé : annulation automatique après un délai d'inactivité, avec alerte (QO-54). Le cas du Streamer en direct la rend plus urgente.

## Questions liées

QO-03, QO-12, QO-24, QO-34, QO-44, QO-52, QO-53, QO-54
