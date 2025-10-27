# AI Chess Game

A Python implementation of Chess with an AI opponent using the Minimax algorithm with Alpha-Beta pruning.

## Overview

This Chess implementation provides a graphical interface using Pygame where players can compete against an AI opponent. The AI uses the Minimax algorithm with Alpha-Beta pruning to make strategic decisions.

## Features

- Full chess rules implementation using the `python-chess` library
- Graphical user interface with Pygame
- Piece movement visualization
- Legal move highlighting
- Intelligent AI opponent
- Game state detection (checkmate, stalemate, insufficient material)
- Move validation
- Unicode chess pieces display

## Technical Details

### Game Architecture

The game is built using several key components:

1. **Board Representation**:
   - Uses the `python-chess` library for game state management
   - 8x8 grid with proper piece placement
   - Unicode symbols for chess pieces

2. **User Interface**:
   - Built with Pygame
   - Visual feedback for selected pieces
   - Highlight of legal moves
   - Clean and intuitive design

3. **AI Implementation**:
   - Minimax algorithm with Alpha-Beta pruning
   - Position evaluation based on piece values
   - Depth-based search (currently set to depth 2)
   - Considers material advantage and checkmate positions

### Piece Values

The AI uses standard chess piece values for evaluation:
```python
piece_values = {
    PAWN: 1,
    KNIGHT: 3,
    BISHOP: 3,
    ROOK: 5,
    QUEEN: 9,
    KING: 0
}
```

### AI Algorithm

The game implements Minimax with Alpha-Beta pruning for efficient decision making:

```python
def minimax(board, depth, alpha, beta, maximizing):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board), None

    # Recursively evaluate positions
    # Uses alpha-beta pruning to reduce search space
    # Returns best move and its evaluation
```

## How to Play

1. Run the game:
   ```bash
   python Chess_Ai.py
   ```
2. You play as White (bottom pieces)
3. Click on a piece to select it
4. Legal moves will be highlighted in green
5. Click on a highlighted square to make your move
6. The AI (Black) will respond automatically
7. Game continues until checkmate or draw

## Game Controls

- Left mouse click to select and move pieces
- Game automatically detects and announces:
  - Checkmate
  - Stalemate
  - Insufficient material
  - 75-move rule
  - Fivefold repetition

## Dependencies

- Python 3.x
- Pygame
- python-chess

To install dependencies:
```bash
pip install pygame python-chess
```

## Game Complexity

Chess has significant computational complexity:

- Approximate game-tree complexity: 10¹²⁰
- Average branching factor: 35
- Typical game length: 40 moves per player
- Evaluation requires consideration of:
  - Material advantage
  - Position control
  - King safety
  - Tactical opportunities

## Screenshots

![ScreenShot1](path_to_chess_start.png)
![ScreenShot2](path_to_chess_midgame.png)


## Future Enhancements

Potential improvements that could be added:
1. Opening book implementation
2. Adjustable AI difficulty levels
3. Position evaluation improvements
4. Move time controls
5. Game save/load functionality
6. Previous move highlighting
7. Move notation display
