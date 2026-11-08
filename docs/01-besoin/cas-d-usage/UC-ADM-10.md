# UC-ADM-10 : Définir les secteurs d'un mode

*Statut : brouillon.*

| Champ | Contenu |
|---|---|
| **Acteur principal** | Administrateur (le Streamer choisit les secteurs du mode Stream avec UC-STR-05) |
| **Objectif** | Décider quels secteurs de lumières sont utilisés par chaque mode (Lounge, Stream). |
| **Déclencheur** | L'Administrateur ouvre la configuration d'un mode et modifie ses secteurs. |
| **Préconditions** | Au moins un secteur existe. En mode Stream, la configuration n'est pas verrouillée (voir UC-ADM-09). |

## Principe

- Un mode a des secteurs ; un secteur ne connaît pas les modes (voir UC-ADM-02).
- Un secteur peut être utilisé par plusieurs modes. Pour qu'une étoile seule entre dans un mode, on crée un secteur d'une étoile (QO-58).
- Pour l'instant, toutes les étoiles peuvent servir en Lounge comme en Stream.

## Scénario nominal

1. L'Administrateur choisit un mode (Lounge ou Stream).
2. Starlight affiche tous les secteurs ; ceux que le mode utilise sont marqués.
3. L'Administrateur ajoute ou retire des secteurs. Une session d'édition s'ouvre (UC-ADM-11) : avec l'aperçu activé, le résultat s'affiche sur les étoiles et la file est en pause.
4. L'Administrateur valide. Starlight enregistre la configuration, l'applique, et consigne dans le journal : acteur, mode, secteurs avant et après.
5. Si le mode modifié est le mode actif, Starlight recalcule les étoiles envoyées au pilote (désignées par l'ambiance ET dans un secteur du mode) :
   - les étoiles qui sortent du mode sont éteintes tout de suite, y compris pendant une réaction en cours (seules ces étoiles sont touchées) ;
   - les étoiles qui entrent dans le mode affichent l'ambiance courante.

## Pendant un live

L'Administrateur peut modifier les secteurs du mode Stream pendant un live. Le Streamer en est prévenu dans sa régie (qui a changé quoi). Si le Streamer a une session d'édition ouverte, l'Administrateur reçoit « une édition est déjà en cours » (UC-ADM-11).

## Scénarios alternatifs

- **A1, annulation** : rien n'est enregistré, l'affichage revient à l'ambiance courante et la file reprend (UC-ADM-11).
- **A2, aucun secteur choisi pour un mode** : autorisé. Rien ne s'allume dans ce mode, l'alerte « mode sans secteur » s'affiche et le journal l'indique.
- **A3, étoile dans plusieurs secteurs** : elle reste utilisée tant qu'elle appartient à au moins un secteur du mode.
- **A4, configuration verrouillée en Stream** : la modification est refusée (UC-ADM-09).
- **A5, secteur supprimé** : il est retiré des modes qui l'utilisent (UC-ADM-02, A4).
- **A6, étoile dans aucun secteur d'un mode** : alerte non bloquante « étoile dans aucun secteur » (QO-48). Aucun mode ne l'allume ; seuls le test manuel et l'ambiance « Off » l'atteignent.
- **A7, étoile indisponible** : elle reste dans le mode ; à son retour elle reprend l'ambiance courante (QO-55).
- **A8, ambiance « Off »** : elle éteint toutes les étoiles quels que soient les secteurs du mode.

## Postconditions

- Chaque mode utilise exactement les secteurs choisis.
- Le journal indique l'acteur et l'état avant et après.

## Questions liées

QO-48, QO-53, QO-54, QO-55, QO-58
