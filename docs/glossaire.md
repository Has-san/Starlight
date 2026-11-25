# Glossaire Starlight

Ce document fixe le vocabulaire du projet. Tout autre document (besoin, spécifications, code, commentaires) doit l'employer tel quel.

La documentation est en français, le code en anglais (QO-21) : la colonne « Terme anglais » donne le nom à employer dans le code.

## Définitions

| Terme | Terme anglais (code) | Définition |
|---|---|---|
| **Starlight** | `Starlight` | Système qui gère la quasi-totalité du besoin : modes, ambiances, séquences, réactions, événements Twitch, configuration, journal (code dans `host/`). Il commande les étoiles par l'intermédiaire de Star Guardian. |
| **Étoile** | `star` | Source de lumière individuelle et pilotable du système, identifiée de façon unique. Un ruban de LED est une étoile. Les capacités peuvent différer d'une étoile à l'autre : seul le pilote les connaît. L'étoile est annoncée par le pilote, avec un identifiant stable ; l'Administrateur ne la crée ni ne la supprime. |
| **Pilote** | `driver` | Élément qui commande les étoiles : il connaît leurs capacités et décide comment jouer sur chacune une séquence ou une ambiance. Il ne connaît pas les secteurs : Starlight ne lui transmet que les étoiles concernées. « Pilote » est le terme générique du rôle ; le système qui l'assure s'appelle Star Guardian. |
| **Star Guardian** | `star_guardian` | Nom du système qui assure le rôle de pilote des étoiles (code dans `firmware/`) : il annonce les étoiles et leurs capacités, joue les effets et les séquences d'entrée, signale les étoiles indisponibles. Starlight et Star Guardian sont deux systèmes distincts, reliés par une interface. |
| **Secteur** | `sector` | Groupe prédéfini d'étoiles. Sert à l'Administrateur et au Streamer à désigner plusieurs étoiles d'un coup. Une étoile peut appartenir à plusieurs secteurs ; un secteur ne contient pas d'autre secteur. |
| **Mode** | `mode` | Manière de fonctionner de Starlight : Lounge ou Stream. Chaque mode a ses **secteurs** : ceux qu'il utilise. Une étoile seule entre dans un mode par un secteur d'une étoile. |
| **Ambiance** | `ambience` | Configuration des étoiles : pour chaque étoile ou secteur désigné, un état fixe ou une séquence en boucle ; les étoiles non désignées sont éteintes. |
| **Séquence** | `sequence` | Jeu de couleurs, d'intensités, de clignotements et de temporisations des étoiles. Jouée une fois, ou en boucle (donc durable). |
| **Effet d'apparition** | `appear_effect` | Effet facultatif joué par Star Guardian quand une ambiance s'active, avant qu'elle ne s'installe. Starlight le déclenche seulement par l'option « avec apparition » d'une commande, sans en connaître le contenu ; les commandes manuelles et les essais s'envoient « sans apparition ». Ni file, ni priorité. |
| **Régie** | `control_panel` | Interface du Streamer pendant le live (fenêtre web ou plugin) : il y commande Starlight et y reçoit les alertes. Sa forme reste à définir (voir QO-11 et QO-45). |
| **Effet** | `effect` | Ce que le pilote sait jouer sur une étoile, avec ses paramètres (allumer en une couleur et une intensité, éteindre, passer progressivement d'une couleur à une autre). Brique de base d'une étape de séquence. |
| **Aperçu** | `preview` | Application provisoire, sur les étoiles, de la configuration en cours d'édition, avant validation ou annulation (UC-ADM-11). |
| **Essai** | `trial` | Action volontaire de l'Administrateur qui joue une séquence sur une étoile ou un secteur de son choix, à la demande (UC-ADM-04). Diffère de l'aperçu, qui est automatique. |
| **Événement** | `event` | Déclencheur qui entraîne une réaction : événement extérieur (Twitch) ou **événement du Système** (passage en mode Stream, début du live, fin du live). |
| **Réaction** | `reaction` | État temporaire déclenché par un événement, par le Streamer ou par l'Administrateur. Composée par l'Administrateur d'une ou plusieurs séquences ou ambiances, sous un nom (par exemple « Karmine »). |
| **Événement du Système** | `system_event` | Événement interne à Starlight, auquel l'Administrateur peut associer une réaction : passage en mode Stream (UC-SYS-02), début du live (UC-STR-06), fin du live (UC-STR-07). |
| **Début du live** | `live_start` | Moment où le Streamer déclare, à la main, que les spectateurs voient le live. Joue la séquence d'ouverture (réaction associée) et remet en service les récompenses de points de chaîne (UC-STR-06). |
| **Fin du live** | `live_end` | Moment où le Streamer termine le live, à la main (une alerte le lui propose si Twitch signale le live hors ligne). Remet les récompenses de points de chaîne en pause (UC-STR-07). Distincte de la sortie du mode Stream. |
| **Ambiance neutre** | `neutral_ambience` | Ambiance du mode Stream, personnalisable, appliquée à l'entrée en mode Stream. « Off » si aucune n'est désignée (UC-SYS-02). |
| **Étoile en manuel** | `manual_hold` | État d'une étoile (ou d'un secteur) dont l'Administrateur a pris la main : les ambiances et les réactions ne la touchent plus, et elle ignore les secteurs du mode, jusqu'à ce qu'il rende la main ou que la libération automatique ait lieu (UC-ADM-05, UC-ADM-06). |
| **Verrou de configuration** | `config_lock` | Protection du mode Stream : verrouillé, il empêche toute modification de la configuration. Verrouillé par défaut, conservé d'un live à l'autre (UC-ADM-09). |
| **Récapitulatif** | `start_recap` | Affichage de la régie à l'entrée en mode Stream : état des interrupteurs d'événements et du verrou, avec confirmation obligatoire du Streamer (UC-STR-04, UC-ADM-09). |

## Règles de comportement

- À la fin d'une réaction, s'il n'y en a pas d'autre en attente, Starlight reprend l'ambiance précédente.
- L'extinction est une ambiance prédéfinie nommée « Off » : toutes les étoiles sont éteintes. Starlight a donc toujours une ambiance courante. L'ambiance « Off » est protégée : l'Administrateur ne peut ni la modifier ni la supprimer.
- Si plusieurs événements arrivent, leurs réactions sont placées dans une file d'attente classée par priorité (priorités à définir, voir QO-01).
- Une réaction manuelle du Streamer peut être prioritaire : elle passe devant toutes les réactions en attente, sans interrompre celle en cours.
- Une nouvelle ambiance choisie pendant une réaction devient l'ambiance courante tout de suite, mais ne s'affiche qu'à la fin des réactions.
- L'économie d'énergie (extinction après inactivité) ne s'applique pas en mode Stream.
- Le bouton OFF arrête la réaction en cours, vide la file et active l'ambiance « Off ». Il vaut en Lounge comme en Stream.
- Chaque type d'événement Twitch a un interrupteur (autorisé ou interdit), option du mode Stream : un type interdit est ignoré et compté, les ambiances et réactions du Streamer restent possibles. Seules les récompenses de points de chaîne peuvent être bloquées en amont (mise en pause). Avant le début du live, elles sont toutes en pause.
- En mode Stream, le Convive ne peut pas agir : Twitch et le Streamer ont la main. Seuls le Streamer et l'Administrateur changent de mode, à la main.
- Le mode Stream a deux moments distincts à chaque extrémité : le passage en Stream (étoiles sur l'ambiance neutre, seul le Streamer les voit) puis le début du live (séquence d'ouverture pour les spectateurs, manuel) ; la fin du live (manuelle) puis la sortie du Stream (retour à la dernière ambiance du Lounge).
- L'Administrateur peut toujours prendre la main, quel que soit le mode.
- Toute modification de configuration passe par un aperçu sur les étoiles, puis par une validation ou une annulation ; pendant l'aperçu, la file de réactions est en pause et l'Administrateur est alerté quand des réactions attendent.
- Starlight n'envoie au pilote que les étoiles touchées : celles que l'ambiance (ou la séquence) désigne **et** qui appartiennent à un secteur du mode actif. Exceptions : le test manuel de l'Administrateur ignore les secteurs du mode, et l'ambiance « Off » éteint toutes les étoiles. Si rien n'est en commun, rien ne s'allume et le journal l'indique.

## Rôles

Les rôles (Convive, Streamer, Twitch, Administrateur) et leurs droits sont décrits dans [`01-besoin/acteurs.md`](01-besoin/acteurs.md).

| Rôle | Terme anglais (code) |
|---|---|
| Convive | `guest` |
| Streamer | `streamer` |
| Twitch | `twitch` |
| Administrateur | `admin` |
| Système (système complet : auteur d'une action automatique au journal ; pas un acteur) | `system` |

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
