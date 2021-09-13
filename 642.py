import re

old_letters = ['a', 'p', 'c', 'f']

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if len(letter_guessed) == 1 and re.search('[^a-zA-Z]', letter_guessed.lower()) == None and letter_guessed.lower() not in old_letters_guessed:
        old_letters.append(letter_guessed.lower())
        return True
    else:
        print("X")
        #print(" -> ".join(old_letters_guessed.sort()))
        old_letters_guessed.sort()
        print(" -> ".join(old_letters_guessed))
        return False


print(try_update_letter_guessed('A', old_letters))
print(try_update_letter_guessed('s', old_letters))
print(old_letters)
print(try_update_letter_guessed('$', old_letters))
print(try_update_letter_guessed('d', old_letters))
print(old_letters)