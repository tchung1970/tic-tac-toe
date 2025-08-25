# Tic-Tac-Toe

A Python command-line tic-tac-toe game with AI opponents of varying difficulty levels.

## Features

- **Multiple Game Modes**: Choose between Human vs Human or Human vs AI
- **AI Difficulty Levels**:
  - **Easy**: Random moves (great for beginners)
  - **Medium**: 70% optimal moves, 30% random (challenging but beatable)
  - **Hard**: Unbeatable AI using minimax algorithm
- **Clean Interface**: Clear terminal display with intuitive controls
- **Exit Anytime**: Type 'exit' to quit at any menu or during gameplay
- **User-Friendly**: Default options and clear instructions throughout

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

1. **Easy** [default]: AI makes random moves
2. **Medium**: AI plays optimally 70% of the time
3. **Hard**: Unbeatable AI using minimax algorithm

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
- **Cross-platform**: Uses appropriate screen clearing for different operating systems

### AI Strategy

- **Easy**: Uses `random.choice()` for move selection
- **Medium**: Combines optimal moves (70%) with random moves (30%)
- **Hard**: Full minimax implementation with perfect play

## Requirements

- Python 3.6 or higher
- No external dependencies required

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to fork this project and submit pull requests for improvements!

## Author

Created with assistance from Claude Code (claude.ai/code)