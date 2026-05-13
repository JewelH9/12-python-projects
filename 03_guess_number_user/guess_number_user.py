import random

def computer_guess_number(x):   # x is the upper limit of the range of numbers
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':   # Loop until the computer guesses the correct number
        if low != high:     # If low and high are not the same, the computer can make a random guess between them
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high since low == high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').lower()  # Get feedback from the user
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly!')
    
    
if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    print("Think of a number between 1 and 100, and the computer will try to guess it.")
    computer_guess_number(100)   # Start the game with an upper limit of 100