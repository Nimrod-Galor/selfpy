def choose_word(file_path, index):
    """
    return number of words in file and the word in given inde
    :param file_path path to file of words
    :type string
    :param index index of chosen word
    :type int
    :return number of words in file and the word in given inde
    :rtype tuple
    """

    fo = open(file_path, "r")
    content = fo.read()
    fo.close()

    index -= 1
    word_list = list(dict.fromkeys(content.split()))
    number_of_words = len(word_list)
    if index > number_of_words:
        index = index % number_of_words
    print(number_of_words)
    print(index)
    return (number_of_words, word_list[index])

print(choose_word("words.txt", 3))
print(choose_word("words.txt", 15))