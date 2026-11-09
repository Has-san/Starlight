# UC-CON-02 : Éteindre les étoiles

*Statut : validé.*

| Champ | Contenu |
|---|---|
| **Acteur principal** | Convive |
| **Objectif** | Éteindre toutes les étoiles en activant l'ambiance prédéfinie « Off ». |
| **Déclencheur** | Le Convive demande l'extinction via un actionneur (voir QO-11). |
| **Préconditions** | Starlight est en mode Lounge. |

Schéma : [UC-CON-02.drawio.svg](UC-CON-02.drawio.svg).

## Scénario nominal

1. Le Convive demande l'extinction.
2. Starlight reçoit la demande.
3. Starlight active l'ambiance « Off » (toutes les étoiles éteintes).
4. « Off » devient l'ambiance courante et remplace la précédente.

## Scénarios alternatifs

- **A1, mode Stream actif** : la demande est ignorée.
- **A2, ambiance « Off » déjà courante** : aucun changement.
- **A3, étoile injoignable** : les autres étoiles s'éteignent, la défaillance est consignée dans le journal (voir QO-14). L'étoile injoignable s'éteindra d'elle-même après le délai de sécurité (voir QO-16).
- **A4, économie d'énergie en cours** : la demande interrompt la séquence et éteint immédiatement les étoiles.

## Postconditions

- L'ambiance courante est « Off » : les étoiles sont éteintes.
- La temporisation d'inactivité est arrêtée.

## Questions liées

QO-05, QO-11, QO-14, QO-16, QO-17
