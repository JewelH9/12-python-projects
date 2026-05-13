import random

def play_game():   # This function contains the main logic for the rock-paper-scissors game.
    choices = ['rock', 'paper', 'scissors']       # This list defines the valid choices for the game.
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    
    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return
    
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:     # This condition checks if both the user and the computer made the same choice, resulting in a tie.
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):        # This condition checks all the winning scenarios for the user.
        print("You win!")
    else:
        print("Computer wins!")
        

if __name__ == "__main__":
    play_game()   # This line ensures that the game starts when the script is run directly.