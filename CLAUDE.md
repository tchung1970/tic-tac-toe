# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python-based command-line tic-tac-toe game with AI opponents. The game features a clean text interface with multiple game modes and AI difficulty levels.

## Architecture

The game is implemented as a single `TicTacToe` class in `tic_tac_toe.py` with the following key components:

### Core Game Logic
- **Board representation**: 9-element list representing the 3x3 grid
- **Game state management**: Tracks current player, board state, game mode, and AI difficulty
- **Display system**: ASCII art board display with position numbers for user reference
- **Input validation**: Ensures moves are valid (position 1-9, empty cell)
- **Win detection**: Checks all possible winning combinations (rows, columns, diagonals)
- **Game flow**: Main game loop handling player turns and game end conditions

### AI System
- **Easy AI**: Makes completely random moves using `random.choice()`
- **Medium AI**: 70% optimal moves, 30% random moves for balanced gameplay
- **Hard AI**: Unbeatable minimax algorithm implementation with perfect play
- **AI move delay**: Simulated thinking time with visual feedback

### User Interface
- **Game mode selection**: Human vs AI (default) or Human vs Human
- **AI difficulty selection**: Easy (default), Medium, or Hard
- **Screen clearing**: Automatic terminal clearing using `os.system('clear')`
- **Exit functionality**: Type 'exit' at any menu or during gameplay
- **Default options**: Streamlined navigation with Enter key shortcuts

## Common Commands

```bash
# Run the game
python tic_tac_toe.py

# Run with Python 3 explicitly
python3 tic_tac_toe.py
```

## Dependencies and System Requirements

- **Python version**: 3.6+ required (automatically checked on startup)
- **Standard library only**: Uses `random`, `time`, `os`, `sys` modules
- **No external dependencies**: No pip install required
- **Cross-platform**: Works on macOS, Linux, and Windows

## Game Rules and Controls

### Basic Rules
- Human player is X, AI is O (in AI mode)
- Players alternate turns (X goes first)
- Win by getting three marks in a row (horizontal, vertical, or diagonal)
- Game ends in a tie if all positions are filled without a winner

### Controls
- Enter numbers 1-9 to place your mark in the corresponding position
- Press Enter to select default options in menus
- Type 'exit' to quit at any time (menus or gameplay)

## Development Notes

### Key Functions
- `check_dependencies()`: Validates Python version and dependencies
- `get_best_move()`: AI move selection with difficulty-based logic
- `_get_optimal_move()`: Minimax algorithm implementation
- `minimax()`: Recursive minimax with alpha-beta logic
- `main()`: Entry point with menu system

### Code Style
- Uses `os.system('clear')` for cross-platform screen clearing
- F-string formatting for dynamic text
- List comprehension for board operations
- Object-oriented design with single class