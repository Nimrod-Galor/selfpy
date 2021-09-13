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

num_of_tries = 6
print_hangman(num_of_tries)