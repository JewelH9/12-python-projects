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

class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:  # If it's the first move, choose a random corner
            square = random.choice([0, 2, 6, 8])
        else:
            square = self.minimax(game, self.letter)['position']  # Use minimax to find the best move
        return square

    def minimax(self, state, player):
        max_player = self.letter  # Yourself
        other_player = 'O' if player == 'X' else 'X'  # The other player

        # First, check if the previous move is a winner
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)}
        elif not state.empty_squares():  # No empty squares
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # Maximize the max_player
        else:
            best = {'position': None, 'score': math.inf}  # Minimize the other player

        for possible_move in state.available_moves():
            #step 1: make a move, try that spot
            state.make_move(possible_move, player)  # Make a move

            #step 2: recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(state, other_player)  # Recurse using minimax to simulate a game after making that move

            #step 3: undo the move
            row = possible_move // 3   
            col = possible_move % 3

            state.board[row][col] = ' '  # Undo the move
            state.current_winner = None

            sim_score['position'] = possible_move   # This represents the move optimal next move found by minimax (the best move for the other player)

            #step 4: update the dictionaries if necessary
            if player == max_player:  # Trying to maximize the max_player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:  # Trying to minimize the other player
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best