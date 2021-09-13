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

#user_guess = input("Guess a letter: ")
#print(user_guess.lower())

user_word = input("Please enter a word: ")
#print("".rjust(len(user_word), "_"))
#print("".zfill(len(user_word)).replace("0", " _"))
print(" _" * len(user_word))
input()