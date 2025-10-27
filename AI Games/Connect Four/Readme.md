# AI Connect Four Game

A sophisticated implementation of the Connect Four game featuring an intelligent AI opponent using the Minimax algorithm with Alpha-Beta pruning.

## Overview

This Connect Four implementation provides a graphical interface using Tkinter where players compete against an AI that uses advanced game theory concepts to make strategic decisions.

## Features

- Clean and intuitive graphical user interface
- Intelligent AI opponent using Minimax with Alpha-Beta pruning
- Position evaluation heuristics
- Move validation
- Win detection in all directions
- Automatic game state management
- Draw detection

## Technical Details

### Game Architecture

The game is built with object-oriented programming principles and consists of several key components:

1. **Board Representation**:
   - 6x6 grid (ROWS x COLUMNS)
   - Matrix-based board state tracking
   - Efficient move validation

2. **User Interface**:
   - Built with Tkinter
   - Column selection buttons
   - Visual piece placement
   - Game state messages

3. **AI Implementation**:
   - Minimax algorithm with Alpha-Beta pruning
   - Sophisticated position evaluation
   - Pattern-based scoring system
   - Look-ahead depth of 4 moves

### AI Strategy

The AI uses a complex evaluation function that considers:

1. Horizontal, vertical, and diagonal patterns
2. Center column control preference
3. Blocking opponent's winning moves
4. Creating winning opportunities

```python
def evaluate_window(window, piece):
    # Scoring system:
    # Four in a row: 100 points
    # Three in a row with space: 10 points
    # Two in a row with spaces: 5 points
    # Blocking opponent's three: -80 points
```

### Position Scoring

The game evaluates positions by analyzing:
- Center column control
- Connected pieces
- Potential winning sequences
- Blocking positions

## How to Play

1. Run the game:
   ```bash
   python Connect_Four.py
   ```
2. The game window will appear with an empty grid
3. Click on the column numbers (1-7) to drop your piece
4. You play as 'X' and the computer plays as 'O'
5. Take turns dropping pieces
6. Connect four pieces horizontally, vertically, or diagonally to win
7. The game automatically detects wins and draws

## Game Complexity

Connect Four has interesting computational properties:

- Perfect solution: First player can force a win
- Game-tree complexity: approximately 4.5 × 10¹²
- Branching factor: Maximum 7 moves per turn
- State-space complexity: Around 4.5 × 10⁴²
- Solved game: Optimal play leads to first player victory

## AI Decision Making

The AI uses Minimax with Alpha-Beta pruning to:
1. Look ahead several moves
2. Evaluate potential board positions
3. Choose the optimal move
4. Block player's winning sequences
5. Set up its own winning possibilities

```python
def minimax(board, depth, alpha, beta, maximizingPlayer):
    # Implementation combines:
    # - Alpha-beta pruning for efficiency
    # - Position evaluation
    # - Look-ahead depth of 4
    # - Win detection
```

## Dependencies

- Python 3.x
- Tkinter (usually comes with Python)
- math module (standard library)
- random module (standard library)

## Screenshots

![ScreenShot1](https://github.com/Jeba-02/AI/blob/main/AI%20Games/Connect%20Four/Screenshot%202025-10-25%20215754.png)
![ScreenShot2](https://github.com/Jeba-02/AI/blob/main/AI%20Games/Connect%20Four/Screenshot%202025-10-25%20215847.png)


## Future Enhancements

Possible improvements that could be added:
1. Adjustable AI difficulty levels
2. Move animation
3. Game statistics tracking
4. Undo/redo functionality
5. Two-player mode
6. Custom board sizes
7. AI vs AI mode for analysis
8. Opening book implementation

