import re
def numbers_letters_count(my_str):
    """
    count the number of digits and number of none digit in string
    :param my_str string
    :type string
    :return return a list of the number of digits and number of none digit in string
    :rtype list
    """
    num_ofdigits = 0
    num_ofnonedigits = 0
    for letter in my_str:
        if re.search('[0-9]', letter) == None:
            num_ofnonedigits += 1
        else:
            num_ofdigits += 1
    return [num_ofdigits, num_ofnonedigits]
print(numbers_letters_count("Python 3.6.3"))