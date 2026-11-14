# UC-SYS-01 : Économie d'énergie (mode Lounge)

*Statut : brouillon.*

| Champ | Contenu |
|---|---|
| **Acteur principal** | Système |
| **Objectif** | Éteindre progressivement les étoiles quand personne n'intervient, pour économiser l'énergie. |
| **Déclencheur** | Le délai d'inactivité est écoulé. |
| **Préconditions** | Starlight est en mode Lounge. L'économie d'énergie est activée. L'ambiance courante n'est pas marquée « ne jamais éteindre automatiquement ». |

## Principe

- **Inactivité** : sans capteur de présence, c'est le temps écoulé depuis la dernière demande d'un Convive (ambiance, extinction). Toute demande remet la temporisation à zéro.
- **Délai** : paramétrable par l'Administrateur.
- **Avertissement** : sans capteur de présence, Starlight demande d'abord au Convive de **confirmer sa présence** (alerte « confirmez votre présence ») avant de commencer à éteindre. La confirmation est n'importe quelle demande du Convive. Si un capteur de présence existe un jour (ID-14), il remplace cette alerte : la présence détectée remet la temporisation à zéro.
- **Extinction** : si personne ne confirme pendant le **préavis** (durée paramétrable), les lumières baissent **progressivement** jusqu'à l'extinction.
- **Garde-fous** :
  - un **interrupteur général** active ou coupe l'économie d'énergie ;
  - une option par ambiance, **« ne jamais éteindre automatiquement »**, par exemple pour une veilleuse ;
  - les étoiles **en manuel** (UC-ADM-05) ne sont jamais touchées.
- Elle n'a lieu qu'en mode Lounge : le mode Stream ne s'éteint jamais seul.

## Scénario nominal

1. Le Système mesure le temps écoulé depuis la dernière demande d'un Convive.
2. Le délai est écoulé : Starlight alerte le Convive (« confirmez votre présence ») ; les étoiles ne changent pas encore.
3. Si le Convive confirme pendant le préavis, la temporisation repart de zéro (A1).
4. Sinon, à la fin du préavis, le Système lance la séquence d'extinction progressive sur les étoiles du mode Lounge : les étoiles baissent progressivement jusqu'à l'extinction.
5. Starlight consigne dans le journal : acteur « Système », motif « inactivité ».
6. Les étoiles restent éteintes jusqu'à une demande d'un Convive (UC-CON-01 ou UC-CON-02).

## Scénarios alternatifs

- **A1, demande d'un Convive pendant le préavis ou pendant la séquence** : pendant le préavis, elle confirme la présence et la temporisation repart de zéro ; pendant la séquence, elle l'interrompt. « Off » éteint tout de suite (UC-CON-02, A4) ; une ambiance sélectionnée s'affiche (UC-CON-01). La temporisation repart de zéro.
- **A2, ambiance courante marquée « ne jamais éteindre »** : le décompte ne démarre pas.
- **A3, interrupteur général coupé** : aucune extinction automatique.
- **A4, étoile en manuel** : non touchée ; elle reste dans son effet (UC-ADM-05).
- **A5, étoile injoignable** : les autres étoiles s'éteignent, la défaillance est consignée (QO-14).
- **A6, changement de mode** : au passage en Stream, l'économie d'énergie s'arrête et la temporisation est réinitialisée.
- **A7, ambiance « Off » déjà courante** : rien à éteindre, le décompte ne démarre pas.

## Postconditions

- Les étoiles du mode Lounge sont éteintes, ou la séquence a été interrompue par une demande.
- Le journal indique l'acteur « Système » et le motif.

## Points non tranchés

- **Ambiance courante pendant l'économie d'énergie** : proposé qu'elle soit conservée, pour qu'une seule demande du Convive (même pour la même ambiance) rallume les étoiles. UC-CON-01 dit qu'une ambiance déjà courante ne change rien : il faut préciser que, pendant l'économie d'énergie, la demande rallume (QO-61).
- **Session d'édition ouverte** : proposé qu'elle compte comme une activité (pas d'extinction automatique pendant l'édition) (QO-61).
- **Durée de la séquence d'extinction et du préavis** : proposé qu'elles soient paramétrables, comme le délai (QO-61).
- **Forme de l'alerte** « confirmez votre présence » : elle dépend des actionneurs du Convive (bouton, téléphone, télécommande, QO-11). Avec un simple bouton sans écran, proposé que l'alerte soit visuelle (par exemple une pulsation des lumières) (QO-61).

## Questions liées

QO-11, QO-13, QO-14, QO-61
