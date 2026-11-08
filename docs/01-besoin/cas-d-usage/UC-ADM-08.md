# UC-ADM-08 : Connecter Starlight à Twitch

*Statut : validé.*

| Champ | Contenu |
|---|---|
| **Acteur principal** | Administrateur |
| **Acteurs secondaires** | Streamer (propriétaire de la chaîne, qui autorise), Twitch |
| **Objectif** | Permettre à Starlight de recevoir les événements de la chaîne Twitch et de connaître ses récompenses de points de chaîne. |
| **Déclencheur** | L'Administrateur demande la connexion à Twitch. |
| **Préconditions** | Twitch est joignable. Le propriétaire de la chaîne peut se connecter à son compte Twitch. |

## Droits demandés

- **Lecture (obligatoire)** : recevoir les événements de la chaîne et lister ses récompenses.
- **Gestion des récompenses (optionnelle)** : mettre en pause ou annuler un échange. Elle n'est pas demandée tant que QO-42 reste ouverte.

Le jeton obtenu est conservé par Starlight. Il n'est jamais affiché ni écrit dans le journal.

## Scénario nominal

1. L'Administrateur demande la connexion à Twitch.
2. Starlight envoie vers la page d'autorisation de Twitch, qui présente les droits demandés.
3. Le propriétaire de la chaîne se connecte à son compte Twitch et autorise Starlight.
4. Twitch renvoie l'autorisation à Starlight, qui conserve le jeton.
5. Starlight commence à recevoir les événements de la chaîne et récupère la liste de ses récompenses (elles deviennent disponibles pour UC-ADM-07).
6. Starlight consigne la connexion dans le journal (acteur, chaîne, date, sans jeton) et indique à l'Administrateur qu'il est connecté.

## Règles

- Si l'Administrateur et le Streamer sont la même personne, les étapes 1 et 3 sont faites par elle.
- L'Administrateur peut se connecter et se déconnecter en mode Lounge comme en mode Stream. Les événements ne produisent une réaction qu'en mode Stream (voir UC-TWI-01).
- Une interdiction des événements Twitch (UC-STR-04) ne déconnecte pas Starlight : la connexion est maintenue, les événements sont ignorés.
- Starlight est connecté à **une seule chaîne** à la fois.

## Connexion en fonctionnement

- Si la connexion se coupe, Starlight se reconnecte automatiquement. Chaque coupure et chaque reconnexion sont consignées dans le journal.
- Les événements survenus pendant une coupure ne sont pas rejoués : ils seraient périmés (même raisonnement que QO-41).
- Si la reconnexion échoue, ou si l'autorisation est expirée ou révoquée sans pouvoir être renouvelée, Starlight passe à l'état « déconnecté », le consigne et **prévient le Streamer dans son interface de régie** (voir QO-45).
- Dans tous ces cas, les ambiances et les réactions manuelles continuent de fonctionner.

## Scénarios alternatifs

- **A1, autorisation refusée** : aucune connexion n'est établie ; le refus est consigné et l'Administrateur en est informé.
- **A2, Twitch injoignable** : la connexion échoue ; l'échec est consigné et l'Administrateur peut réessayer.
- **A3, déjà connecté** : Starlight demande confirmation avant de remplacer la connexion existante.
- **A4, déconnexion** : l'Administrateur demande la déconnexion. Starlight supprime le jeton, cesse de recevoir les événements Twitch et consigne l'action. Les associations de UC-ADM-07 sont conservées.
- **A5, autorisation révoquée côté Twitch** : détectée par Starlight comme dans « Connexion en fonctionnement » ; une nouvelle connexion (scénario nominal) est nécessaire.

## Postconditions

- Connecté : Starlight reçoit les événements et connaît les récompenses de la chaîne.
- Sinon : aucun jeton n'est conservé, les événements Twitch sont absents, et le Streamer en est informé s'il s'agit d'une perte en cours de fonctionnement.
- Dans tous les cas, le journal décrit l'événement sans aucun secret.

## À confirmer par l'expérience

Portées exactes demandées à Twitch, durée de vie des jetons et conditions de leur renouvellement, délais de détection d'une coupure : voir EXP-01 et la documentation officielle de Twitch.

## Questions liées

QO-11, QO-14, QO-15, QO-41, QO-42, QO-45
