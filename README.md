# Introduction

Chopsticks is a schoolyard game I learned in junior high and used to play with my friends and family all the time. I recently realized that I could use my new found computer science power to explore some of the underlying structure of this game and more importantly have some fun with it.

# The Rules

Chopsticks is a game played with just your hands. Each player starts with their pointer finger extended on each hands. They take turns using one of their hands to touch one of the opponents hands, adding the value of their hand to the opponent hands (without changing their own value). Should a hand go past 5, it modulos. If a hand goes exactly to 5, that hand is temporarily dead. If both of your hands are dead, you lose. Players can split their living hand to revive a dead hand by tapping their hands together, and can more generally freely exchange values between hands, even opting to kill one of their own hands (although this is controversial in some circles. I will call it the suicide rule). The only exception is a player can't split their hand in such a way that the values on their hands swap.

# Examples

Until I have time to make pictures, I will represent a game with:

(p1 left hand, p1 right hand) (p2 left hand, p2 right hand) => (1, 1) (1, 1)

Valid splits would be:

(4, 0) => (2, 2)
(3, 1) => (2, 2)
(4, 4) => (3, 0) [depending on if the suicide rule is used]

But not

(1, 2) => (2, 1)
(1, 0), => (0, 1)




