#MIT 6.189 Project 1: Hangman Project
# *Art created by internet artist sk*

from random import randrange
from string import *  # noqa: F403
from hangman_lib import *  # noqa: F403

WORDLIST_FILENAME = "words.txt"

def load_words():
    print('\033[1m*Art created by internet artist sk*\033[0m')
    
    
    inFile = open(WORDLIST_FILENAME, 'r')

    for line in inFile:
        words = line.strip()
        wordlist = words.split(' ')
    print('Welcome to my hangman game! 😃')
    print("Word chosed from list of: " + str(len(wordlist)) + " words!")
    return wordlist

words_dict = load_words()

def get_word():
    global words_dict
    if not words_dict:
        load_words()

    word = words_dict[randrange(0, len(words_dict))]
    return word

# CONSTANTS
MAX_MISTAKES = 6

# GLOBAL VARIABLES 
secret_word = get_word()
letters_guessed = []
mistakes_made = 0
secret_code = []


def word_guessed():
    global secret_word
    global letters_guessed

    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True
    

def print_guessed():
    global secret_word
    global letters_guessed
    global secret_code
    
    secret_code = []
    char_list = []
    for char in secret_word:
        char_list.append(char)
        secret_code.append('-')

    for i, letter in enumerate(char_list):
        if letter in letters_guessed:
            secret_code[i] = letter
    return ''.join(secret_code)


def play_hangman():
    global secret_word
    global letters_guessed
    global mistakes_made
    global secret_code
    
    while mistakes_made < MAX_MISTAKES and print_guessed() != secret_word:
        guess = input("What is your guess?\nLetter or Word:\n>")  # noqa: E501
        if len(guess) == 1:
            if guess not in letters_guessed:
                letters_guessed.append(guess)
                if guess in secret_word:
                    print_hangman_image(mistakes_made)  # noqa: F405
                    print('Letters Guessed: ' + str(letters_guessed))
                    print('Mistakes Made: MAX-' + str(MAX_MISTAKES) +  ' MADE-' + str(mistakes_made))  # noqa: E501
                    print('Current Progress: ' + print_guessed())

                else:
                    mistakes_made += 1
                    print_hangman_image(mistakes_made)  # noqa: F405
                    print('That letter is not in the word')
                    print('Letters Guessed: ' + str(letters_guessed))
                    print('Mistakes Made: MAX-' + str(MAX_MISTAKES) +  ' MADE-' + str(mistakes_made))  # noqa: E501
                    print('Current Progress: ' + print_guessed())

            elif guess in letters_guessed:
                print_hangman_image(mistakes_made)  # noqa: F405
                print('Letters Guessed: ' + str(letters_guessed))
                print('Mistakes Made: MAX-' + str(MAX_MISTAKES) +  ' MADE-' + str(mistakes_made))  # noqa: E501
                print('Current Progress: ' + print_guessed()) 
                print("!!!LETTER ALREADY GUESSED, TRY AGAIN!!!") 
        
        elif len(guess) > 1:
            if guess == secret_word:
                print_hangman_image(mistakes_made)   # noqa: F405
                print('Letters Guessed: ' + str(letters_guessed))
                print('Mistakes Made: MAX-' + str(MAX_MISTAKES) +  ' MADE-' + str(mistakes_made))  # noqa: E501
                print('Current Progress: ' + secret_word)
                print("🎊🎊!!!CONGRATS, YOU WIN THE GAME!!!🎊🎊\nTHE ANSWER WAS: " + secret_word)  # noqa: E501
                break

            elif guess != secret_word:
                mistakes_made += 1
                print_hangman_image(mistakes_made)  # noqa: F405
                print('That is not the word')
                print('Letters Guessed: ' + str(letters_guessed))
                print('Mistakes Made: MAX-' + str(MAX_MISTAKES) +  ' MADE-' + str(mistakes_made))  # noqa: E501
                print('Current Progress: ' + print_guessed())
        
    else:
        if print_guessed() == secret_word:
            print("🎊🎊!!!CONGRATS, YOU WIN THE GAME!!!🎊🎊\nTHE ANSWER WAS: " + secret_word)  # noqa: E501ord)
    
        elif MAX_MISTAKES == 6:
            print("❌❌SORRY, YOU LOSE THE GAME❌❌\nTHE ANSWER WAS: " + secret_word)
        
    return None

play_hangman()
