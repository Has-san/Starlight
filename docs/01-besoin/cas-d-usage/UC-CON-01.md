# UC-CON-01 : Activer une ambiance

*Statut : validé.*

| Champ | Contenu |
|---|---|
| **Acteur principal** | Convive |
| **Objectif** | Changer l'ambiance lumineuse du salon. |
| **Déclencheur** | Le Convive sélectionne une ambiance via un actionneur (bouton poussoir, téléphone, télécommande : à définir, voir QO-11). |
| **Préconditions** | Starlight est en mode Lounge. |

## Scénario nominal

1. Le Convive sélectionne une ambiance disponible.
2. Starlight reçoit la demande.
3. Starlight applique la configuration de l'ambiance aux étoiles concernées.
4. L'ambiance sélectionnée devient l'ambiance courante et remplace la précédente.

## Scénarios alternatifs

- **A1, mode Stream actif** : la demande est ignorée, le Convive ne peut pas agir en mode Stream.
- **A2, ambiance déjà active** : aucun changement.
- **A3, étoile injoignable** : les autres étoiles appliquent l'ambiance, la défaillance est signalée (voir QO-14).
- **A4, étoiles éteintes par l'économie d'énergie** : la demande réactive les étoiles avec l'ambiance sélectionnée.

## Postconditions

- L'ambiance sélectionnée est l'ambiance courante.
- Toute temporisation d'inactivité repart de zéro (voir ID-04, QO-13).

## Questions liées

QO-05, QO-11, QO-13, QO-14
