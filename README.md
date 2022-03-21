# Python-Introduction-To-Programming-I
# 1.Feeding the Rabbit Game
## HOW TO PLAY
***
In this assignment, you will implement a game called ’Feeding the Rabbit Game’. In this
game, the rabbit which is placed in a board will move according to the commands and collect
points according to the food it eats. The user plays the game by moving the the rabbit
denoted by * to horizontally or vertically adjacent cells. The user earns/lose points if he/she
move the rabbit to a cell that contains Carrot (C), Apple (A) or Meat (M). The game is over
and the rabbit cannot move any more if user can move the rabbit to a cell that contains
Poison (P). The board may contain Walls (W). The rabbit cannot break the wall, and if the
rabbit is in the cell next to the wall, it remains in the cell where it is, even if commanded to
move towards the wall. The user moves the rabbit (*) by giving directions to the computer
about which direction it is to be moved. There are four allowed moves: Right (R), Left (L),
Up (U), and Down (D). The rabbit can move one cell at a time.

If the cell that the rabbit is trying to move is already occupied, i.e., if there is another character
there, the rabbit replaces those character with the * character. Moreover, the rabbit can’t
get out of the board or move into walls. For example, if the rabbit is on the far left and is
asked to move to the left, he will not move to left any more. This situation is the same for
all directions.

In this game, the user will determine the size of the map such as 4x8, 5x4, 6x6 or so on,
manually enter the elements into the cells and manually enter directions of movements as a
list as exemplified in Section 2.
Some rules are listed for scoring as follow:

• Rabbit earns 10 points if rabbit eats carrot

• Rabbit earns 5 points if rabbit eats apple

• Rabbit loses 5 points if rabbit eats meats

• Rabbit dies if rabbit eats poison



### Example board:

X W X C X

A W X A X

C X X W P

W X X X X

X * X W X

Symbols on the board and their meanings, *R=Rabbit, C=Carrot, A=Apple, P=Poison, M=Meat,*
*W=Wall and X=Empty*

### Example
Please enter feeding map as a list:

[[’W’, ’X’, ’W’, ’C’, ’X’], [’A’, ’X’, ’X’, ’A’, ’W’], [’C’, ’X’, ’X’,
’X’, ’P’], [’X’, ’X’, ’X’, ’X’, ’X’], [’X’, ’*’, ’X’, ’X’, ’X’]]

Please enter direction of movements as a list:

[’U’,’U’,’L’,’U’,’L’]

Your board is:

W|X|W|C|X
---|---|---|---|---
A|X|X|A|W
C|X|X|X|P
X|X|X|X|X
X|*|X|X|X

Your output should be like this:
W|X|W|C|X
---|---|---|---|---
*|X|X|A|W
X|X|X|X|P
X|X|X|X|X
X|X|X|X|X

Your score is: 15


### Execute your code on server use the following command in your terminal:
*python3 feedingTheRabbitGame.py*

# 2.Feeding-the-Rabbit-Game
