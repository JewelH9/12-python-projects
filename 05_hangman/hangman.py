import random
from words import words  #importing the list of words from the words.py file
import string   #importing string module to get the list of uppercase letters

def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()
  
def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed
    
    lives = 6

    while len(word_letters) > 0 and lives > 0:  # while there are still letters to guess and the user has lives remaining
        print('You have used these letters: ', ' '.join(used_letters))   #.join() method is used to join the elements of the set into a string, with a space in between each element

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:  # if the letter is in the alphabet and has not been used yet
            used_letters.add(user_letter)
            if user_letter in word_letters:   # if the guessed letter is in the word, remove it from the set of letters to guess
                word_letters.remove(user_letter)
            else:
                lives -= 1  # if the guessed letter is not in the word, reduce the number of lives by 1
                print('Letter is not in the word. You have', lives, 'lives left.')

        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')

        else:
            print('Invalid character. Please try again.')

    if lives == 0:
        print('Sorry, you died. The word was', word, '!')
    else:
        print('Congratulations! You guessed the word', word, '!')
    

hangman()