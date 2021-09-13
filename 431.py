import re

user_guess = input("Guess a letter: ")
none_alphabet = re.search('[^a-zA-Z]', user_guess)

if len(user_guess) > 1:
    if none_alphabet != None:
        print("E3")
    else:
        print("E1")
elif none_alphabet != None:
    print("E2")
else:
    print(user_guess.lower())
