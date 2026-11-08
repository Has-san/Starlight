# UC-TWI-01 : Émettre un événement entraînant une réaction

*Statut : validé.*

| Champ | Contenu |
|---|---|
| **Acteur principal** | Twitch (acteur externe) |
| **Objectif** | Faire jouer par Starlight la réaction prédéfinie associée à un événement. |
| **Déclencheur** | Twitch émet un événement (abonnement, don, raid…). |
| **Préconditions** | Starlight est en mode Stream. Les événements Twitch ne sont pas interdits par le Streamer (voir UC-STR-04). Starlight est connecté à Twitch. L'Administrateur a associé une réaction au type de l'événement (voir UC-ADM-07). |

## Scénario nominal

1. Twitch émet un événement.
2. Starlight reçoit l'événement et identifie son type.
3. Starlight retrouve la réaction que l'Administrateur a associée à ce type d'événement.
4. Si aucune réaction n'est en cours, Starlight la joue immédiatement ; sinon, elle est placée dans la file d'attente selon sa priorité (voir QO-01). Une réaction prioritaire passe avant les autres réactions en attente, sans interrompre la réaction en cours.
5. Le pilote, pour chaque étoile concernée, joue la séquence adaptée à ses capacités.
6. À la fin de la réaction, s'il n'y en a pas d'autre en attente, Starlight reprend l'ambiance précédente.

## Scénarios alternatifs

- **A1, mode Lounge actif** : l'événement est ignoré.
- **A2, aucune réaction associée** : l'événement est ignoré et consigné dans le journal.
- **A3, rafale d'événements** : aucun événement n'est perdu. La réaction peut varier avec le nombre d'occurrences du même événement (par exemple plus rapide, ou autant de clignotements que d'événements). Voir QO-22.
- **A4, événement reçu en double** : chaque événement est identifiable (horodatage ou identifiant) ; un doublon est reconnu et ignoré. Voir QO-23.
- **A5, Administrateur a pris la main** : comportement à définir (voir QO-12).
- **A6, connexion à Twitch perdue** : plus aucun événement n'arrive ; la perte est consignée dans le journal et l'ambiance courante est conservée.
- **A7, événements Twitch interdits** : l'événement est ignoré et compté dans le journal (voir UC-STR-04).

## Postconditions

- La réaction a été jouée (ou ignorée selon A1, A2, A4).
- L'ambiance courante est la même qu'avant l'événement.

## Questions liées

QO-01, QO-02, QO-12, QO-22, QO-25, QO-27
