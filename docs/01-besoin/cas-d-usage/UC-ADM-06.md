# UC-ADM-06 : Rendre la main

*Statut : validé.*

| Champ | Contenu |
|---|---|
| **Acteur principal** | Administrateur (le Streamer voit l'état dans sa régie, sans pouvoir rendre la main) |
| **Objectif** | Rendre au système les étoiles que l'Administrateur a prises en manuel (UC-ADM-05). |
| **Déclencheur** | L'Administrateur demande de rendre la main : sur toutes les étoiles en manuel, ou sur des étoiles ou des secteurs choisis. |
| **Préconditions** | Au moins une étoile est en manuel. |

## Principe

- Rendre la main est l'inverse de UC-ADM-05. Ce n'est pas de la configuration : ni aperçu ni validation, et le verrou de UC-ADM-09 ne l'empêche pas.
- Deux façons de rendre la main : **tout rendre** (un seul geste, pour fermer une séance de test) ou **rendre la main sur une sélection** d'étoiles ou de secteurs (pour garder un cas particulier pendant qu'on en teste un autre).
- La libération automatique de UC-ADM-05 produit le même effet, avec « Système » comme acteur et « délai » comme motif.

## Scénario nominal

1. L'Administrateur ouvre la liste des étoiles en manuel.
2. Il choisit « tout rendre », ou sélectionne des étoiles ou des secteurs.
3. Starlight retire la prise de main sur les étoiles concernées. Un secteur désigne toutes ses étoiles ; une étoile qui appartient à un secteur sélectionné et à un secteur non sélectionné est rendue.
4. Ces étoiles reprennent l'**ambiance courante**. Si une réaction est en cours, elles ne la rejoignent pas : elles affichent l'ambiance courante, et la réaction continue sur les autres étoiles.
5. Starlight consigne dans le journal : acteur, étoiles rendues, motif « demande de l'Administrateur ».
6. L'interface de l'Administrateur et la régie du Streamer mettent à jour « étoiles en manuel » ; l'alerte disparaît quand il n'en reste plus.

## Scénarios alternatifs

- **A1, aucune étoile en manuel** : rien à faire ; l'Administrateur en est informé.
- **A2, étoile indisponible** : elle n'est plus en manuel ; à son retour elle reprend l'ambiance courante (QO-55).
- **A3, session d'édition ouverte** : rendre la main reste possible ; ce n'est pas une commande sur les étoiles (le refus de UC-ADM-05 vise les commandes, QO-60).
- **A4, bouton « Off »** : il met déjà fin à la prise de main (UC-ADM-05, A5) ; rien d'autre à rendre.
- **A5, libération automatique en même temps** : la première des deux s'applique ; la seconde ne trouve rien à rendre.
- **A6, ambiance courante « Off »** : les étoiles rendues restent éteintes.

## Postconditions

- Les étoiles concernées ne sont plus en manuel et affichent l'ambiance courante.
- Le journal indique l'acteur, les étoiles et le motif.
- Aucune configuration n'a changé.

## Questions liées

QO-48, QO-54, QO-55, QO-60
