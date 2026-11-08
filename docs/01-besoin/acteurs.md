# Acteurs

Rôles qui interagissent avec Starlight. Les termes sont définis dans le [glossaire](../glossaire.md).

| Rôle | Description | Droits |
|---|---|---|
| **Convive** | Utilisateur en mode Lounge. Une ou plusieurs personnes présentes dans le salon. | Active une ambiance (sans pouvoir en créer). Éteint les étoiles. Aucune action possible en mode Stream. |
| **Streamer** | Streamer en mode Stream. | Active une ambiance. Déclenche manuellement une réaction. Vide la file, arrête la réaction en cours, utilise le bouton OFF. Interdit ou autorise les événements Twitch. Choisit les secteurs du mode Stream. |
| **Twitch** | Acteur externe. | Émet un événement entraînant une réaction prédéfinie. |
| **Administrateur** | Gère la configuration de Starlight. | Crée, modifie, supprime secteurs, ambiances (sauf « Off »), séquences et réactions. Consulte et nomme les étoiles annoncées par le pilote, et voit si elles sont disponibles. Associe une réaction à chaque type d'événement. Active chaque étoile ou secteur. Définit les secteurs de chaque mode. Déclenche une réaction. Peut prendre la main à tout moment. |
| **Système** | Acteur interne de Starlight. | Exécute des comportements particuliers déclenchés par le temps ou par un changement de mode (économie d'énergie, séquence d'ouverture du mode Stream, séquences de diagnostic). |

Le développeur n'est pas un rôle du système en fonctionnement.
