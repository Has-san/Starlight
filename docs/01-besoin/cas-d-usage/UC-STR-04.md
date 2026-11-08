# UC-STR-04 : Interdire ou autoriser les événements Twitch

*Statut : validé.*

| Champ | Contenu |
|---|---|
| **Acteur principal** | Streamer |
| **Objectif** | Empêcher Twitch de déclencher des réactions, tout en gardant ses propres ambiances et réactions. |
| **Déclencheur** | Le Streamer demande d'interdire (ou d'autoriser) les événements Twitch. |
| **Préconditions** | Starlight est en mode Stream. |

L'interdiction est une **option du mode Stream**, pas un mode : elle se combine avec lui (voir QO-41).

## Scénario nominal : interdire

1. Le Streamer demande d'interdire les événements Twitch.
2. Starlight cesse de traiter les événements Twitch : ceux qui arrivent ensuite ne produisent aucune réaction.
3. Starlight consigne dans le journal le début de l'interdiction (acteur) et compte les événements ignorés.
4. Les réactions déjà en cours ou en attente ne sont pas touchées *(proposé)* ; le Streamer peut les supprimer avec UC-STR-03.
5. Les ambiances et les réactions manuelles du Streamer restent possibles (UC-STR-01, UC-STR-02).

## Scénario nominal : autoriser

1. Le Streamer demande d'autoriser à nouveau les événements Twitch.
2. Starlight traite de nouveau les événements Twitch reçus à partir de ce moment.
3. Les événements ignorés pendant l'interdiction ne sont pas rejoués *(proposé : ils seraient périmés)*.
4. Starlight consigne dans le journal la fin de l'interdiction et le nombre d'événements ignorés.

## Scénarios alternatifs *(proposés, à valider)*

- **A1, mode Lounge actif** : la demande est ignorée (les événements Twitch sont déjà ignorés en mode Lounge).
- **A2, déjà dans l'état demandé** : aucun changement.
- **A3, sortie du mode Stream** : l'interdiction est levée *(proposé, voir QO-41)*, pour qu'elle ne reste pas active par surprise au stream suivant.
- **A4, échanges de points de chaîne reçus pendant l'interdiction** : leur traitement (pause des récompenses, annulation avec remboursement) dépend de l'expérience EXP-01 et de QO-42.

## Postconditions

- L'état « événements Twitch interdits » ou « autorisés » est enregistré.
- Le journal indique l'acteur, le moment, et le nombre d'événements ignorés.

## Questions liées

QO-20, QO-41, QO-42
