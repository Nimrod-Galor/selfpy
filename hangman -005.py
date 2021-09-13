import re
HANGMAN_ASCII_ART = """
  _    _ 
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/ """

MAX_TRIES = 6

print(HANGMAN_ASCII_ART, "\n\r", MAX_TRIES)


picture1 = """x-------x"""
picture2 = """x-------x
    |
    |
    |
    |
    |"""
picture3 = """x-------x
    |       |
    |       0
    |
    |
    |"""
picture4 = """x-------x
    |       |
    |       0
    |       |
    |
    |"""
picture5 = """x-------x
    |       |
    |       0
    |      /|\\
    |
    |"""
picture6 = """x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |"""
picture7 = """x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""

user_guess = input("Guess a letter: ")



def is_valid_input(letter_guessed):
    if len(letter_guessed) == 1 && re.search('[a-zA-Z]', letter_guessed) == None:
        return True
    else:
        return False

print(is_valid_input('a'))

input()