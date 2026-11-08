# UC-STR-05 : Choisir les secteurs du mode Stream

*Statut : validé.*

| Champ | Contenu |
|---|---|
| **Acteur principal** | Streamer (l'Administrateur définit aussi les secteurs de chaque mode avec UC-ADM-10) |
| **Objectif** | Décider quels secteurs de lumières sont utilisés pendant le mode Stream. |
| **Déclencheur** | Le Streamer modifie la liste des secteurs du mode Stream depuis sa régie. |
| **Préconditions** | Starlight est en mode Stream. Au moins un secteur existe. |

## Scénario nominal

1. Le Streamer ouvre la liste des secteurs. Tous les secteurs y figurent (aucun filtre pour l'instant, voir QO-58) ; ceux qui sont utilisés par le mode Stream sont marqués.
2. Il ajoute ou retire un ou plusieurs secteurs.
3. Le changement s'applique **tout de suite**, sans aperçu ni validation et sans mettre la file en pause (UC-ADM-11 n'est pas utilisé).
4. Starlight consigne le changement dans le journal : acteur, secteurs avant et après.
5. Starlight recalcule les étoiles envoyées au pilote (désignées par l'ambiance ET dans un secteur du mode) :
   - les étoiles qui sortent du mode sont **éteintes tout de suite**, y compris si une réaction est en cours (seules ces étoiles sont touchées, la réaction continue sur les autres) ;
   - les étoiles qui entrent dans le mode affichent l'ambiance courante.

## Scénarios alternatifs

- **A1, mode Lounge actif** : la modification est refusée. Le Streamer ne change les secteurs de Stream qu'en mode Stream ; l'Administrateur peut le faire à tout moment avec UC-ADM-10.
- **A2, aucun changement** : rien n'est consigné.
- **A3, aucun secteur choisi** : autorisé. Rien ne s'allume, l'alerte « mode sans secteur » s'affiche et le journal l'indique.
- **A4, étoile dans plusieurs secteurs** : elle reste utilisée tant qu'elle appartient à au moins un secteur du mode.
- **A5, secteur supprimé par l'Administrateur** : il est retiré du mode (UC-ADM-02, A4) ; la suppression est consignée.
- **A6, deux changements successifs** : le dernier s'applique, l'acteur est consigné à chaque fois.
- **A7, verrou de configuration** : le verrou de UC-ADM-09 ne s'applique pas au Streamer pour ce choix.
- **A8, étoile indisponible** : elle reste dans le mode ; à son retour elle reprend l'ambiance courante (QO-55).

## Postconditions

- Le mode Stream utilise exactement les secteurs choisis.
- Le journal indique l'acteur et l'état avant et après.
- Les étoiles hors du mode sont éteintes ; les autres affichent l'ambiance courante ou la réaction en cours.

## Questions liées

QO-48, QO-53, QO-55, QO-58
