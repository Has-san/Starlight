# UC-SYS-02 : Passage en mode Stream

*Statut : brouillon.*

| Champ | Contenu |
|---|---|
| **Acteur principal** | Système |
| **Objectif** | Préparer les étoiles et la régie quand Starlight passe en mode Stream, avant que le live ne commence. |
| **Déclencheur** | Starlight passe du mode Lounge au mode Stream. |
| **Préconditions** | Aucune session d'édition en cours (sinon elle est traitée avant le changement de mode, UC-ADM-11). |

## Principe

- **Moment** : le passage en mode Stream a lieu typiquement à l'ouverture d'OBS. Le live n'a pas commencé : **seul le Streamer voit les étoiles**. C'est la phase de **préparation**.
- **Deux moments distincts** : le passage en mode Stream (ce cas d'usage) et le **début du live**, déclenché à la main par le Streamer (cas d'usage à rédiger, UC-STR-06), qui joue la séquence d'ouverture que voient les spectateurs. Les deux peuvent avoir une réaction différente.
- **Ambiance neutre** : à l'entrée, les secteurs du mode Stream prennent l'**ambiance neutre**, une ambiance comme les autres, **personnalisable** par l'Administrateur (UC-ADM-03) et désignée comme point d'entrée du mode Stream. Si aucune n'est désignée, c'est « Off ».
- **Réaction au passage en Stream** : une réaction **facultative** peut être associée à l'événement « passage en mode Stream » (UC-ADM-07). C'est une réaction ordinaire (UC-ADM-12), qui se joue sur la base neutre ; à sa fin, les étoiles reviennent à l'ambiance neutre.
- **Récapitulatif** : la régie du Streamer affiche le récapitulatif des autorisations et l'état du verrou de configuration, avec confirmation obligatoire (UC-STR-04, UC-ADM-09). Cette phase de préparation permet de le confirmer avant le live.
- **Étoiles en manuel** (UC-ADM-05) : non touchées.

## Scénario nominal

1. Starlight passe en mode Stream.
2. Le Système applique l'ambiance neutre aux étoiles des secteurs du mode Stream (UC-ADM-10, UC-STR-05).
3. Si une réaction est associée au passage en mode Stream, le Système la joue.
4. La régie du Streamer affiche le récapitulatif ; le Streamer le confirme (UC-STR-04).
5. Starlight consigne dans le journal : acteur « Système », motif « passage en mode Stream ».
6. Les étoiles restent sur l'ambiance neutre. Le Streamer peut choisir une ambiance (UC-STR-01) ou déclencher une réaction (UC-STR-02) sans attendre le début du live.

## Scénarios alternatifs

- **A1, aucune ambiance neutre désignée** : les étoiles s'éteignent (« Off »).
- **A2, aucune réaction associée** : l'étape 3 est ignorée.
- **A3, étoile en manuel** : non touchée, elle reste dans son effet.
- **A4, étoile injoignable** : les autres étoiles s'allument, la défaillance est consignée (QO-14).
- **A5, régie fermée** : le récapitulatif l'attend ; le journal indique « non confirmé » (UC-STR-04).
- **A6, retour en mode Lounge pendant la réaction** : la réaction est arrêtée.

## Postconditions

- Les étoiles du mode Stream sont sur l'ambiance neutre.
- Le Streamer a vu le récapitulatif, ou il l'attend.
- Le journal indique l'acteur « Système » et le motif.

## Points non tranchés

- **Phases du mode Stream** : proposé de distinguer « préparation » (avant le début du live) et « en live ». Elles décident de l'état des étoiles et du traitement des événements (QO-62).
- **Événements Twitch pendant la préparation** : proposé qu'ils soient ignorés, et non mis en file, jusqu'au début du live (QO-62).
- **Étoiles du Lounge hors des secteurs Stream** : conservent-elles leur état ou s'éteignent-elles à l'entrée en Stream ? (QO-62).
- **Types d'événements associables** : UC-ADM-07 doit permettre d'associer une réaction aux événements du Système (« passage en mode Stream », « début du live »), en plus de ceux de Twitch (QO-62).
- **Sortie du mode Stream** : état des étoiles à définir, dans un cas d'usage à part (QO-09).

## Questions liées

QO-09, QO-14, QO-36, QO-49, QO-62
