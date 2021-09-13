import re
def is_valid_input(letter_guessed):
    if len(letter_guessed) == 1 and re.search('[^a-zA-Z]', letter_guessed) == None:
        return True
    else:
        return False

print(is_valid_input('a'))
print(is_valid_input('A'))
print(is_valid_input('$'))
print(is_valid_input('ab'))
print(is_valid_input('app$'))
