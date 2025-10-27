# AI TicTacToe Game

A sophisticated implementation of the classic TicTacToe game featuring an unbeatable AI opponent using the Minimax algorithm.

## Overview

This TicTacToe implementation is built using Python and Tkinter for the GUI. It provides a challenging gaming experience where players face off against an AI opponent that makes optimal moves using the Minimax algorithm.

## Features

- Clean and intuitive graphical user interface
- Unbeatable AI opponent using Minimax algorithm
- Real-time move validation
- Automatic win/draw detection
- Easy game reset functionality

## Technical Details

### Game Architecture

The game is built with object-oriented programming principles and consists of several key components:

1. **Game Board**: 
   - 3x3 grid implemented using Tkinter buttons
   - Each cell can hold either 'X' (player) or 'O' (computer)

2. **Player Interaction**:
   - Players make moves by clicking on empty cells
   - Invalid moves are automatically prevented
   - Visual feedback for player and computer moves

3. **AI Implementation**:
   - Uses the Minimax algorithm for computer moves
   - Evaluates all possible future game states
   - Makes optimal decisions to either win or force a draw

### AI Algorithm

The game implements the Minimax algorithm, which:

1. Explores all possible game states
2. Assigns scores to each state:
   - +1 for computer win
   - -1 for player win
   - 0 for draw
3. Chooses the move that maximizes the computer's chances of winning while minimizing the player's chances

```python
def minimax(self, depth, is_maximizing):
    # Base cases: check for terminal states
    if self.check_winner(self.computer): return 1
    if self.check_winner(self.player): return -1
    if self.is_draw(): return 0

    # Recursive cases
    if is_maximizing:
        return max(self.minimax(depth + 1, False) for move in self.available_moves())
    else:
        return min(self.minimax(depth + 1, True) for move in self.available_moves())
```

## How to Play

1. Run the game using Python:
   ```bash
   python tik_tak_toe.py
   ```
2. The game window will appear with an empty 3x3 grid
3. You play as 'X' and the computer plays as 'O'
4. Click on any empty cell to make your move
5. The computer will respond with its move after 500ms
6. The game continues until there's a winner or a draw
7. A message box will announce the game result
8. The game automatically resets after each round

## Game Complexity

Despite its simple rules, TicTacToe has interesting computational complexity:

- Total possible board positions: 3⁹ = 19,683
- Unique board positions: 765 (accounting for symmetry)
- Maximum game length: 9 moves
- Branching factor: Starts at 9 and decreases each turn

The Minimax algorithm explores this game tree to make optimal decisions, ensuring the computer player is unbeatable.

## Dependencies

- Python 3.x
- Tkinter (usually comes with Python installation)
- math module (standard library)

## Screenshots

![ScreenShot1](https://github.com/Jeba-02/AI/blob/main/AI%20Games/TikTacToe/Screenshot%202025-10-25%20215954.png)
![ScreenShot2](https://github.com/Jeba-02/AI/blob/main/AI%20Games/TikTacToe/Screenshot%202025-10-25%20220003.png)

## Future Enhancements

Possible improvements that could be added:
1. Difficulty levels
2. Score tracking
3. Game history
4. Animation effects
5. Sound effects

