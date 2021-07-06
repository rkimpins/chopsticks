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


# Solving the Game

## Complexity

Before we get started solving chopsticks, let us take a look at the complexity of the game. This will be important for determing which methods will most likely be successful for solving this game.

### State-Space Complexity

Each hand is limited to 0 to 4 active fingers for the median player. Rather simply, if we factor in whose player's turn it is, we get 2 x 5 x 5 x 5 x 5 = 1250. This is a very small state-space, suggesting we can easily solve this with minimax search or some other brute force search method. If we let F = the number of fingers each hand has, H = the number of hands a player has, and P = the number of players, we get the formula P x (F ^ (H x P)). Seeing as this is exponential, solving this game for larger versions becomes computationally expensive quickly.

We can reduce state-space complexity by recognizing that a hand of (1, 2) is effectively the same as a hand (2, 1). This splits our complexity roughly in half, but I will need to check this more thoroughly.

### Branching Factor

This isn't hugely important for our purposes, but I think it would be fun to calculate. First we must consider touching opponent hands. There are only 4 options here: Left to Left, Left to Right, Right to Left, Right to Right. We must also consider switching. If we think of it as moving fingers from one hand to the other, we realize we have at most 4 future states. Consider the case where we have 4 fingers on one hand. We can move either 1, 2, 3, or 4 fingers over. With this in mine, we have a worst-case branching factor of 8. Now, if we consider the general case of F, H, P, we get H x (H x (P - 1)) + (F - 1) which is approximetly H^2 x P + F.

### Average Game Length and Infintie Loops

As the header has spoiled, there are infinite loops in this game. I know this from general experience playing one, but I will show an example loop to prove it. The move notation I will use is PiHjPkTl: Player i uses Hand j to strike Player k on their Target hand l. This works for any combination of hands and players, but for the simpler case of two players and two hands, I will use PiHjTk, since we know which opponent we are striking. For the case of splitting, I will simply put PiSH1H2: Player i is Splitting and their new state is Hand 1 Hand 2.

(2 3) (2 3) ==P1H2T1=>
(2 3) (0 3) ==P2H2T1=>
(0 3) (0 3) ==P1S21==>
(2 1) (0 3) ==P2S21==>
(2 1) (2 1) ==P1H1T2=>
(2 1) (2 3) ==P2H1T2=>
(2 3) (2 3)

As we can see, we have a 6 move cycle, and the turn is once again player 1's. I don't know if this is the shortest cycle for this game, but it would be interesting to find a shorter one.

It is worth considering ways to avoid infinite loops. We could implement a rule that the same move from the same state by the same player can not be made twice. We could also put a hard cap on the number of turns and call it a draw after that. 

