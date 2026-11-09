# UC-ADM-07 : Associer une réaction à un type d'événement

*Statut : validé.*

| Champ | Contenu |
|---|---|
| **Acteur principal** | Administrateur |
| **Objectif** | Décider quelle réaction (et avec quelle priorité) Starlight joue quand un type d'événement se produit. |
| **Déclencheur** | L'Administrateur ouvre la configuration des associations. |
| **Préconditions** | Au moins une réaction existe dans la liste des réactions (voir QO-31). Pour les points de chaîne, Starlight est connecté à Twitch (voir UC-ADM-08). |

Schéma : [UC-ADM-07.drawio.svg](UC-ADM-07.drawio.svg).

## Types d'événement

Un type d'événement est choisi dans une liste fermée : abonnement, don, follow, raid, etc. Les **points de chaîne** forment une famille : chaque récompense de la chaîne est un type d'événement à part entière (identifiée par son identifiant Twitch, affichée par son titre) et a donc sa propre association.

Un type d'événement a **au plus une association**.

## Scénario nominal

1. L'Administrateur consulte la liste des types d'événement et, pour chacun, son association actuelle (réaction, priorité) ou l'absence d'association.
2. Il choisit un type d'événement.
3. Il choisit la réaction à associer, parmi les réactions de la liste.
4. Il règle la priorité de l'événement. Ce réglage est libre ; les valeurs possibles restent à définir (voir QO-01 et QO-32).
5. Il enregistre.
6. Starlight vérifie que la réaction existe, enregistre l'association et la consigne dans le journal (acteur, type d'événement, ancienne et nouvelle valeur).
7. L'association s'applique aux événements suivants.

## Règles

- Les modifications passent par un aperçu, puis une validation ou une annulation (UC-ADM-11).
- **Attribution à l'arrivée (provisoire, voir QO-44)** : la réaction d'un événement est déterminée quand il arrive. Une modification ne concerne que les événements à venir ; les réactions déjà en file ne changent pas.
- **Aucune association** : un événement de ce type est ignoré et consigné dans le journal (comme A2 de UC-TWI-01).
- **« Aucune réaction » explicite** : l'Administrateur peut associer volontairement « aucune réaction » à un type. L'événement est alors ignoré et consigné, ce qui distingue un choix d'un oubli.
- La priorité fait partie de l'association : une même réaction peut avoir des priorités différentes selon le type d'événement.
- L'Administrateur peut agir en Lounge comme en Stream.

## Scénarios alternatifs

- **A1, suppression d'une réaction associée** : refusée. Une réaction actuellement associée à un type d'événement ne peut pas être supprimée ; l'Administrateur doit d'abord modifier ou retirer l'association. Il n'existe donc pas d'association invalide.
- **A2, modification, désactivation ou suppression d'une association** : même scénario que le nominal ; l'effet est le même (événements à venir uniquement).
- **A3, récompense de chaîne inconnue** : un échange arrive pour une récompense sans association. Il est traité comme « aucune association » (événement ignoré et consigné).
- **A4, Twitch non connecté** : les types liés aux points de chaîne ne peuvent pas être proposés ; les autres types restent configurables.

## Postconditions

- L'association est enregistrée, ou inchangée en cas d'erreur.
- Le journal indique l'acteur, le type d'événement et la modification.
- Les réactions déjà en file ne sont pas modifiées.

## Questions liées

QO-01, QO-22, QO-26, QO-31, QO-32, QO-42, QO-44
