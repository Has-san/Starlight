# UC-STR-07 : Terminer le live

*Statut : brouillon.*

| Champ | Contenu |
|---|---|
| **Acteur principal** | Streamer (l'Administrateur peut faire la même chose) |
| **Objectif** | Marquer la fin du live : jouer une réaction de clôture facultative et fermer les récompenses de points de chaîne. |
| **Déclencheur** | Le Streamer demande la fin du live depuis sa régie, ou accepte la proposition de l'alerte de fin de live. |
| **Préconditions** | Starlight est en mode Stream. Le live a commencé (UC-STR-06) et n'est pas terminé. |

## Principe

- La fin du live est **manuelle** : Starlight ne la décide jamais seul, car une fin de live ne se distingue pas sûrement d'une coupure de connexion.
- C'est un événement du Système (« fin du live »), auquel l'Administrateur peut associer une réaction de clôture (UC-ADM-07). Sans association, il n'y a pas de réaction de clôture.
- La fin du live **n'est pas** la sortie du mode Stream : les étoiles ne changent pas de mode et restent sur leur ambiance (le retour en Lounge est un autre cas d'usage).
- Les récompenses de points de chaîne sont **remises en pause** (QO-42), pour que personne ne dépense de points une fois le live fini.
- La réaction de clôture est une réaction ordinaire (UC-ADM-12) : elle entre dans la file avec la priorité de l'association, sans toucher aux réactions déjà en file.
- Les autres événements Twitch continuent d'être traités selon les autorisations en vigueur (UC-STR-04), jusqu'à la sortie du mode Stream.

## Alerte de fin de live

- Si Twitch signale que le live est hors ligne **depuis plus longtemps qu'un délai paramétrable** (5 minutes par défaut, réglé par l'Administrateur), la régie du Streamer affiche une alerte : « le live semble terminé ».
- L'alerte **propose** de terminer le live ; elle n'agit jamais seule. Accepter la proposition suit le scénario nominal.
- L'alerte disparaît d'elle-même si Twitch signale que le live est de nouveau en ligne, ou quand le Streamer termine le live ou la refuse.
- Elle n'existe que si Starlight est connecté à Twitch (UC-ADM-08) et si le live a commencé dans Starlight.
- L'émission et le refus de l'alerte sont consignés dans le journal.

## Scénario nominal

1. Le Streamer demande la fin du live depuis sa régie.
2. Starlight met en pause les récompenses de points de chaîne.
3. Si une réaction est associée à l'événement « fin du live », Starlight l'ajoute à la file.
4. Starlight consigne dans le journal : acteur, événement « fin du live ».
5. Le live est marqué comme terminé.

## Scénarios alternatifs

- **A1, live non commencé ou déjà terminé** : la demande est ignorée.
- **A2, mode Lounge actif** : la demande est refusée.
- **A3, aucune réaction associée** : l'étape 3 est ignorée ; les récompenses sont tout de même mises en pause.
- **A4, récompense impossible à mettre en pause** : alerte dans la régie, consignée dans le journal (QO-42).
- **A5, alerte refusée** : le Streamer indique qu'il continue ; l'alerte ne revient pas pour la même coupure, mais une nouvelle coupure repart d'un nouveau délai.
- **A6, nouveau début de live** : après une fin de live, le Streamer peut démarrer un nouveau live (UC-STR-06) sans quitter le mode Stream.

## Postconditions

- Le live est marqué comme terminé.
- Les récompenses de points de chaîne sont en pause.
- Le journal indique l'acteur et l'événement.

## Points non tranchés

- **Session d'édition ouverte** : proposé que la fin du live soit refusée tant qu'une session d'édition est en cours, comme le début du live (UC-STR-06), car la file est en pause pendant l'aperçu (QO-64).
- **Délai de l'alerte** : 5 minutes par défaut, réglé par l'Administrateur ; valeur proposée (QO-64).

## Questions liées

QO-09, QO-42, QO-63, QO-64
