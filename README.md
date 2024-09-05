# Connect4
A summer project to create a connect 4 AI in a manner similar to AlphaGo Zero

# Resources
* Rules for Connect 4: https://rulesofplaying.com/connect-4-rules/
* Possible Environment: https://gymnasium.farama.org/tutorials/gymnasium_basics/environment_creation/

# Basics
The basics of how this AI will function, mainly for my own reference

## The Game
Played on a 6x7 board, with each element belong to red, black, or no-one. Each player gets 21 checkers, with red(?) starting. Pieces are played until there are four of the same pieces in a row along the horizontal, vertical, or diagonal. If all players run out of pieces without four in a row, then the game is a draw. Pieces "fall down" a column, stopping when they hit either another piece or the bottom of the board.

## The AI
### Action Space
At each step, the AI chooses one of the seven columns (if possible) to place a piece in. (Discrete 7)

### Observation Space
The AI can observe the entire board state, a 6x7 matrix with three possible positions. (Box low=-1, high=1, shape=(6, 7))
