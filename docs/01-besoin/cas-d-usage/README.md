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
| [UC-STR-04](UC-STR-04.md) | Interdire ou autoriser des types d'événements Twitch (un interrupteur par type) | Validé |
| [UC-STR-05](UC-STR-05.md) | Choisir les secteurs du mode Stream | Validé |
| [UC-TWI-01](UC-TWI-01.md) | Émettre un événement entraînant une réaction | Validé |
| [UC-ADM-01](UC-ADM-01.md) | Consulter et nommer les étoiles (annoncées par le pilote) | Validé |
| [UC-ADM-02](UC-ADM-02.md) | Gérer les secteurs (créer, modifier, supprimer) | Validé |
| [UC-ADM-03](UC-ADM-03.md) | Gérer les ambiances (créer, modifier, supprimer ; « Off » est protégée) | Validé |
| [UC-ADM-04](UC-ADM-04.md) | Gérer les séquences (créer, modifier, supprimer) | Validé |
| [UC-ADM-05](UC-ADM-05.md) | Activer une étoile ou un secteur | Validé |
| [UC-ADM-06](UC-ADM-06.md) | Rendre la main | Validé |
| [UC-ADM-07](UC-ADM-07.md) | Associer une réaction à un type d'événement | Validé |
| [UC-ADM-08](UC-ADM-08.md) | Connecter Starlight à Twitch | Validé |
| [UC-ADM-09](UC-ADM-09.md) | Verrouiller ou autoriser la configuration pendant le Stream | Validé |
| [UC-ADM-10](UC-ADM-10.md) | Définir les secteurs d'un mode (Lounge, Stream) | Validé |
| [UC-ADM-11](UC-ADM-11.md) | Valider ou annuler une configuration en cours (aperçu) | Validé |
| [UC-ADM-12](UC-ADM-12.md) | Gérer les réactions (créer, modifier, supprimer) | Validé |
| [UC-SYS-01](UC-SYS-01.md) | Économie d'énergie (mode Lounge uniquement) | Validé |
| [UC-SYS-02](UC-SYS-02.md) | Passage en mode Stream (ambiance neutre, réaction facultative, récapitulatif) | Validé |
| [UC-STR-06](UC-STR-06.md) | Démarrer le live (séquence d'ouverture, déclenchement manuel) | Brouillon |

Les comportements du Système sont décrits comme des cas d'usage dont l'acteur est le Système (déclenchement par le temps ou par un changement de mode).
