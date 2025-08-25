import random
import time
import os

class TicTacToe:
    def __init__(self, ai_mode=False, difficulty='hard'):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.ai_mode = ai_mode
        self.difficulty = difficulty
        self.human_player = 'X'
        self.ai_player = 'O'
    
    def display_board(self):
        print("\n   |   |   ")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("___|___|___")
        print("   |   |   ")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("___|___|___")
        print("   |   |   ")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        print("   |   |   \n")
        
        print("Position numbers:")
        print("   |   |   ")
        print(" 1 | 2 | 3 ")
        print("___|___|___")
        print("   |   |   ")
        print(" 4 | 5 | 6 ")
        print("___|___|___")
        print("   |   |   ")
        print(" 7 | 8 | 9 ")
        print("   |   |   \n")
    
    def make_move(self, position):
        if position < 1 or position > 9:
            return False
        
        position -= 1
        
        if self.board[position] != ' ':
            return False
        
        self.board[position] = self.current_player
        return True
    
    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        
        for combo in winning_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' '):
                return self.board[combo[0]]
        
        return None
    
    def is_board_full(self):
        return ' ' not in self.board
    
    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def get_available_moves(self):
        return [i + 1 for i, cell in enumerate(self.board) if cell == ' ']
    
    def minimax(self, board, depth, is_maximizing):
        winner = self.check_winner()
        
        if winner == self.ai_player:
            return 1
        elif winner == self.human_player:
            return -1
        elif self.is_board_full():
            return 0
        
        if is_maximizing:
            max_eval = -float('inf')
            for move in self.get_available_moves():
                temp_board = self.board.copy()
                self.board[move - 1] = self.ai_player
                eval_score = self.minimax(board, depth + 1, False)
                self.board = temp_board
                max_eval = max(max_eval, eval_score)
            return max_eval
        else:
            min_eval = float('inf')
            for move in self.get_available_moves():
                temp_board = self.board.copy()
                self.board[move - 1] = self.human_player
                eval_score = self.minimax(board, depth + 1, True)
                self.board = temp_board
                min_eval = min(min_eval, eval_score)
            return min_eval
    
    def get_best_move(self):
        available_moves = self.get_available_moves()
        
        if self.difficulty == 'easy':
            return random.choice(available_moves)
        elif self.difficulty == 'medium':
            # 70% chance for optimal move, 30% random
            if random.random() < 0.7:
                return self._get_optimal_move()
            else:
                return random.choice(available_moves)
        else:  # hard
            return self._get_optimal_move()
    
    def _get_optimal_move(self):
        best_move = None
        best_value = -float('inf')
        
        for move in self.get_available_moves():
            temp_board = self.board.copy()
            self.board[move - 1] = self.ai_player
            move_value = self.minimax(temp_board, 0, False)
            self.board = temp_board
            
            if move_value > best_value:
                best_value = move_value
                best_move = move
        
        return best_move if best_move else random.choice(self.get_available_moves())
    
    def ai_move(self):
        print("AI is thinking...")
        time.sleep(1)
        move = self.get_best_move()
        self.make_move(move)
        print(f"AI chooses position {move}")
    
    def play(self):
        print("Welcome to Tic Tac Toe!")
        if self.ai_mode:
            difficulty_text = self.difficulty.capitalize()
            print(f"You are X, AI is O ({difficulty_text}). Enter a number 1-9 to place your mark, or 'exit' to quit.")
        else:
            print("Players will alternate turns. Enter a number 1-9 to place your mark, or 'exit' to quit.")
        
        while True:
            self.display_board()
            
            if self.ai_mode and self.current_player == self.ai_player:
                self.ai_move()
            else:
                if self.ai_mode:
                    user_input = input(f"Your move (1-9) or 'exit': ").strip().lower()
                else:
                    user_input = input(f"Player {self.current_player}, enter your move (1-9) or 'exit': ").strip().lower()
                
                if user_input == 'exit':
                    print("Thanks for playing!")
                    break
                
                try:
                    position = int(user_input)
                except ValueError:
                    print("Please enter a valid number between 1 and 9, or 'exit' to quit.")
                    continue
                
                if not self.make_move(position):
                    print("Invalid move! Position already taken or out of range.")
                    continue
            
            winner = self.check_winner()
            if winner:
                self.display_board()
                if self.ai_mode:
                    if winner == self.human_player:
                        print("You win!")
                    else:
                        print("AI wins!")
                else:
                    print(f"Player {winner} wins!")
                break
            
            if self.is_board_full():
                self.display_board()
                print("It's a tie!")
                break
            
            self.switch_player()


def main():
    os.system('clear')
    print("Choose game mode:")
    print("1. Human vs AI [default]")
    print("2. Human vs Human")
    
    while True:
        choice = input("Enter 1, 2, or press Enter for [default] ('exit' to quit): ").strip().lower()
        if choice == 'exit':
            print("Thanks for playing!")
            return
        elif choice == '1' or choice == '':
            # AI difficulty selection
            print("\nChoose AI difficulty:")
            print("1. Easy (random moves) [default]")
            print("2. Medium (mostly smart)")
            print("3. Hard (unbeatable)")
            
            while True:
                diff_choice = input("Enter 1, 2, 3, or press Enter for [default] ('exit' to quit): ").strip().lower()
                if diff_choice == 'exit':
                    print("Thanks for playing!")
                    return
                elif diff_choice == '1' or diff_choice == '':
                    difficulty = 'easy'
                    break
                elif diff_choice == '2':
                    difficulty = 'medium'
                    break
                elif diff_choice == '3':
                    difficulty = 'hard'
                    break
                else:
                    print("Please enter 1, 2, 3, or 'exit'.")
            
            game = TicTacToe(ai_mode=True, difficulty=difficulty)
            break
        elif choice == '2':
            game = TicTacToe(ai_mode=False)
            break
        else:
            print("Please enter 1, 2, or 'exit'.")
    
    print()
    game.play()

if __name__ == "__main__":
    main()