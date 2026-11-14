# UC-ADM-05 : Activer une étoile ou un secteur

*Statut : validé.*

| Champ | Contenu |
|---|---|
| **Acteur principal** | Administrateur |
| **Objectif** | Allumer ou éteindre à la main des étoiles ou des secteurs, pour tester ou pour un cas particulier. |
| **Déclencheur** | L'Administrateur sélectionne des étoiles ou des secteurs et commande un effet. |
| **Préconditions** | Aucune : possible en mode Lounge comme en mode Stream. |

## Principe

- Commander une étoile ou un secteur est une **prise de main** : ces étoiles sont dites **en manuel**. Ni les changements d'ambiance ni les réactions ne les touchent tant qu'elles le restent.
- La commande **ignore les secteurs des modes**, comme l'aperçu (UC-ADM-11).
- Ce n'est pas de la configuration : ni aperçu ni validation (UC-ADM-11 n'est pas utilisé), et le verrou de UC-ADM-09 ne l'empêche pas.
- Les effets commandables sont ceux que le pilote annonce : **allumer** (couleur, intensité) ou **éteindre**. Un effet qui boucle est réservé aux séquences.
- La prise de main se termine par **UC-ADM-06** (rendre la main) ou par la libération automatique ci-dessous.
- Pour le reste du système, c'est transparent : les étoiles en manuel sont simplement des étoiles qu'aucune ambiance ne pilote.

## Scénario nominal

1. L'Administrateur ouvre la liste des étoiles et des secteurs (celles qui sont indisponibles sont signalées).
2. Il sélectionne une ou plusieurs étoiles ou un ou plusieurs secteurs.
3. Il choisit l'effet : allumer (couleur, intensité) ou éteindre.
4. Starlight envoie la commande au pilote pour les étoiles concernées (un secteur désigne toutes ses étoiles) et les marque **en manuel**.
5. Starlight consigne dans le journal : acteur, cibles, effet.
6. L'interface de l'Administrateur et la régie du Streamer affichent « étoiles en manuel », avec une alerte tant qu'il en reste.

## Libération automatique

Une étoile en manuel peut être rendue au système sans action de l'Administrateur :

- le réglage est **propre à chaque mode** (Lounge, Stream) : un interrupteur actif ou inactif, et une durée **paramétrable** ;
- valeurs par défaut : **active en mode Stream, inactive en mode Lounge** ;
- le délai court depuis la dernière commande sur ces étoiles ; toute nouvelle commande le remet à zéro ;
- l'Administrateur est prévenu avant la libération et peut la repousser, avec le même préavis paramétrable que pour une session d'édition oubliée (UC-ADM-11) ;
- les étoiles reprennent l'ambiance courante (comme UC-ADM-06), et la libération est consignée au journal (acteur « Système », motif « délai ») ;
- au **changement de mode**, c'est le réglage du mode actif qui s'applique, et le délai redémarre à l'entrée dans le nouveau mode.

## Scénarios alternatifs

- **A1, étoile indisponible** : la commande est refusée pour cette étoile, les autres l'appliquent, le refus est signalé.
- **A2, étoile dans plusieurs secteurs** : une commande par secteur ne la touche qu'une fois ; la dernière commande reçue s'applique.
- **A3, nouvelle commande sur une étoile déjà en manuel** : le nouvel effet remplace l'ancien et le délai de libération repart de zéro.
- **A4, changement d'ambiance ou réaction pendant la prise de main** : les étoiles en manuel ne sont pas touchées.
- **A5, bouton « Off »** : il éteint aussi les étoiles en manuel et met fin à la prise de main : elles passent sous l'ambiance « Off » (QO-60).
- **A6 bis, session d'édition ouverte** : la commande manuelle est refusée tant qu'une session d'édition (aperçu) est ouverte, pour éviter deux sources de commande sur les mêmes étoiles (QO-60).
- **A6, retour d'une étoile après indisponibilité** : si elle n'est pas en manuel, elle reprend l'ambiance courante (QO-55).

## Postconditions

- Les étoiles commandées sont en manuel, dans l'effet demandé.
- Le journal indique l'acteur, les cibles et l'effet.
- Aucune configuration n'a changé.

## Questions liées

QO-48, QO-54, QO-55, QO-60
