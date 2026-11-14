# UC-SYS-02 : Passage en mode Stream

*Statut : brouillon.*

| Champ | Contenu |
|---|---|
| **Acteur principal** | Système |
| **Objectif** | Préparer les étoiles et la régie quand Starlight passe en mode Stream, et lancer le traitement des événements Twitch. |
| **Déclencheur** | Starlight passe du mode Lounge au mode Stream. |
| **Préconditions** | Aucune session d'édition en cours (sinon elle est traitée avant le changement de mode, UC-ADM-11). |

## Principe

- **Moment** : le passage en mode Stream a lieu typiquement à l'ouverture d'OBS. Le live n'a pas forcément commencé : **seul le Streamer voit les étoiles**.
- **Deux moments distincts** : le passage en mode Stream (ce cas d'usage) et le **début du live**, déclenché à la main par le Streamer (cas d'usage à rédiger, UC-STR-06), qui joue la séquence d'ouverture que voient les spectateurs. Les deux peuvent avoir une réaction différente. Le début du live est un événement du Système ; il lève aussi la mise en pause des récompenses de points de chaîne.
- **Événements Twitch** : ils sont traités **dès l'activation du mode Stream**, selon les autorisations en vigueur (UC-STR-04), sans attendre le début du live. **Seule exception** : les récompenses de points de chaîne sont mises en pause jusqu'au début du live, pour que personne ne dépense de points avant que le live ne soit visible. Abonnements, bits, raids et follows ne se contrôlent pas en amont (UC-STR-04) : ils sont traités comme d'habitude.
- **Étoiles hors des secteurs du mode Stream** : elles **s'éteignent** à l'entrée.
- **Ambiance neutre** : à l'entrée, les secteurs du mode Stream prennent l'**ambiance neutre**, une ambiance comme les autres, **personnalisable** par l'Administrateur (UC-ADM-03) et désignée comme point d'entrée du mode Stream. Si aucune n'est désignée, c'est « Off ».
- **Réaction au passage en Stream** : une réaction **facultative** peut être associée à l'événement « passage en mode Stream » (UC-ADM-07). C'est une réaction ordinaire (UC-ADM-12), qui se joue sur la base neutre ; à sa fin, les étoiles reviennent à l'ambiance neutre.
- **Récapitulatif** : la régie du Streamer affiche le récapitulatif des autorisations et l'état du verrou de configuration, avec confirmation obligatoire (UC-STR-04, UC-ADM-09). Le récapitulatif s'affiche avant tout événement traité, ce qui permet de le confirmer avant le live.
- **Étoiles en manuel** (UC-ADM-05) : non touchées.

## Scénario nominal

1. Starlight passe en mode Stream.
2. Le Système applique l'ambiance neutre aux étoiles des secteurs du mode Stream (UC-ADM-10, UC-STR-05) et éteint les autres étoiles.
3. Le Système met en pause les récompenses de points de chaîne (QO-42), jusqu'au début du live.
4. Si une réaction est associée au passage en mode Stream, le Système la joue.
5. La régie du Streamer affiche le récapitulatif ; le Streamer le confirme (UC-STR-04).
6. Starlight consigne dans le journal : acteur « Système », motif « passage en mode Stream ».
7. Les événements Twitch (hors points de chaîne) sont traités à partir de cet instant.
8. Les étoiles restent sur l'ambiance neutre. Le Streamer peut choisir une ambiance (UC-STR-01) ou déclencher une réaction (UC-STR-02) sans attendre le début du live.

## Scénarios alternatifs

- **A1, aucune ambiance neutre désignée** : les étoiles s'éteignent (« Off »).
- **A2, aucune réaction associée** : l'étape 3 est ignorée.
- **A3, étoile en manuel** : non touchée, elle reste dans son effet.
- **A4, étoile injoignable** : les autres étoiles s'allument, la défaillance est consignée (QO-14).
- **A5, régie fermée** : le récapitulatif l'attend ; le journal indique « non confirmé » (UC-STR-04).
- **A6, retour en mode Lounge pendant la réaction** : la réaction est arrêtée.
- **A7, récompense impossible à mettre en pause** : le récapitulatif l'indique par une alerte ; les échanges reçus avant le début du live sont ignorés et consignés (traitement exact : QO-42).

## Postconditions

- Les étoiles du mode Stream sont sur l'ambiance neutre.
- Les récompenses de points de chaîne sont en pause jusqu'au début du live.
- Le Streamer a vu le récapitulatif, ou il l'attend.
- Le journal indique l'acteur « Système » et le motif.

## Points non tranchés

- **Test avant le live** : avant le début du live, un modérateur ne peut pas échanger de récompense pour tester ; le test passe par le déclenchement manuel (UC-STR-02). Une dérogation par liste de modérateurs est notée en idée (ID-16).
- **Sortie du mode Stream** : état des étoiles à définir, dans un cas d'usage à part (QO-09).

## Questions liées

QO-09, QO-14, QO-36, QO-49, QO-62
