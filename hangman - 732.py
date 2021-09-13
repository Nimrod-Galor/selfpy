secret_word = "mammals"
old_letters_guessed = []

def show_hidden_word(secret_word, old_letters_guessed):
    """
    show user progress
    :param secret_word the secret word user have to guess
    :type string
    :param old_letters_guessed list of the letters user have guessed
    :type list
    :return string of secret_word hidden except of letters use have guessed
    :rtype string
    """
    str_return = ""
    for char in secret_word:
        exist = False
        for old_letter in old_letters_guessed:
            if char == old_letter:
                exist = True
                break
        if exist:
            str_return += " " + char
        else:
            str_return += " _"
    return str_return.lstrip()

def check_win(secret_word, old_letters_guessed):
    """
    check if user guessed the secret word
    :param secret_word the secret word user have to guess
    :type string
    :param old_letters_guessed list of the letters user have guessed
    :type list
    :return true if user guessed the secret word
    :rtype bool
    """
    success = True
    for char in secret_word:
        if char not in old_letters_guessed:
            success = False
            break
    return success

secret_word = "friends"
old_letters_guessed = ['m', 'p', 'j', 'i', 's', 'k']
print(check_win(secret_word, old_letters_guessed))

secret_word = "yes"
old_letters_guessed = ['d', 'g', 'e', 'i', 's', 'k', 'y']
print(check_win(secret_word, old_letters_guessed)) 

