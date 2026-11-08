# Inventaire des cas d'usage

Un fichier par cas d'usage, nommé par son identifiant. Format : `UC-<rôle>-<numéro>`, où le rôle est celui de l'acteur principal ([acteurs](../acteurs.md)) :
`CON` Convive, `STR` Streamer, `TWI` Twitch, `ADM` Administrateur, `SYS` Système.

Les identifiants sont stables : un numéro n'est jamais réutilisé.

| ID | Titre | Statut |
|---|---|---|
| [UC-CON-01](UC-CON-01.md) | Activer une ambiance | Validé |
| [UC-CON-02](UC-CON-02.md) | Éteindre les étoiles | Validé |
| [UC-STR-01](UC-STR-01.md) | Activer une ambiance | Validé |
| [UC-STR-02](UC-STR-02.md) | Déclencher manuellement une réaction | Validé |
| [UC-STR-03](UC-STR-03.md) | Arrêter les réactions (vider la file, arrêter la réaction en cours, bouton OFF) | Validé |
| [UC-STR-04](UC-STR-04.md) | Interdire ou autoriser des types d'événements Twitch (un interrupteur par type) | À valider |
| UC-STR-05 | Définir le périmètre du mode Stream | À rédiger |
| [UC-TWI-01](UC-TWI-01.md) | Émettre un événement entraînant une réaction | Validé |
| [UC-ADM-01](UC-ADM-01.md) | Consulter et nommer les étoiles (annoncées par le pilote) | Validé |
| [UC-ADM-02](UC-ADM-02.md) | Gérer les secteurs (créer, modifier, supprimer) | Validé |
| [UC-ADM-03](UC-ADM-03.md) | Gérer les ambiances (créer, modifier, supprimer ; « Off » est protégée) | Validé |
| [UC-ADM-04](UC-ADM-04.md) | Gérer les séquences (créer, modifier, supprimer) | Brouillon |
| UC-ADM-05 | Activer une étoile ou un secteur | À rédiger |
| UC-ADM-06 | Rendre la main | À rédiger |
| [UC-ADM-07](UC-ADM-07.md) | Associer une réaction à un type d'événement | Validé |
| [UC-ADM-08](UC-ADM-08.md) | Connecter Starlight à Twitch | Validé |
| UC-ADM-09 | Verrouiller ou autoriser la configuration pendant le Stream | À rédiger |
| UC-ADM-10 | Définir le périmètre d'un mode (étoiles et secteurs utilisés par Lounge, Stream) | À rédiger |
| [UC-ADM-11](UC-ADM-11.md) | Valider ou annuler une configuration en cours (aperçu) | Validé |
| UC-ADM-12 | Gérer les réactions (créer, modifier, supprimer) | À rédiger |
| UC-SYS-01 | Économie d'énergie (mode Lounge uniquement) | À rédiger |
| UC-SYS-02 | Séquence d'ouverture du mode Stream | À rédiger |

Les comportements du Système sont décrits comme des cas d'usage dont l'acteur est le Système (déclenchement par le temps ou par un changement de mode).
