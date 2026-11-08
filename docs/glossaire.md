# Glossaire Starlight

Ce document fixe le vocabulaire du projet. Tout autre document (besoin, spécifications, code, commentaires) doit l'employer tel quel.

La documentation est en français, le code en anglais (QO-21) : la colonne « Terme anglais » donne le nom à employer dans le code.

## Définitions

| Terme | Terme anglais (code) | Définition |
|---|---|---|
| **Starlight** | `Starlight` | Système complet des étoiles pilotables. |
| **Étoile** | `star` | Source de lumière individuelle et pilotable du système, identifiée de façon unique. Un ruban de LED est une étoile. Les capacités peuvent différer d'une étoile à l'autre : seul le pilote les connaît. L'étoile est annoncée par le pilote, avec un identifiant stable ; l'Administrateur ne la crée ni ne la supprime. |
| **Pilote** | `driver` | Élément qui commande les étoiles : il connaît leurs capacités et décide comment jouer sur chacune une séquence ou une ambiance. Il ne connaît pas les secteurs : Starlight ne lui transmet que les étoiles concernées. |
| **Secteur** | `sector` | Groupe prédéfini d'étoiles. Sert à l'Administrateur et au Streamer à désigner plusieurs étoiles d'un coup. Une étoile peut appartenir à plusieurs secteurs ; un secteur ne contient pas d'autre secteur. |
| **Mode** | `mode` | Manière de fonctionner de Starlight : Lounge ou Stream. Chaque mode a ses **secteurs** : ceux qu'il utilise. Une étoile seule entre dans un mode par un secteur d'une étoile. |
| **Ambiance** | `ambience` | Configuration des étoiles : pour chaque étoile ou secteur désigné, un état fixe ou une séquence en boucle ; les étoiles non désignées sont éteintes. |
| **Séquence** | `sequence` | Jeu de couleurs, d'intensités, de clignotements et de temporisations des étoiles. Jouée une fois, ou en boucle (donc durable). |
| **Séquence d'entrée** | `intro_sequence` | Séquence facultative jouée par le pilote quand une ambiance s'active, avant qu'elle ne s'installe. Interne au pilote : ni file, ni priorité, invisible des autres éléments du système. |
| **Régie** | `control_panel` | Interface du Streamer pendant le live (fenêtre web ou plugin) : il y commande Starlight et y reçoit les alertes. Sa forme reste à définir (voir QO-11 et QO-45). |
| **Effet** | `effect` | Ce que le pilote sait jouer sur une étoile, avec ses paramètres (allumer en une couleur et une intensité, éteindre, passer progressivement d'une couleur à une autre). Brique de base d'une étape de séquence. |
| **Aperçu** | `preview` | Application provisoire, sur les étoiles, de la configuration en cours d'édition, avant validation ou annulation (UC-ADM-11). |
| **Essai** | `trial` | Action volontaire de l'Administrateur qui joue une séquence sur une étoile ou un secteur de son choix, à la demande (UC-ADM-04). Diffère de l'aperçu, qui est automatique. |
| **Événement** | `event` | Déclencheur extérieur qui entraîne une réaction. |
| **Réaction** | `reaction` | État temporaire déclenché par un événement extérieur, par le Streamer ou par l'Administrateur. Composée par l'Administrateur d'une ou plusieurs séquences ou ambiances, sous un nom (par exemple « Karmine »). |

## Règles de comportement

- À la fin d'une réaction, s'il n'y en a pas d'autre en attente, Starlight reprend l'ambiance précédente.
- L'extinction est une ambiance prédéfinie nommée « Off » : toutes les étoiles sont éteintes. Starlight a donc toujours une ambiance courante. L'ambiance « Off » est protégée : l'Administrateur ne peut ni la modifier ni la supprimer.
- Si plusieurs événements arrivent, leurs réactions sont placées dans une file d'attente classée par priorité (priorités à définir, voir QO-01).
- Une réaction manuelle du Streamer peut être prioritaire : elle passe devant toutes les réactions en attente, sans interrompre celle en cours.
- Une nouvelle ambiance choisie pendant une réaction devient l'ambiance courante tout de suite, mais ne s'affiche qu'à la fin des réactions.
- L'économie d'énergie (extinction après inactivité) ne s'applique pas en mode Stream.
- Le bouton OFF arrête la réaction en cours, vide la file et active l'ambiance « Off ». Il vaut en Lounge comme en Stream.
- Interdire les événements Twitch est une option du mode Stream : les événements sont alors ignorés et comptés, les ambiances et réactions du Streamer restent possibles.
- En mode Stream, le Convive ne peut pas agir : Twitch et le Streamer ont la main.
- L'Administrateur peut toujours prendre la main, quel que soit le mode.
- Toute modification de configuration passe par un aperçu sur les étoiles, puis par une validation ou une annulation ; pendant l'aperçu, la file de réactions est en pause et l'Administrateur est alerté quand des réactions attendent.
- Starlight n'envoie au pilote que les étoiles touchées : celles que l'ambiance (ou la séquence) désigne **et** qui appartiennent à un secteur du mode actif. Exceptions : le test manuel de l'Administrateur ignore les secteurs du mode, et l'ambiance « Off » éteint toutes les étoiles. Si rien n'est en commun, rien ne s'allume et le journal l'indique.

## Rôles

Les rôles (Convive, Streamer, Twitch, Administrateur, Système) et leurs droits sont décrits dans [`01-besoin/acteurs.md`](01-besoin/acteurs.md).

| Rôle | Terme anglais (code) |
|---|---|
| Convive | `guest` |
| Streamer | `streamer` |
| Twitch | `twitch` |
| Administrateur | `admin` |
| Système | `system` |

## Autres termes du code

| Terme | Terme anglais (code) |
|---|---|
| File d'attente (des réactions) | `reaction_queue` |
| Journal | `log` |
| Session d'édition | `editing_session` |
| Ambiance courante | `current_ambience` |
| Ambiance « Off » | `OFF` |

## Termes abandonnés

| Ancien terme | Remplacé par |
|---|---|
| Source de lumière, lumière | Étoile |
| Schéma, pattern | Séquence |
| Spectateur (Viewer) | Twitch (acteur externe) |
| Animation | Séquence |
| Architecte | Administrateur |
| Module, contrôleur (au sens de pilote d'étoile) | Pilote |
