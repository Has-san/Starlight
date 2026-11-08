# UC-ADM-04 : Gérer les séquences (créer, modifier, supprimer)

*Statut : brouillon, à valider.*

| Champ | Contenu |
|---|---|
| **Acteur principal** | Administrateur |
| **Objectif** | Créer ses propres séquences (clignotements, fondus, enchaînements) pour les utiliser dans des ambiances et des réactions. |
| **Déclencheur** | L'Administrateur ouvre la configuration des séquences. |
| **Préconditions** | En mode Stream, la configuration n'est pas verrouillée (voir UC-ADM-09). En mode Lounge, aucune condition. |

## Vocabulaire

- **Effet** : ce que le pilote sait jouer sur une étoile, avec ses paramètres. Exemples : allumer en une couleur et une intensité, éteindre, passer progressivement d'une couleur à une autre. C'est la brique de base d'une étape. 
- **Essai** : action volontaire de l'Administrateur qui joue une séquence sur une étoile ou un secteur de son choix, à la demande. Il diffère de l'**aperçu**, qui est automatique pendant l'édition (UC-ADM-11).

## Ce qu'est une séquence

- Un **nom**, choisi par l'Administrateur et unique.
- Des **étapes ordonnées dans le temps**. Chaque étape a une durée **réglée par l'Administrateur** (elle peut varier d'une étape à l'autre), vise des étoiles ou des secteurs, et applique un **effet** avec ses paramètres (couleur, intensité...). Les étapes peuvent se chevaucher.
- Une **répétition** : jouée une fois, ou en boucle.
- Les **effets** sont ceux que le pilote annonce, avec leurs paramètres. L'Administrateur ne voit que ceux-là.

Exemple : « Karmine », une suite d'allumages bleus et blancs de durées variables qui suit le rythme d'un chant de supporters. L'Administrateur règle lui-même ce rythme.

## Scénario nominal : créer une séquence

1. L'Administrateur demande la création d'une séquence et saisit un nom.
2. Il choisit la répétition (une fois ou en boucle).
3. Il ajoute des étapes : durée, étoiles ou secteurs visés, effet et paramètres.
4. Starlight joue l'**aperçu** de la séquence (UC-ADM-11).
5. L'Administrateur **valide** (ou annule) selon UC-ADM-11.
6. Starlight vérifie la séquence, l'enregistre et consigne la création dans le journal (acteur, séquence).

## Règles

- Les séquences sont éditées par aperçu, puis validation ou annulation (UC-ADM-11).
- **Une séquence en boucle est durable** : elle sert aux ambiances, jamais aux réactions, qui sont temporaires.
- **Une séquence utilisée dans une réaction est jouée une fois** et sa durée respecte la durée maximale d'une réaction (environ 10 secondes, voir QO-25). Cette durée est vérifiée à la validation de la séquence et de la réaction (UC-ADM-12).
- **Essai explicite** : l'Administrateur peut jouer une séquence sur une étoile ou un secteur de son choix, hors périmètre du mode, même si l'aperçu est désactivé. L'essai s'arrête à la fin de la séquence, à la durée maximale pour une boucle, ou quand l'Administrateur l'arrête.
- Un secteur ou une étoile indisponible peut être visé ; il joue la séquence quand il est disponible (voir QO-55 pour les ambiances).

## Scénarios alternatifs

- **A1, nom déjà utilisé** : refusé, rien n'est enregistré.
- **A2, effet que le pilote n'annonce plus** : la séquence est signalée comme invalide à l'Administrateur (alerte non bloquante) ; elle n'est pas jouée tant qu'elle n'est pas corrigée.
- **A3, modifier une séquence** : l'Administrateur peut changer le nom, la répétition et les étapes. Les ambiances et réactions qui l'utilisent suivent la configuration validée. Si la séquence en boucle est celle de l'ambiance courante, l'affichage suit tout de suite (QO-52).
- **A4, modification qui ferait dépasser la durée maximale d'une réaction, ou passer en boucle une séquence utilisée par une réaction** : refusée avec explication.
- **A5, supprimer une séquence utilisée par une ambiance ou une réaction** : refusé. L'Administrateur doit d'abord modifier ce qui l'utilise (QO-46).
- **A6, configuration verrouillée en mode Stream** : refusé ; l'Administrateur peut lever le verrou (UC-ADM-09).

## Postconditions

- La liste des séquences reflète la demande, ou reste inchangée si elle est refusée ou annulée.
- Le journal indique l'acteur et l'opération.

## Points non tranchés

- Saisie du rythme : régler à la main chaque durée est long pour un chant comme « Karmine ». Une aide (par exemple enregistrer le rythme en le frappant) est une idée à étudier, hors besoin pour l'instant.
- Plus tard, avec le son : suivre le rythme d'un son (ID-10).

## Questions liées

QO-02, QO-08, QO-10, QO-25, QO-46, QO-47, QO-52, QO-55
