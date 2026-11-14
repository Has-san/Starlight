# UC-STR-07 : Terminer le live

*Statut : validé.*

| Champ | Contenu |
|---|---|
| **Acteur principal** | Streamer (l'Administrateur peut faire la même chose) |
| **Objectif** | Marquer la fin du live : jouer une réaction de clôture facultative et fermer les récompenses de points de chaîne. |
| **Déclencheur** | Le Streamer demande la fin du live depuis sa régie, ou accepte la proposition de l'alerte de fin de live. |
| **Préconditions** | Starlight est en mode Stream. Le live a commencé (UC-STR-06) et n'est pas terminé. |

## Principe

- La fin du live est **manuelle** : une fin de live ne se distingue pas sûrement d'une coupure de connexion. Starlight n'agit seul qu'après une alerte restée sans réponse (voir « Alerte de fin de live et coupure automatique »).
- C'est un événement du Système (« fin du live »), auquel l'Administrateur peut associer une réaction de clôture (UC-ADM-07). Sans association, il n'y a pas de réaction de clôture.
- La fin du live **n'est pas** la sortie du mode Stream : les étoiles ne changent pas de mode et restent sur leur ambiance (le retour en Lounge est un autre cas d'usage).
- Les récompenses de points de chaîne sont **remises en pause** (QO-42), pour que personne ne dépense de points une fois le live fini.
- La réaction de clôture est une réaction ordinaire (UC-ADM-12) : elle entre dans la file avec la priorité de l'association, sans toucher aux réactions déjà en file.
- Les autres événements Twitch continuent d'être traités selon les autorisations en vigueur (UC-STR-04), jusqu'à la sortie du mode Stream.

## Alerte de fin de live et coupure automatique

- Si Twitch signale que le live est hors ligne **depuis plus longtemps qu'un premier délai** (**5 minutes** par défaut), la régie du Streamer affiche une alerte : « le live semble terminé ».
- L'alerte **propose** de terminer le live. Accepter la proposition suit le scénario nominal.
- **Coupure automatique** : si l'alerte reste **sans réponse** jusqu'à un second délai (**20 minutes** par défaut après le signal de Twitch, soit **15 minutes après l'alerte**), Starlight termine le live et **quitte le mode Stream** : retour en Lounge (UC-SYS-03). Les récompenses de points de chaîne sont mises en pause, la file est vidée et il n'y a pas de réaction de clôture. C'est la seule exception au refus de quitter le Stream pendant un live (UC-STR-08).
- Les deux délais sont **paramétrables** par l'Administrateur ; le second doit être plus long que le premier.
- Le décompte s'arrête si Twitch signale que le live est de nouveau en ligne, ou si le Streamer répond à l'alerte : il termine le live (scénario nominal) ou la refuse (A5).
- Elle n'existe que si Starlight est connecté à Twitch (UC-ADM-08) et si le live a commencé dans Starlight.
- L'émission de l'alerte, son refus et la coupure automatique sont consignés dans le journal (la coupure : acteur « Système », motif « live non terminé »).

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
- **A5, alerte refusée** : le Streamer indique qu'il continue ; la coupure automatique est annulée, l'alerte ne revient pas pour la même coupure, et une nouvelle coupure repart d'un nouveau délai.
- **A8, coupure automatique** : l'alerte reste sans réponse jusqu'au second délai ; Starlight termine le live, met les récompenses en pause, vide la file et revient en Lounge. Le Streamer retrouve la régie dans cet état et peut repasser en Stream (UC-STR-08).
- **A6, session d'édition ouverte** : la fin du live est acceptée ; la réaction de clôture attend la fin de la session.
- **A7, nouveau début de live** : après une fin de live, le Streamer peut démarrer un nouveau live (UC-STR-06) sans quitter le mode Stream.

## Postconditions

- Le live est marqué comme terminé.
- Les récompenses de points de chaîne sont en pause.
- Le journal indique l'acteur et l'événement.

## Précisions décidées

- **Session d'édition ouverte** : la fin du live reste possible, contrairement au début du live (UC-STR-06), car elle protège les spectateurs (récompenses remises en pause tout de suite). La réaction de clôture entre dans la file, qui est en pause pendant l'aperçu : elle se joue à la fin de la session d'édition (UC-ADM-11).
- **Nouveau live** : après une fin de live, un nouveau live peut commencer sans quitter le mode Stream.
- **Délais** : alerte à 5 minutes, coupure automatique à 20 minutes après le signal de Twitch (15 minutes après l'alerte), réglés par l'Administrateur.

## Questions liées

QO-09, QO-42, QO-63, QO-64
