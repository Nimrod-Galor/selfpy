def arrow(my_char, max_length):
    """
    return a string representing an arrow painted with user input letter and length
    :param my_char selected char
    :type char
    :param max_length max length of arrow
    :type int
    :return string representing arrow
    :rtype string
    """
    str_arrow = ""
    for num in range(1, max_length + 1):
        str_arrow += my_char * int(num) + "\n"
    for num in reversed(range(1, max_length)):
        str_arrow += my_char * int(num) + "\n"

    return str_arrow


print(arrow('*', 5))