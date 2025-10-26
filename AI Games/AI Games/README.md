🎮 Python AI Game Collection

A collection of three classic board games — Tic-Tac-Toe, Connect Four, and Chess — each featuring a graphical interface and a computer opponent powered by the Minimax algorithm with Alpha-Beta pruning (for efficiency).

Each game allows a human player to compete against an unbeatable or strong AI opponent.

🧩 Game 1: Tic-Tac-Toe (Tkinter GUI)
🧠 Overview

A simple yet strategic Tic-Tac-Toe game built with Tkinter, where the player (“X”) faces off against a perfect AI opponent (“O”). The AI uses the Minimax algorithm, ensuring that it will never lose.

⚙️ Features

Graphical 3x3 grid using Tkinter buttons

Smart AI that calculates the best possible move

Win, lose, or draw detection

Automatic game reset after each round

🏗️ How It Works

The board is a 3×3 grid of buttons representing 9 possible positions.

The player clicks a square to place their “X”.

The computer then evaluates all possible outcomes using Minimax and makes the optimal move.

The game checks for:

Player or computer wins

Draws (no moves left)

Displays a popup result and restarts automatically.

▶️ Run
python tic_tac_toe.py

🔵 Game 2: Connect Four (Tkinter GUI)
🧠 Overview

A GUI-based Connect Four game built with Tkinter, where you compete against an AI that uses Minimax with Alpha-Beta pruning to simulate several moves ahead and pick the most strategic column.

⚙️ Features

6×7 interactive grid

Player vs AI gameplay

AI with deep search for optimal move decisions

Colored pieces (“X” in red for player, “O” in blue for computer)

Win detection (horizontal, vertical, and diagonal)

Auto reset after win/draw

🏗️ How It Works

The player selects a column to drop their piece.

The AI evaluates all possible future board states up to a fixed depth using Minimax.

Scoring is based on how many consecutive pieces are connected and how close they are to forming four-in-a-row.

Alpha-Beta pruning reduces unnecessary calculations for efficiency.

The game visually updates after every move and declares a winner or draw.

▶️ Run
python connect_four.py

♟️ Game 3: Chess (Pygame GUI)
🧠 Overview

A fully functional Chess game built using Pygame and python-chess, allowing a player to face off against a computer opponent that uses Minimax with Alpha-Beta pruning.
The AI evaluates board positions using piece values and simple heuristics for a challenging experience.

⚙️ Features

Beautiful 8×8 chessboard rendered with Unicode chess pieces

Highlighted legal moves and selections

Player vs AI gameplay (Player = White, Computer = Black)

Real-time move validation using python-chess

Automatic detection of checkmate, stalemate, and draws

Game result screen after each match

🏗️ How It Works

The player selects and moves pieces with mouse clicks.

The AI uses Minimax with Alpha-Beta pruning to simulate moves up to a search depth.

Each position is evaluated based on:

Material balance (piece values)

Game state (checkmate, stalemate, etc.)

The game displays the winner and automatically closes after showing the result screen.

▶️ Run
python chess_ai.py

🧠 About the AI (Minimax + Alpha-Beta Pruning)

All three games implement variants of the Minimax algorithm, a recursive decision-making technique used in game theory and AI.

The player is the minimizing agent (tries to minimize AI’s score).

The AI is the maximizing agent (tries to maximize its score).

Alpha-Beta pruning improves efficiency by cutting off branches that cannot possibly affect the final decision.

Simplified Logic
def minimax(state, depth, alpha, beta, maximizing):
    if terminal or depth == 0:
        return evaluate(state)

    if maximizing:
        for each move:
            score = minimax(next_state, depth-1, alpha, beta, False)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return alpha
    else:
        for each move:
            score = minimax(next_state, depth-1, alpha, beta, True)
            beta = min(beta, score)
            if beta <= alpha:
                break
        return beta

🧰 Requirements

Python 3.8+

Tkinter (included with Python)

Pygame

python-chess

Install Dependencies
pip install pygame python-chess

📂 File Structure
├── tic_tac_toe.py        # Tic-Tac-Toe with Minimax AI (Tkinter)
├── connect_four.py        # Connect Four with Minimax + Alpha-Beta (Tkinter)
├── chess_ai.py            # Chess with Minimax + Alpha-Beta (Pygame)
├── README.md              # Documentation

🏁 Summary
Game	Interface	AI Algorithm	Difficulty	Library
Tic-Tac-Toe	Tkinter	Minimax	Unbeatable	tkinter
Connect Four	Tkinter	Minimax + Alpha-Beta	Strong	tkinter
Chess	Pygame	Minimax + Alpha-Beta	Challenging	pygame + python-chess
👨‍💻 Author

Developed in Python for educational purposes to demonstrate:

Game AI logic

Recursive search algorithms

GUI programming with Tkinter & Pygame
