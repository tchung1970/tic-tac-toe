# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python-based command-line tic-tac-toe game. The game features a simple text interface where two players take turns placing X's and O's on a 3x3 grid.

## Architecture

The game is implemented as a single `TicTacToe` class in `tic_tac_toe.py` with the following key components:

- **Board representation**: 9-element list representing the 3x3 grid
- **Game state management**: Tracks current player, board state, and game status
- **Display system**: ASCII art board display with position numbers for user reference
- **Input validation**: Ensures moves are valid (position 1-9, empty cell)
- **Win detection**: Checks all possible winning combinations (rows, columns, diagonals)
- **Game flow**: Main game loop handling player turns and game end conditions

## Common Commands

```bash
# Run the game
python tic_tac_toe.py

# Run with Python 3 explicitly
python3 tic_tac_toe.py
```

## Game Rules

- Players alternate turns (X goes first)
- Enter numbers 1-9 to place your mark in the corresponding position
- Win by getting three marks in a row (horizontal, vertical, or diagonal)
- Game ends in a tie if all positions are filled without a winner