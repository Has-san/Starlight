# UC-STR-06 : Démarrer le live

*Statut : validé.*

| Champ | Contenu |
|---|---|
| **Acteur principal** | Streamer (l'Administrateur peut faire la même chose) |
| **Objectif** | Marquer le début du live : jouer la séquence d'ouverture que voient les spectateurs et ouvrir les récompenses de points de chaîne. |
| **Déclencheur** | Le Streamer demande le début du live depuis sa régie. |
| **Préconditions** | Starlight est en mode Stream (UC-SYS-02). Le live n'a pas déjà commencé, ou il a été terminé (UC-STR-07). |

## Principe

- Le début du live est **manuel** : il a lieu quand le Streamer quitte sa scène d'attente, au moment où les spectateurs commencent à voir le live.
- C'est un événement du Système, auquel l'Administrateur peut associer une réaction (UC-ADM-07). Cette réaction est la **séquence d'ouverture** ; elle peut être différente de la réaction jouée au passage en mode Stream (UC-SYS-02). Sans association, il n'y a pas de séquence d'ouverture.
- La séquence d'ouverture est une réaction ordinaire (UC-ADM-12). Les événements Twitch qui arrivent pendant qu'elle se joue **attendent sa fin** dans la file ; ils ne la coupent pas.
- Au début du live, les récompenses de points de chaîne mises en pause à l'entrée en Stream sont **remises en service**, sauf celles que le Streamer a interdites par son interrupteur (UC-STR-04).
- Un changement de scène OBS pourrait un jour déclencher le début du live (ID-15) ; ce n'est pas le cas aujourd'hui.

## Scénario nominal

1. Le Streamer demande le début du live depuis sa régie.
2. Starlight remet en service les récompenses de points de chaîne, sauf celles interdites (UC-STR-04).
3. Si une réaction est associée à l'événement « début du live », Starlight la joue.
4. Starlight consigne dans le journal : acteur, événement « début du live ».
5. Les événements arrivant pendant la séquence d'ouverture attendent sa fin, puis sont traités dans l'ordre normal de la file.
6. À la fin de la séquence, les étoiles reviennent à l'ambiance qui était courante.

## Scénarios alternatifs

- **A1, aucune réaction associée** : l'étape 3 est ignorée ; les récompenses sont tout de même remises en service.
- **A2, live déjà commencé** : la demande est ignorée.
- **A3, mode Lounge actif** : la demande est refusée (le début du live n'existe qu'en mode Stream).
- **A4, récompense impossible à remettre en service** : alerte dans la régie, consignée dans le journal ; les autres récompenses sont remises en service.
- **A5, étoile en manuel** : non touchée par la séquence d'ouverture (UC-ADM-05).
- **A6, étoile injoignable** : la séquence se joue sur les autres étoiles, la défaillance est consignée (QO-14).

## Postconditions

- Le live est marqué comme commencé.
- Les récompenses de points de chaîne sont en service, sauf celles interdites.
- Le journal indique l'acteur et l'événement.

## Précisions décidées

- **Session d'édition ouverte** : le début du live est refusé tant qu'une session d'édition est en cours, comme les prises de main (UC-ADM-05, QO-60), car la file est en pause pendant l'aperçu.
- **Récapitulatif non confirmé** : la demande invite d'abord le Streamer à confirmer le récapitulatif, puisque le live devient visible des spectateurs.
- **Fin du live** : elle est manuelle (UC-STR-07) et distincte de la sortie du mode Stream. Après une fin de live, un nouveau live peut commencer.

## Points non tranchés

- **Sortie du mode Stream** : état des étoiles à définir, dans un cas d'usage à part (QO-09).

## Questions liées

QO-09, QO-14, QO-42, QO-60, QO-63
