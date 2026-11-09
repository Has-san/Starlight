# UC-STR-03 : Arrêter les réactions (vider la file, arrêter la réaction en cours, bouton OFF)

*Statut : validé.*

| Champ | Contenu |
|---|---|
| **Acteur principal** | Streamer (l'Administrateur peut faire exactement les mêmes actions ; si un rôle devait en avoir davantage, ce serait l'Administrateur) |
| **Objectif** | Reprendre la main quand les réactions s'accumulent ou ne sont plus voulues. |
| **Déclencheur** | Le Streamer demande l'une des trois actions : vider la file, arrêter la réaction en cours, ou utiliser le bouton OFF. |
| **Préconditions** | Starlight est en mode Stream. |

Schéma : [UC-STR-03.drawio.svg](UC-STR-03.drawio.svg).

## Les trois demandes

| Demande | Effet |
|---|---|
| **Vider la file** | Supprime toutes les réactions en attente (pas une à une). La réaction en cours n'est pas touchée. |
| **Arrêter la réaction en cours** | Arrête immédiatement la réaction en cours. La file n'est pas touchée. |
| **Bouton OFF** | Arrête la réaction en cours, vide la file, puis active l'ambiance « Off ». |

## Voir la file

Le Streamer (dans sa régie) et l'Administrateur voient le contenu de la file d'attente : pour chaque réaction en attente, son nom, son origine (événement Twitch ou demande manuelle) et son rang. Cette vue précède toute suppression.

## Scénario nominal : vider la file

1. Le Streamer consulte la file puis demande de la vider.
2. Starlight supprime toutes les réactions en attente.
3. Starlight consigne l'action dans le journal : acteur (Streamer ou Administrateur), nombre de réactions supprimées, origine de chacune (événement Twitch ou demande manuelle).
4. La réaction en cours se poursuit ; à sa fin, Starlight affiche l'ambiance courante.

## Scénario nominal : arrêter la réaction en cours

1. Le Streamer demande d'arrêter la réaction en cours.
2. Starlight l'arrête immédiatement et consigne l'action dans le journal (acteur, réaction arrêtée).
3. Si la file n'est pas vide, la réaction suivante est jouée ; sinon, Starlight affiche l'ambiance courante.

## Scénario nominal : bouton OFF

1. Le Streamer utilise le bouton OFF.
2. Starlight arrête la réaction en cours et vide la file.
3. Starlight active l'ambiance « Off », qui devient l'ambiance courante et s'affiche tout de suite (plus aucune réaction en cours).
4. Starlight consigne l'action dans le journal : acteur, réaction arrêtée, réactions supprimées.

En mode Lounge, le même bouton se réduit à UC-CON-02 (il n'y a rien à arrêter).

## Scénarios alternatifs

- **A1, mode Lounge actif** : pour une demande d'arrêt ou de vidage, rien à faire (aucune réaction en mode Lounge) ; le bouton OFF suit UC-CON-02.
- **A2, rien en cours ni en attente** : aucun changement (pour OFF : l'ambiance « Off » est activée).
- **A3, nouveaux événements après un vidage ou un OFF** : ils sont traités normalement. Pour un silence complet, le Streamer interdit aussi les types d'événements (UC-STR-04).
- **A4, suppression volontaire** : les réactions supprimées ne sont pas jouées plus tard. Cette perte est voulue par le Streamer et reste visible dans le journal.

## Postconditions

- Après un vidage, la file est vide ; après un arrêt, la réaction en cours n'est plus jouée ; après OFF, l'ambiance courante est « Off ».
- Le journal indique l'acteur et ce qui a été arrêté ou supprimé : toutes les actions de ce cas d'usage sont tracées.

## Questions liées

QO-12, QO-37, QO-39, QO-42
