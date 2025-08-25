# Tic-Tac-Toe

A Python command-line tic-tac-toe game with AI opponents of varying difficulty levels.

## Features

- **Multiple Game Modes**: Choose between Human vs Human or Human vs AI
- **AI Difficulty Levels**:
  - **Easy**: Random moves (great for beginners) [default]
  - **Medium**: 70% optimal moves, 30% random (challenging but beatable)
  - **Hard**: Unbeatable AI using minimax algorithm
- **Clean Interface**: Clear terminal display with automatic screen clearing
- **Exit Anytime**: Type 'exit' to quit at any menu or during gameplay
- **User-Friendly**: Default options and streamlined menu navigation
- **Dependency Checking**: Automatic Python version validation on startup

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/tchung1970/tic-tac-toe.git
   cd tic-tac-toe
   ```

2. Run the game (requires Python 3.6+):
   ```bash
   python tic_tac_toe.py
   ```

## How to Play

### Game Modes

1. **Human vs AI** [default]: Play against the computer
2. **Human vs Human**: Two players take turns

### AI Difficulty Levels

When playing against AI, choose from:

1. **Easy** [default]: AI makes random moves (perfect for beginners)
2. **Medium**: AI plays optimally 70% of the time (challenging but beatable)
3. **Hard**: Unbeatable AI using minimax algorithm (perfect play)

### Controls

- Enter numbers **1-9** to place your mark on the board
- Press **Enter** to select default options
- Type **'exit'** to quit at any time

### Board Layout

```
   |   |   
 1 | 2 | 3 
___|___|___
   |   |   
 4 | 5 | 6 
___|___|___
   |   |   
 7 | 8 | 9 
   |   |   
```

## Game Rules

- Player X always goes first
- Win by getting three marks in a row (horizontal, vertical, or diagonal)
- Game ends in a tie if all positions are filled without a winner

## Technical Details

### Architecture

- **Object-oriented design** with a single `TicTacToe` class
- **Board representation**: 9-element list for the 3x3 grid
- **AI implementation**: Minimax algorithm for optimal play
- **Input validation**: Ensures all moves are valid
- **Dependency checking**: Python version validation (3.6+ required)
- **Cross-platform screen clearing**: Uses `os.system('clear')` for clean interface

### AI Strategy

- **Easy**: Uses `random.choice()` for move selection
- **Medium**: Combines optimal moves (70%) with random moves (30%)
- **Hard**: Full minimax implementation with perfect play

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Contributing

Feel free to fork this project and submit pull requests for improvements!

## Author

Thomas Chung  
Created: August 25, 2025

## License

This project is open source and available under the MIT [LICENSE](LICENSE).