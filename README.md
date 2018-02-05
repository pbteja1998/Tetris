## Controls:
- **A --> Move Left**
- **D --> Move Right**
- **S --> Rotate ClockWise**
- **SPACE --> Fall Instantly**
- **ESCAPE --> Quit the game**

1. Score and level will printed below the game everytime they update
1. Score will be printed on terminal at the end of the game
1. Score = Score + 10 if a block falls
1. Score = Score + 100 if a row is filled completely
1. If a row is completely filled, then that row will be deleted
1. There are 11 Levels in total in this game.
1. Speed with which the block falls increases with level of game
1. There are total of 6 different types of blocks each with 4 configurations
1. There are 30 rows and 32 columns

## Conventions:
1. `matrix[i][j] = 0` denotes unfilled block
1. `matrix[i][j] = 1` denotes filled moving block
1. `matrix[i][j] = -1` denoted filled static block that is fixed to the body

## Modularity:
There are 4 modules in this code
1. `base.py` (which is primary module)
1. `block.py`
1. `board.py`
1. `figures.py` (all figures are defined in this module)

## Inheritance:
1. class `Block inherited the following classes:
  `Fig1`, `Fig2`, `Fig3`, `Fig4`, `Fig5`, `Fig6` from the `figures.py` module
1. class `GamePlay` inherited the following classes:
  `Block`, `Board`

## Polymorphism:
  Polymorphism is used in figures.py module
