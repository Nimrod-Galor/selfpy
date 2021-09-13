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

old_letters = []

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if len(letter_guessed) == 1 and re.search('[^a-zA-Z]', letter_guessed) == None and letter_guessed.lower() not in old_letters_guessed:
        old_letters.append(letter_guessed.lower())
        return True
    else:
        print("X")
        print(" -> ".join(old_letters_guessed.sort()))
        return False


print(check_valid_input('C', old_letters))
print(check_valid_input('ep', old_letters))
print(check_valid_input('$', old_letters))
print(check_valid_input('s', old_letters))

input()