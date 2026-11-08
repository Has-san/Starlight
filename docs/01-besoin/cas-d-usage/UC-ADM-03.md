# UC-ADM-03 : Gérer les ambiances (créer, modifier, supprimer)

*Statut : validé.*

| Champ | Contenu |
|---|---|
| **Acteur principal** | Administrateur |
| **Objectif** | Définir les ambiances que le Convive et le Streamer pourront activer. |
| **Déclencheur** | L'Administrateur ouvre la configuration des ambiances. |
| **Préconditions** | En mode Stream, la configuration n'est pas verrouillée (voir UC-ADM-09). En mode Lounge, aucune condition. |

## Ce qu'est une ambiance

- Un **nom**, choisi par l'Administrateur et unique.
- Une ou plusieurs **désignations**. Chacune vise une étoile ou un secteur entier et dit ce qu'il fait :
  - soit un **état fixe** (couleur, intensité), décrit à l'intention : le pilote le traduit selon les capacités de chaque étoile (QO-10) ;
  - soit une **séquence en boucle**, exécutée localement par le pilote.
- Les étoiles du périmètre du mode que l'ambiance ne désigne pas sont **éteintes**.
- L'ambiance **« Off »** est prédéfinie et protégée : l'Administrateur ne peut ni la modifier ni la supprimer (QO-17).

## Résolution des désignations

- Une étoile désignée **directement** l'emporte sur un secteur qui la contient (« Salon en bleu, sauf la lampe 2 en rouge »).
- Si deux secteurs donnent des états différents à la même étoile, la validation est **refusée** avec une explication (quelle étoile, quels secteurs). L'Administrateur lève lui-même l'ambiguïté.

## Scénario nominal : créer une ambiance

1. L'Administrateur demande la création d'une ambiance et saisit un nom.
2. Il ajoute des désignations (étoile ou secteur) et choisit pour chacune un état fixe ou une séquence en boucle.
3. Starlight montre l'**aperçu** sur les étoiles (UC-ADM-11).
4. L'Administrateur **valide** (ou annule) selon UC-ADM-11.
5. Starlight vérifie le nom et les désignations, enregistre l'ambiance et consigne la création dans le journal (acteur, ambiance, désignations).

## Règles

- Les ambiances sont éditées par aperçu, puis validation ou annulation (UC-ADM-11).
- À la fin d'une réaction, l'ambiance courante reprend. Si elle contient une séquence en boucle, celle-ci **redémarre** depuis le début (proposé).
- La séquence d'entrée d'une ambiance (ID-09) est interne au pilote : elle n'est pas configurée ici.

## Scénarios alternatifs

- **A1, nom déjà utilisé** : refusé, rien n'est enregistré.
- **A2, désignations en conflit** : validation refusée, avec explication (voir « Résolution des désignations »). La session reste ouverte.
- **A3, modifier une ambiance** : l'Administrateur peut changer le nom et les désignations. Si l'ambiance est l'ambiance courante, l'affichage suit la configuration validée tout de suite (QO-52).
- **A4, supprimer une ambiance utilisée par une réaction** : refusé. L'Administrateur doit d'abord modifier la réaction (QO-46).
- **A5, supprimer l'ambiance courante** : refusé. Starlight a toujours une ambiance courante : il faut d'abord en activer une autre.
- **A6, « Off »** : toute modification ou suppression est refusée.
- **A7, configuration verrouillée en mode Stream** : refusé ; l'Administrateur peut lever le verrou (UC-ADM-09).
- **A8, étoile indisponible désignée** : autorisée. À son retour, l'étoile reprend l'ambiance courante (QO-55).

## Postconditions

- La liste des ambiances reflète la demande, ou reste inchangée si elle est refusée ou annulée.
- Le journal indique l'acteur et l'opération.

## Points non tranchés

Aucun. Les séquences en boucle d'une ambiance sont celles que l'Administrateur crée (UC-ADM-04).

## Questions liées

QO-08, QO-10, QO-17, QO-34, QO-46, QO-52, QO-55
