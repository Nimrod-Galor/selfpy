def sequence_del(my_str):
    """
    delete letters that repeat more than once in string
    :param my_str string
    :type string
    :return a string with none repeting letters
    :rtype string
    """
    new_str = ""
    last_letter = ""
    for letter in my_str:
        if letter != last_letter:
            new_str += letter
            last_letter = letter
    return new_str

print(sequence_del("ppyyyyythhhhhooonnnnn"))
print(sequence_del("SSSSsssshhhh"))
print(sequence_del("Heeyyy   yyouuuu!!!"))