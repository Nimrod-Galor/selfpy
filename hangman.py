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
MAX_TRIES = 7

HANGMAN_PHOTOS = {
"1": """x-------x""",
"2": """x-------x
|
|
|
|
|""",
"3": """x-------x
|       |
|       0
|
|
|""",
"4": """x-------x
|       |
|       0
|       |
|
|""",
"5": """x-------x
|       |
|       0
|      /|\\
|
|""",
"6": """x-------x
|       |
|       0
|      /|\\
|      /
|""",
"7": """x-------x
|       |
|       0
|      /|\\
|      / \\
|"""
}

def print_hangman(num_of_tries):
    """
    print one of the stages in HANGMAN_PHOTOS
    :param num_of_tries number of user failed tries
    :type int
    :return none
    """
    print(HANGMAN_PHOTOS[str(num_of_tries)])

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

def check_valid_input(letter_guessed, old_letters_guessed):
    """
    check if valid input.
    :param letter_guessed the char the user input
    :type string
    :param old_letters_guessed the characters user guessed previously
    :type list
    :return true if valid input else false
    :rtype bool	
    """
    if len(letter_guessed) == 1 and re.search('[^a-zA-Z]', letter_guessed) == None and letter_guessed.lower() not in old_letters_guessed:
        return True
    else:
        return False

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    use check_valid_input function to determine if input is valid. if it is add it to previous letter guessed list and return true. other ways print X and the previously guessed letters and return false.
    :param letter_guessed the char the user input
    :type string
    :param old_letters_guessed the characters user guessed previously
    :type list
    :return true if valid input else false
    :rtype bool
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    else:
        print("X")
        old_letters_guessed.sort()
        print(" -> ".join(old_letters_guessed))
        return False

def choose_word(file_path, index):
    """
    return number of words in file and the word in given inde
    :param file_path path to file of words
    :type string
    :param index index of chosen word
    :type int
    :return word in given index
    :rtype string
    """
    fo = open(file_path, "r")
    content = fo.read()
    fo.close()

    index -= 1
    word_list = list(dict.fromkeys(content.split()))
    number_of_words = len(word_list)
    if index > number_of_words:
        index = index % number_of_words
    return word_list[index]

def main():
    """
    get user input path to text file containing list of words.
    get user input a number that will represent position of a word.
    chose a word based on user input
    :return none
    """

    secret_word = ""
    num_of_tries = 1
    old_letters_guessed = []

    print(HANGMAN_ASCII_ART, "\nMax tries: ", MAX_TRIES)
    file_path = input("Enter a file path: ")
    word_index = input("Enter a number: ")
    secret_word = choose_word(file_path, int(word_index))
    print("\nLet’s start!\n")
    print_hangman(num_of_tries)
    print(show_hidden_word(secret_word, old_letters_guessed))
		
    while True:
        valid_input_flag = False
        while valid_input_flag == False:
            letter_guessed = input("Guess a letter: ")
            valid_input_flag = try_update_letter_guessed(letter_guessed, old_letters_guessed)

        if letter_guessed.lower() not in secret_word:
            print(":(")
            num_of_tries += 1
            print_hangman(num_of_tries)

        print(show_hidden_word(secret_word, old_letters_guessed))

        if check_win(secret_word, old_letters_guessed):
            print("WIN")
            break
        print("old_letters_guessed: " , len(old_letters_guessed), " max tries: ", MAX_TRIES)
        if len(old_letters_guessed) >= MAX_TRIES - 1:
            print("LOSE")
            break

if __name__ == "__main__":
    main()