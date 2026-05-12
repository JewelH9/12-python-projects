import random        #python built-in module to generate random numbers

def guess_number_computer():        #function definition for the game
    print("Welcome to the Guess the Number Game!")
    print("I will think of a number between 1 and 100, and you have to guess it.")
    
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False
    
    while not guessed_correctly:
        try:                                                     #use try-except block to handle invalid input (non-integer values)
            user_guess = int(input("Enter your guess: "))        #get user input and convert it to an integer
            attempts += 1
            
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")          #handle the case where the user enters a non-integer value
            
if __name__ == "__main__":          #this ensures that the game runs only when the script is executed directly
    guess_number_computer()         #start the game by calling the function