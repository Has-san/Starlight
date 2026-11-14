# UC-ADM-12 : Gérer les réactions (créer, modifier, supprimer)

*Statut : validé.*

| Champ | Contenu |
|---|---|
| **Acteur principal** | Administrateur |
| **Objectif** | Composer ses propres réactions (par exemple « Karmine ») pour les associer à des événements ou les déclencher à la main. |
| **Déclencheur** | L'Administrateur ouvre la configuration des réactions. |
| **Préconditions** | En mode Stream, la configuration n'est pas verrouillée (voir UC-ADM-09). En mode Lounge, aucune condition. |

## Ce qu'est une réaction

- Un **nom**, choisi par l'Administrateur et unique.
- Des **éléments placés sur une ligne de temps**. Chaque élément est une **séquence** (jouée une fois, jamais en boucle) ou une **ambiance** (affichée pendant une durée donnée), avec un **instant de départ**.
  - Deux éléments qui partent au même instant jouent **en simultané** (sur leurs propres cibles) ; un élément qui part à la fin d'un autre joue **en série**. On peut aussi les mélanger ou les faire se chevaucher (QO-02).
  - Les cibles (étoiles ou secteurs) sont celles de la séquence ou de l'ambiance choisie.
- Une **durée totale**, égale à la fin du dernier élément. Elle ne dépasse pas la **durée maximale d'une réaction** : 10 secondes par défaut, la même pour toutes les réactions, **paramétrable** (QO-25).
- La réaction est **temporaire** : jouée une fois, elle laisse ensuite la place à l'ambiance courante.
- La **priorité** n'est pas une propriété de la réaction : elle est choisie dans l'association à un type d'événement (UC-ADM-07) ou par la personne qui déclenche la réaction (UC-STR-02).

## Scénario nominal : créer une réaction

1. L'Administrateur demande la création d'une réaction et saisit un nom.
2. Il ajoute des éléments : une séquence ou une ambiance, avec son instant de départ (et sa durée pour une ambiance).
3. Starlight joue l'**aperçu** de la réaction (UC-ADM-11).
4. L'Administrateur **valide** (ou annule) selon UC-ADM-11.
5. Starlight vérifie la réaction, l'enregistre et consigne la création dans le journal (acteur, réaction).

## Règles

- Les réactions sont éditées par aperçu, puis validation ou annulation (UC-ADM-11).
- **À la validation**, Starlight vérifie : nom unique, au moins un élément, aucune séquence en boucle, durée totale inférieure ou égale au maximum, éléments existants et valides.
- Une réaction dont un effet n'est plus annoncé par le pilote est signalée comme invalide (alerte non bloquante) et n'est pas jouée tant qu'elle n'est pas corrigée.
- Les séquences et les ambiances utilisées par une réaction ne peuvent pas être supprimées tant que la réaction existe (UC-ADM-03, UC-ADM-04, QO-46).
- **Essai** : l'Administrateur peut jouer une réaction à l'essai comme une séquence (UC-ADM-04) : prise de main sur les étoiles visées, possible même quand la configuration est verrouillée, étoiles rendues à la fin.
- **Pas de réaction dans une réaction** : une réaction ne contient que des séquences et des ambiances, pour garder une durée vérifiable.
- **Suppression d'une réaction non associée alors qu'une demande manuelle est en file** : la demande en file est jouée avec la version qui existait à son arrivée (QO-44).

## Scénarios alternatifs

- **A1, nom déjà utilisé** : refusé, rien n'est enregistré.
- **A2, durée supérieure au maximum, séquence en boucle ou réaction vide** : refusé avec explication ; rien n'est raccourci en silence.
- **A3, modifier une réaction** : l'Administrateur peut changer le nom et les éléments. La nouvelle version s'applique aux événements à venir ; les réactions déjà en file ou en cours ne changent pas (QO-44).
- **A4, supprimer une réaction associée à un type d'événement** : refusé (UC-ADM-07). L'Administrateur doit d'abord retirer l'association.
- **A5, supprimer une réaction non associée** : autorisé ; la suppression est consignée.
- **A6, configuration verrouillée en mode Stream** : refusé ; l'Administrateur peut lever le verrou (UC-ADM-09).

## Postconditions

- La liste des réactions reflète la demande, ou reste inchangée si elle est refusée ou annulée.
- Le journal indique l'acteur et l'opération.

## Points non tranchés

- **Variation selon le nombre d'occurrences** (rafale, QO-22) : hors de ce cas d'usage pour l'instant.

## Questions liées

QO-02, QO-22, QO-25, QO-44, QO-46, QO-56
