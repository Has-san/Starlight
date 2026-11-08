# EXP-01 : points de chaîne Twitch (expérience technique)

*Statut : à réaliser. Cette expérience se mène en parallèle de l'expression de besoin ; elle ne bloque aucun cas d'usage.*

Mode d'emploi du script : [MODE-EMPLOI.md](MODE-EMPLOI.md).

## Pourquoi cette expérience

Plusieurs décisions du besoin dépendent de ce que Twitch permet réellement (UC-STR-03, UC-STR-04, QO-41, QO-42). Les informations actuelles viennent de la documentation de l'API relue via des copies tierces : elles doivent être confirmées par l'expérience.

**Objectif** : savoir, par des essais réels, ce que Starlight peut lire, mettre en pause, annuler et rembourser sur les récompenses de points de chaîne.

**Hors périmètre** : aucun code Starlight, aucune étoile, aucun abonnement/don/raid (ce sera EXP-02 si besoin). On teste uniquement l'échange avec Twitch.

## Hypothèses à confirmer

| ID | Hypothèse | D'où elle vient |
|---|---|---|
| H1 | Starlight peut recevoir les échanges de **toutes** les récompenses de la chaîne, y compris celles créées à la main par le Streamer. | L'abonnement aux échanges accepte un filtre facultatif par récompense, donc sans filtre il couvre toutes les récompenses. |
| H2 | Starlight ne peut modifier (pause, désactivation) que les récompenses **créées par sa propre application**. | Documentation de la mise à jour d'une récompense. |
| H3 | Annuler un échange rembourse les points du spectateur. | Documentation de la mise à jour du statut d'un échange. |
| H4 | Une récompense configurée pour sauter la file de demandes ne peut plus être annulée. | Hypothèse personnelle, **aucune source vérifiée**. |
| H5 | Les récompenses personnalisées exigent une chaîne affiliée ou partenaire. | Mémoire, **non vérifié**. Non bloquant ici : la chaîne de test est affiliée. |

## Prérequis

- Une chaîne Twitch de test (statut affilié confirmé).
- Un **second compte** jouant le spectateur, avec des points de chaîne.
- Une application enregistrée sur la console développeur de Twitch (identifiant client, secret).
- Un jeton utilisateur du Streamer avec l'autorisation de gérer les échanges (`channel:manage:redemptions`). Selon la source consultée, la lecture seule des échanges est possible avec `channel:read:redemptions` ; à vérifier.
- Un outil de test : un petit script Python jetable, ou l'outil en ligne de commande de Twitch (à vérifier) pour simuler des événements.

## Règles de sécurité

- Le secret de l'application et les jetons ne sont **jamais** écrits dans un document, un message de commit ou une conversation. Les passer par des variables d'environnement.
- Le code de l'expérience reste dans un dossier à part (`experiments/EXP-01/`), pas dans `host/`, pour qu'un prototype jetable ne devienne pas le produit.
- Utiliser des récompenses à coût minimal.

## Essais

Pour chaque essai : noter la date, le résultat observé et une conclusion en une phrase.

| ID | Objectif | Étapes | Résultat attendu | Résultat observé | Questions touchées |
|---|---|---|---|---|---|
| E0 | Obtenir un jeton | Créer l'application ; obtenir le jeton avec les autorisations (statut affilié déjà confirmé) | Jeton valide | | QO-42 |
| E1 | Créer une récompense par l'API | Créer une récompense « Starlight test » | Elle apparaît dans la chaîne | | QO-42 |
| E2 | Recevoir un échange d'une récompense créée par Starlight | S'abonner aux échanges ; échanger depuis le compte spectateur | Événement reçu avec identifiant, récompense, utilisateur, statut | | QO-23, QO-42 |
| E3 | Recevoir un échange d'une récompense créée à la main (H1) | Créer une récompense dans le tableau de bord ; l'échanger | Événement reçu aussi | | QO-42 |
| E4 | Mettre en pause une récompense de Starlight (H2) | Passer la récompense en pause, puis la désactiver ; essayer d'échanger depuis le compte spectateur | Échange impossible | | QO-41, QO-42 |
| E5 | Modifier une récompense créée à la main (H2) | Tenter la pause sur la récompense de E3 | Échec ; noter le message d'erreur | | QO-41, QO-42 |
| E6 | Annuler un échange et rembourser (H3) | Échange avec file de demandes active ; passer le statut à « annulé » | Points rendus au spectateur | | QO-37, QO-42 |
| E7 | Annuler un échange sur une récompense qui saute la file (H4) | Même essai avec l'option « sauter la file » | À observer | | QO-37, QO-42 |
| E8 | Mesurer le délai | 10 échanges ; mesurer le temps entre l'échange et la réception | Délais minimal, moyen, maximal | | QO-22, QO-25 |
| E9 | Doublons | Couper et rétablir la connexion pendant des échanges ; chercher des événements reçus deux fois | Identifiant unique permettant de dédoublonner | | QO-23 |
| E10 | Résilience | Laisser expirer le jeton ; couper le réseau ; observer la reconnexion | Comportement documenté ; durée de vie du jeton connue | | QO-19, sécurité |
| E11 | Échange pendant une pause | Échanger au moment exact de la mise en pause | Échange accepté ou refusé ; si accepté, il est annulable | | QO-41, QO-42 |

## À la fin

Reporter les conclusions dans le registre des questions ouvertes (QO-41, QO-42, QO-23, QO-22, QO-25, QO-19) et créer, si besoin, un cas d'usage de l'Administrateur « connecter Starlight à Twitch ».

## Sources consultées

- Mise à jour d'une récompense : https://docs.rs/crate/twitch_api/latest/source/src/helix/endpoints/points/update_custom_reward.rs
- Mise à jour du statut d'un échange : https://docs.rs/twitch_api2/latest/src/twitch_api2/helix/endpoints/points/update_redemption_status.rs.html
- Événement d'échange (EventSub) : https://docs.rs/crate/twitch_api/latest/source/src/eventsub/channel/channel_points_custom_reward_redemption/add.rs

Ces pages sont des copies tierces de la documentation de l'API de Twitch ; la référence reste la documentation officielle.
