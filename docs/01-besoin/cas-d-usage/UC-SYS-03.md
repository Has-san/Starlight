# UC-SYS-03 : Sortie du mode Stream (retour en Lounge)

*Statut : brouillon.*

| Champ | Contenu |
|---|---|
| **Acteur principal** | Système |
| **Objectif** | Remettre les étoiles dans l'état du mode Lounge quand Starlight quitte le mode Stream. |
| **Déclencheur** | Starlight passe du mode Stream au mode Lounge, par une demande manuelle (UC-STR-08) ou par la coupure automatique après une alerte de fin de live (UC-STR-07). |
| **Préconditions** | Aucun live n'est en cours : il est terminé ou n'a jamais commencé. |

## Principe

- **État d'arrivée** : les étoiles des secteurs du mode Lounge reprennent la **dernière ambiance du Lounge**, mémorisée à l'entrée en Stream (UC-SYS-02). Si elle a été supprimée entre-temps, ou si le Lounge était sur « Off », les étoiles passent à « Off ».
- **Étoiles hors des secteurs du Lounge** : elles s'éteignent, comme à l'entrée en Stream.
- **Réaction et file** : la réaction en cours est arrêtée et la file est vidée, avec une trace dans le journal. Les événements Twitch ne sont plus traités en mode Lounge.
- **Récompenses de points de chaîne** : elles sont en pause (elles le sont depuis la fin du live, ou depuis l'entrée en Stream si le live n'a jamais commencé). Si ce n'est pas le cas, le Système les met en pause.
- **Étoiles en manuel** (UC-ADM-05) : non touchées. Le délai de libération automatique repart de zéro.
- **Économie d'énergie** (UC-SYS-01) : elle redémarre, la temporisation repart de zéro.
- Pas de réaction associée à la sortie du Stream : seul le début et la fin du live ont un événement du Système.

## Scénario nominal

1. Starlight passe en mode Lounge.
2. Le Système arrête la réaction en cours et vide la file.
3. Le Système vérifie que les récompenses de points de chaîne sont en pause, et les met en pause sinon.
4. Le Système applique aux étoiles des secteurs du mode Lounge la dernière ambiance du Lounge, et éteint les autres étoiles.
5. Starlight consigne dans le journal : acteur « Système », motif « sortie du mode Stream ».
6. Les Convives peuvent de nouveau demander une ambiance ou l'extinction (UC-CON-01, UC-CON-02).

## Scénarios alternatifs

- **A1, dernière ambiance du Lounge supprimée** : les étoiles passent à « Off ».
- **A2, Lounge sur « Off » avant le Stream** : les étoiles passent à « Off ».
- **A3, étoile en manuel** : non touchée, elle reste dans son effet.
- **A4, étoile injoignable** : les autres étoiles reprennent leur état, la défaillance est consignée (QO-14).
- **A5, récompense impossible à mettre en pause** : alerte dans la régie, consignée dans le journal (QO-42).
- **A6, sortie par coupure automatique** : même scénario, avec le motif « live non terminé » (UC-STR-07).

## Postconditions

- Starlight est en mode Lounge ; les étoiles du Lounge ont repris la dernière ambiance, les autres sont éteintes.
- La file est vide, les récompenses sont en pause.
- Le journal indique l'acteur « Système » et le motif.

## Points non tranchés

- **Réaction de clôture encore en cours** : proposé que la sortie l'arrête et vide la file, sans attendre ; si le Streamer veut la voir en entier, il quitte le Stream après (QO-66).

## Questions liées

QO-09, QO-14, QO-42, QO-49, QO-66
