# UC-ADM-09 : Verrouiller ou autoriser la configuration pendant le Stream

*Statut : validé.*

| Champ | Contenu |
|---|---|
| **Acteur principal** | Administrateur |
| **Objectif** | Protéger un live de toute modification de configuration accidentelle, ou la permettre volontairement. |
| **Déclencheur** | L'Administrateur verrouille ou déverrouille la configuration. |
| **Préconditions** | Aucune : le réglage se bascule à tout moment, y compris en plein live et en mode Lounge. |

Schéma : [UC-ADM-09.drawio.svg](UC-ADM-09.drawio.svg).

## Principe

- Le verrou est un réglage de l'Administrateur : « verrouiller la configuration pendant le Stream ». Il est **conservé d'un live à l'autre**.
- Valeur par défaut : **verrouillé**. L'Administrateur doit déverrouiller volontairement pour modifier la configuration en direct.
- Le verrou n'a d'effet qu'en **mode Stream**. En mode Lounge, rien n'est verrouillé.
- Le Streamer voit l'état du verrou dans sa régie.

## Ce que le verrou couvre

| Verrouillé : refusé | Toujours possible |
|---|---|
| Toute modification de configuration : nommer une étoile (UC-ADM-01), secteurs (UC-ADM-02), ambiances (UC-ADM-03), séquences (UC-ADM-04), associations événement → réaction (UC-ADM-07), secteurs d'un mode (UC-ADM-10), réactions (UC-ADM-12) | Consulter la configuration |
| | Actions de live : activer une ambiance, déclencher une réaction, arrêter, bouton OFF |
| | Test manuel d'une étoile ou d'un secteur |
| | Choix des secteurs du mode Stream par le Streamer (UC-STR-05) |

## Scénario nominal : verrouiller

1. L'Administrateur demande de verrouiller la configuration.
2. Si une session d'édition est ouverte (UC-ADM-11), Starlight lui demande d'abord de **valider ou d'annuler** ; rien n'est appliqué en silence.
3. Starlight active le verrou et consigne dans le journal : acteur, moment, nouvel état.
4. La régie du Streamer affiche que la configuration est verrouillée.

## Scénario nominal : déverrouiller

1. L'Administrateur demande de déverrouiller la configuration.
2. Starlight lève le verrou et consigne dans le journal : acteur, moment, nouvel état.
3. La régie du Streamer affiche que la configuration est déverrouillée.
4. Les modifications repassent par la session d'édition de UC-ADM-11 (aperçu, validation ou annulation).

## Scénarios alternatifs

- **A1, mode Lounge actif** : le réglage reste modifiable ; il prend effet à l'entrée en mode Stream.
- **A2, déjà dans l'état demandé** : aucun changement, rien n'est consigné.
- **A3, session d'édition ouverte au moment de verrouiller** : voir l'étape 2 ; si l'Administrateur ne valide ni n'annule, le verrouillage n'est pas appliqué.
- **A4, entrée en mode Stream** : le verrou est dans l'état où il a été laissé au live précédent.

## Postconditions

- Le verrou est dans l'état demandé et enregistré.
- Le journal indique l'acteur, le moment et le nouvel état.
- En mode Stream verrouillé, aucune modification de configuration n'est possible.

## Verrou laissé ouvert par oubli

Le verrou étant conservé d'un live à l'autre, un déverrouillage oublié laisserait le live suivant sans protection. L'état du verrou figure donc dans le récapitulatif de début de live (UC-STR-04), avec une alerte persistante tant que la configuration est déverrouillée (QO-59).

## Points non tranchés

- **Session d'édition oubliée** : annulée automatiquement après un délai paramétrable (voir UC-ADM-11, QO-54).

## Questions liées

QO-48, QO-53, QO-54, QO-59
