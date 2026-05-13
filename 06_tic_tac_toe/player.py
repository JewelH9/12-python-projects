import math
import random

class Player:
    def __init__(self, letter):  # X or O
        self.letter = letter  

    def get_move(self, game):  # we want all players to get their next move given a game
        pass
      
      
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square
      

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')   # Ask the user to input a move and check if it's valid
            try:
                val = int(square)
                if val not in game.available_moves():    # If the move is not valid, raise an error and ask for input again
                    raise ValueError
                valid_square = True
            except ValueError:        # If the input is not a valid integer or not an available move, print an error message and ask for input again
                print('Invalid square. Try again.')
        return val