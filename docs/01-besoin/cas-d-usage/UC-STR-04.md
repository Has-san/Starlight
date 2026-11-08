# UC-STR-04 : Interdire ou autoriser des types d'événements Twitch

*Statut : à valider (modifié le 8 novembre : interrupteur par type d'événement).*

| Champ | Contenu |
|---|---|
| **Acteur principal** | Streamer (l'Administrateur peut faire de même) |
| **Objectif** | Choisir les types d'événements Twitch qui peuvent déclencher des réactions, tout en gardant ses propres ambiances et réactions. |
| **Déclencheur** | Le Streamer interdit ou autorise un type d'événement, ou utilise « tout interdire » / « tout autoriser ». |
| **Préconditions** | Starlight est en mode Stream. |

## Principe

- Chaque type d'événement connu de Starlight (voir UC-ADM-07) a un **interrupteur** : autorisé ou interdit. Exemples : follow, abonnement, bits, raid, et **chaque récompense de points de chaîne** (une récompense est un type d'événement).
- « Tout interdire » et « tout autoriser » sont des raccourcis qui basculent tous les interrupteurs d'un coup.
- Exemple : ne garder que les abonnements et les bits, en interdisant le reste.
- Un interrupteur ne modifie pas l'association événement → réaction (UC-ADM-07) : elle est conservée et redevient active à l'autorisation.
- L'interdiction est une **option du mode Stream**, pas un mode (voir QO-41).

## Scénario nominal : interdire un type

1. Le Streamer interdit un type d'événement (ou utilise « tout interdire »).
2. Starlight ignore dès lors les événements de ce type : ils ne produisent aucune réaction.
3. Starlight consigne dans le journal le changement (acteur, type concerné) et compte les événements ignorés, type par type.
4. Pour un type payé en points de chaîne, Starlight fait au mieux pour que les points ne puissent plus être dépensés (mise en pause de la récompense, voir QO-42), afin que personne ne soit lésé.
5. Les réactions déjà en cours ou en attente ne sont pas touchées (voir QO-43) ; le Streamer peut les supprimer avec UC-STR-03.
6. Les ambiances et les réactions manuelles du Streamer restent possibles (UC-STR-01, UC-STR-02).

## Scénario nominal : autoriser un type

1. Le Streamer autorise un type d'événement (ou utilise « tout autoriser »).
2. Starlight traite de nouveau les événements de ce type reçus à partir de ce moment (et remet la récompense en service s'il l'avait mise en pause).
3. Les événements ignorés ne sont pas rejoués : ils seraient périmés (voir QO-41).
4. Starlight consigne dans le journal le changement et le nombre d'événements ignorés pour ce type.

## Début de session

Les interrupteurs restent tels quels d'un live à l'autre : rien n'est réinitialisé automatiquement.

À l'entrée en mode Stream, la régie du Streamer affiche un **récapitulatif** : la liste de tous les types d'événements avec leur état (autorisé ou interdit), les types interdits étant mis en évidence. Depuis ce récapitulatif, le Streamer peut modifier chaque interrupteur ou utiliser « tout autoriser ».

- L'affichage est **non bloquant** : il n'empêche ni les ambiances, ni les réactions manuelles, et les événements sont traités selon l'état enregistré sans attendre.
- La **confirmation est obligatoire** : le récapitulatif reste affiché, avec une alerte persistante, tant que le Streamer n'a pas confirmé (« j'ai vu l'état »). La confirmation est consignée dans le journal (acteur, moment).
- Si la régie n'est pas ouverte à l'entrée en mode Stream, le récapitulatif l'attend ; le journal indique « non confirmé » tant qu'il n'y a pas eu de confirmation.

## Limite à connaître

Seuls les événements payés en points de chaîne peuvent être bloqués en amont. Un abonnement, des bits, un raid ou un follow se font hors de Starlight : on peut seulement les ignorer, et le spectateur ne reçoit alors aucune réaction en retour.

## Scénarios alternatifs

- **A1, mode Lounge actif** : la demande est ignorée (les événements Twitch sont déjà ignorés en mode Lounge).
- **A2, déjà dans l'état demandé** : aucun changement.
- **A3, entrée en mode Stream** : voir « Début de session » (récapitulatif et confirmation, QO-57).
- **A4, échanges de points de chaîne reçus malgré l'interdiction** : leur traitement (annulation avec remboursement) dépend de l'expérience EXP-01 et de QO-42.

## Postconditions

- L'état de chaque type d'événement (autorisé ou interdit) est enregistré.
- Le journal indique l'acteur, le moment, le type concerné et le nombre d'événements ignorés.

## Questions liées

QO-20, QO-41, QO-42, QO-43, QO-57
