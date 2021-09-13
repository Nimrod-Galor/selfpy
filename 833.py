def count_chars(my_str):
    """
    return dictionary where key is char from string and value is the number of times that char repeat in the string
    :param my_str string
    :type string
    :return dictionary where key is char from string and value is the number of times that char repeat in the string
    :rtype dictionary
    """
    return_dict = {}
    for char in my_str:
        if char == " ":
            continue
        if char in return_dict.keys():
            return_dict[char] += 1
        else:
            return_dict[char] = 1
    return return_dict

magic_str = "abra cadabra"
print(count_chars(magic_str))