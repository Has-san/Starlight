# UC-STR-08 : Changer de mode (Lounge ↔ Stream)

*Statut : validé.*

| Champ | Contenu |
|---|---|
| **Acteur principal** | Streamer (l'Administrateur peut faire la même chose) |
| **Objectif** | Faire passer Starlight du mode Lounge au mode Stream, ou l'inverse. |
| **Déclencheur** | Le Streamer demande le changement de mode depuis sa régie. |
| **Préconditions** | Aucune, hors cas refusés ci-dessous. |

## Principe

- Le changement de mode est **toujours manuel**. Il n'est pas déclenché par l'ouverture d'OBS, qui peut servir à autre chose que streamer.
- **Le Convive ne peut pas changer de mode.** Seuls le Streamer et l'Administrateur le peuvent.
- Les conséquences du changement sont décrites ailleurs : en entrée, UC-SYS-02 (ambiance neutre, réaction facultative, récapitulatif, pause des récompenses) ; en sortie, UC-SYS-03 (à rédiger : retour à la dernière ambiance du Lounge).
- **Quitter le mode Stream est refusé tant qu'un live est en cours** (commencé et non terminé). Le Streamer doit d'abord terminer le live (UC-STR-07) ; l'alerte de fin de live l'y aide. Seule exception : la coupure automatique après une alerte de fin de live restée sans réponse (UC-STR-07).
- Un changement de mode est une **action en direct** : le verrou de configuration (UC-ADM-09) ne l'empêche pas.
- Au changement de mode, le délai de libération automatique des étoiles en manuel repart de zéro (UC-ADM-05) et l'économie d'énergie est réinitialisée (UC-SYS-01).

## Scénario nominal

1. Le Streamer demande le changement de mode depuis sa régie.
2. Starlight vérifie qu'il n'y a pas de session d'édition en cours (voir « Points non tranchés ») et, pour une sortie du Stream, qu'aucun live n'est en cours.
3. Starlight change de mode.
4. Le Système joue les conséquences de l'entrée (UC-SYS-02) ou de la sortie (UC-SYS-03).
5. Starlight consigne dans le journal : acteur, ancien mode, nouveau mode.

## Scénarios alternatifs

- **A1, demande par un Convive** : refusée.
- **A2, mode déjà actif** : aucun changement.
- **A3, sortie du Stream avec un live en cours** : refusée, avec un message qui indique de terminer le live d'abord (UC-STR-07).
- **A4, session d'édition ouverte** : le Streamer doit d'abord valider ou annuler la session, comme pour le verrou de configuration (UC-ADM-09).
- **A5, Twitch non connecté à l'entrée en Stream** : l'entrée est possible ; le récapitulatif signale l'absence de connexion par une alerte.
- **A6, étoile en manuel** : non touchée par les conséquences du changement (UC-ADM-05).

## Postconditions

- Starlight est dans le nouveau mode, ou dans le mode d'origine si la demande est refusée.
- Le journal indique l'acteur et les deux modes.

## Questions liées

QO-09, QO-49, QO-65
