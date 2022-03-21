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

# 2.Chess Game
## Pieces
Piece|Black|White
---|---|---
King|KI|ki
Queen|QU|qu
Rook|R1 R2|r1 r2
Bishop|B1 B2|b1 b2
Knight|N1 N2|n1 n2
Pawn|P1 P2 P3 P4 P5 P6 P7 P8|p1 p2 p3 p4 p5 p6 p7 p8

## Commands
---
### 1)initalize
Arguments: This command does not take any arguments.

Description: This command load the pieces to the board.

Output: OK

### 2)showmoves
Arguments: piece

Description: Lists the possible target positions of the given piece can move. The order of
the positions will be from a to h and from 1 to 8 increasing, i.e. a3 will be printed before a5
and a7 will be printed before b2.

Output: position1 position2 position3...

Output on Failure: FAILED

### 3)move
Arguments: piece position

Description: Moves the given piece to the given position. The operation should fail if the
move is not valid.
Output on successful operation: OK

Output on Failure: FAILED

### 4)print
Arguments: This command does not take any arguments.

Description: Prints the status of the board to the console.

Output: The output will be 8 lines of 8 characters, where the rows will be 8 to 1 from
top to bottom and the columns will be a to h from left to right. Pieces will be represented
with their corresponding letters and empty squares will be represented as a single whitespace
character.

### 5)exit
Arguments: This command does not take any arguments.

Description: Instructs the program to exit.

Output: This command does not output any information to the console.

### Execute your code on server use the following command in your terminal:
python3 chess.py input.txt

