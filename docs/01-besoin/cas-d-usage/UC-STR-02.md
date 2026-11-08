# UC-STR-02 : Déclencher manuellement une réaction

*Statut : validé.*

| Champ | Contenu |
|---|---|
| **Acteur principal** | Streamer (l'Administrateur peut aussi déclencher une réaction de la même façon, avec les mêmes options) |
| **Objectif** | Faire jouer une réaction à la demande, en direct ou pour la tester. |
| **Déclencheur** | Le Streamer sélectionne une réaction via un actionneur (voir QO-11). |
| **Préconditions** | Starlight est en mode Stream. |

## Scénario nominal

1. Le Streamer consulte la liste des réactions disponibles (toutes les réactions y figurent ; l'Administrateur y a accès aussi, voir QO-31) et en sélectionne une.
2. Le Streamer indique si sa demande est prioritaire ou non (par défaut : non prioritaire, voir QO-32).
3. Starlight reçoit la demande, la consigne dans le journal comme **réaction manuelle** (distincte d'une réaction issue d'un événement), puis la place dans la file :
   - **prioritaire** : elle passe devant toutes les autres réactions en attente, sans interrompre la réaction en cours (voir QO-24) ;
   - **non prioritaire** : elle est ajoutée à la file avec le même jeu de priorité qu'un événement externe.
4. La suite est identique à UC-TWI-01 (étapes 5 et 6) : lecture par le pilote pour les étoiles concernées, puis reprise de l'ambiance précédente s'il n'y a pas d'autre réaction en attente.

## Différence avec UC-TWI-01

La réaction est choisie directement par le Streamer : aucune association « événement → réaction » n'intervient (UC-ADM-07 n'est pas utilisé). Le Streamer peut en plus choisir la priorité de sa demande.

## Scénarios alternatifs

- **A1, mode Lounge actif** : la demande est ignorée.
- **A2, demandes répétées** : traitées comme une rafale (voir QO-22) ; aucune demande n'est perdue.
- **A3, réaction en cours** : elle n'est pas interrompue ; la demande passe après elle (devant les autres si elle est prioritaire).
- **A4, plusieurs demandes prioritaires** : traitées dans leur ordre d'arrivée (voir QO-32).

## Postconditions

- La réaction a été jouée (ou ignorée selon A1).
- Le journal indique que la réaction était manuelle.
- L'ambiance courante est la même qu'avant la demande.

## Questions liées

QO-11, QO-22, QO-25, QO-31, QO-32
