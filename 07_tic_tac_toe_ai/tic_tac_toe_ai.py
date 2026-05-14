import time
from player import GeniusComputerPlayer, HumanPlayer, RandomComputerPlayer

class tictactoe:
    def __init__(self):  # Initialize the game board and set the current player
        self.board = [[' ' for _ in range(3)] for _ in range(3)]     # 3x3 board initialized with empty spaces
        self.current_winner = None  # Keep track of the winner!

    def print_board(self):  # Print the current state of the game board
        for row in self.board:
            print('| ' + ' | '.join(row) + ' |')    # Print each row of the board with separators
            
    @staticmethod     # Static method to print the board numbers for reference
    def print_board_nums():  # Print the board with numbers for reference
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]    # Create a board with numbers 0-8 for reference
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
            
    def available_moves(self):  # Return a list of available moves (empty squares)
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    moves.append(i * 3 + j)
        return moves
      
    def empty_squares(self):  # Check if there are any empty squares left
        return ' ' in [square for row in self.board for square in row]
      
    def num_empty_squares(self):  # Return the number of empty squares
        return len(self.available_moves())
      
    def make_move(self, square, letter):  # Make a move on the board
        row = square // 3
        col = square % 3
        if self.board[row][col] == ' ':  # If the square is empty, make the move
            self.board[row][col] = letter
            if self.winner(row, col, letter):  # Check if this move wins the game
                self.current_winner = letter
            return True
        return False
      
    def winner(self, row, col, letter):  # Check if the current move wins the game
        # Check the row
        if all([self.board[row][i] == letter for i in range(3)]):
            return True
        # Check the column
        if all([self.board[i][col] == letter for i in range(3)]):
            return True
        # Check diagonals
        if row == col and all([self.board[i][i] == letter for i in range(3)]):
            return True
        if row + col == 2 and all([self.board[i][2 - i] == letter for i in range(3)]):
            return True
        return False
      
     
      
      
def play(game, x_player, o_player, print_game=True):  # Main function to play the game
    if print_game:
        game.print_board_nums()  # Print the board numbers for reference

    letter = 'X'  # Starting letter
    while game.available_moves():  # While there are still available moves
        if letter == 'O':
            square = o_player.get_move(game)  # Get move from O player
        else:
            square = x_player.get_move(game)  # Get move from X player

        row = square // 3
        col = square % 3
        if game.board[row][col] == ' ':  # If the move is valid (the square is empty)
            game.board[row][col] = letter  # Make the move on the board
            if print_game:
                print(letter + f' makes a move to square {square}')  # Print the move made
                game.print_board()  # Print the current state of the board

            if game.winner(row, col, letter):  # Check if the current player has won
                if print_game:
                    print(letter + ' wins!')  # Print the winner
                return letter  # Return the winner

            letter = 'O' if letter == 'X' else 'X'  # Switch players
            
        time.sleep(0.8)  # Pause for a moment to make the game more enjoyable

    if print_game:
        print('It\'s a tie!')  # If there are no more available moves and no winner, it's a tie
        
        
if __name__ == '__main__':
    x_player = HumanPlayer('X')  # Create a human player for X
    o_player = GeniusComputerPlayer('O')  # Create a genius computer player for O
    t = tictactoe()  # Create a new game instance
    play(t, x_player, o_player, print_game=True)  # Start the game