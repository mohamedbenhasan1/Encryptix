# Tic-Tac-Toe AI

This project implements an AI agent that plays the classic game of Tic-Tac-Toe against a human player. The AI uses the Minimax algorithm to make optimal moves, making it unbeatable.

## Features

- Play Tic-Tac-Toe against an unbeatable AI.
- The AI uses the Minimax algorithm to determine the best possible move.
- Simple command-line interface.

## Requirements

- Python 3.x

## Installation

 . Clone the repository or download the script:

```bash
git clone https://github.com/mohamedbenhasan1/Encryptix/Task_3.git
```
No additional libraries are required.
## Usage
Run the script:
```bash
cd Task_3
python game.py
```
Follow the on-screen instructions to make your move by entering a number (1-9) corresponding to the board position:
```bash
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9

The AI will then make its move, and the updated board will be displayed.
The game continues until there is a winner or a draw.
```
## How It Works
- The board is represented as a list of 9 elements.
- The human player is 'X' and the AI is 'O'.
- The minimax function recursively evaluates the board to determine the best possible move for the AI.
- The game checks for wins, losses, and draws after each move.
## Author
Mohamed Benhasan
