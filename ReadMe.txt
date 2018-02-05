Controls:
A --> Move Left
D --> Move Right
S --> Rotate ClockWise
SPACE --> Fall Instantly
ESCAPE --> Quit the game

1)Score and level will printed below the game everytime they update
2)Score will be printed on terminal at the end of the game
3)Score = Score + 10 if a block falls
4)Score = Score + 100 if a row is filled completely
5)If a row is completely filled, then that row will be deleted
6)There are 11 Levels in total in this game.
7)Speed with which the block falls increases with level of game
8)There are total of 6 different types of blocks each with 4 configurations
9)There are 30 rows and 32 columns

Conventions:
1)matrix[i][j] = 0 denotes unfilled block
2)matrix[i][j] = 1 denotes filled moving block
3)matrix[i][j] = -1 denoted filled static block that is fixed to the body

Modularity:
There are 4 modules in this code
i)  base.py (which is primary module)
ii) block.py
iii)board.py
iv) figures.py (all figures are defined in this module)

Inheritance:
i)class "Block" inherited the following classes:
  "Fig1","Fig2","Fig3","Fig4","Fig5","Fig6" from the figures.py module
ii)class "GamePlay" inherited the following classes:
  "Block","Board"

Polymorphism:
  Polymorphism is used in figures.py module
