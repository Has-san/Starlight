# Acteurs

Rôles qui interagissent avec Starlight. Les termes sont définis dans le [glossaire](../glossaire.md).

| Rôle | Description | Droits |
|---|---|---|
| **Convive** | Utilisateur en mode Lounge. Une ou plusieurs personnes présentes dans le salon. | Active une ambiance (sans pouvoir en créer). Éteint les étoiles. Aucune action possible en mode Stream. |
| **Streamer** | Streamer en mode Stream. | Active une ambiance. Déclenche manuellement une réaction. Vide la file, arrête la réaction en cours, utilise le bouton OFF. Interdit ou autorise chaque type d'événement Twitch et confirme le récapitulatif. Choisit les secteurs du mode Stream. Change de mode, démarre et termine le live. Dispose de l'aperçu (activable à tout moment). |
| **Twitch** | Acteur externe. | Émet un événement entraînant une réaction prédéfinie. |
| **Administrateur** | Gère la configuration de Starlight. | Crée, modifie, supprime secteurs, ambiances (sauf « Off »), séquences et réactions. Consulte et nomme les étoiles annoncées par le pilote, et voit si elles sont disponibles. Associe une réaction à chaque type d'événement. Active chaque étoile ou secteur. Définit les secteurs de chaque mode. Déclenche une réaction. Peut prendre la main à tout moment et la rendre. Connecte Starlight à Twitch. Verrouille ou autorise la configuration pendant le Stream. Valide ou annule une configuration en cours (aperçu). Règle les délais (économie d'énergie, sessions oubliées, libération automatique, alerte de fin de live). Peut faire tout ce que fait le Streamer, y compris changer de mode et démarrer ou terminer le live. |
| **Système** | Acteur interne de Starlight. | Exécute des comportements particuliers déclenchés par le temps ou par un changement de mode (économie d'énergie, passage en mode Stream, sortie du mode Stream, coupure automatique après une alerte de fin de live, séquences de diagnostic). |

Schémas d'états par acteur : [Convive](etats-convive.drawio.svg), [Streamer](etats-streamer.drawio.svg), [Twitch](etats-twitch.drawio.svg), [Système](etats-systeme.drawio.svg). Celui du Streamer couvre le mode Stream et le cycle du live (UC-STR-01 à UC-STR-08). Celui de l'Administrateur reste à dessiner.

Le développeur n'est pas un rôle du système en fonctionnement.
