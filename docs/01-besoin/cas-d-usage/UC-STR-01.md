# UC-STR-01 : Activer une ambiance (mode Stream)

*Statut : validé.*

| Champ | Contenu |
|---|---|
| **Acteur principal** | Streamer |
| **Objectif** | Changer l'ambiance lumineuse de fond pendant le stream. |
| **Déclencheur** | Le Streamer sélectionne une ambiance via un actionneur (voir QO-11). |
| **Préconditions** | Starlight est en mode Stream. |

## Différence avec UC-CON-01

Même comportement que UC-CON-01 (activer une ambiance), avec un autre acteur et une autre précondition. La logique d'activation n'existe qu'une fois ; seul le cas de la réaction en cours est propre au mode Stream.

## Scénario nominal

1. Le Streamer sélectionne une ambiance disponible, y compris « Off ».
2. Starlight reçoit la demande et la consigne dans le journal, avec son origine (le Streamer).
3. L'ambiance sélectionnée devient l'ambiance courante et remplace la précédente.
4. Si aucune réaction n'est en cours ni en attente, Starlight applique l'ambiance aux étoiles concernées.

## Scénarios alternatifs

- **A1, mode Lounge actif** : la demande est ignorée.
- **A2, ambiance déjà courante** : aucun changement.
- **A3, étoile injoignable** : les autres étoiles appliquent l'ambiance, la défaillance est consignée dans le journal (voir QO-14).
- **A4, réaction en cours ou en attente** : l'ambiance devient courante immédiatement, mais n'est affichée qu'à la fin des réactions (sans les interrompre). Le retour après réaction se fait donc vers la **nouvelle** ambiance (voir QO-34, tranchée).

## Postconditions

- L'ambiance sélectionnée est l'ambiance courante.
- Le journal indique que la demande vient du Streamer.

## Questions liées

QO-11, QO-14, QO-34
