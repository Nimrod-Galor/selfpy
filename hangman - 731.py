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

def main():
    while(True):
        tmp_input = input("Enter a letter: ")
        old_letters_guessed.append(tmp_input)
        print(show_hidden_word(secret_word, old_letters_guessed))

if __name__ == "__main__":
    main()