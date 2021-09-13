import re

def seven_boom(end_number):
    """
    return a list of numbers from 0 to end_number and replace all numbers that have 7 in them or numbers that can be divided by 7 with the word boom
    :param end_number last number in rage to check
    :type int
    :return  a list of numbers from 0 to end_number and replace all numbers that have 7 in them or numbers that can be divided by 7 with the word boom
    :rtype list
    """
    res_list = []
    for num in range(end_number + 1):
        if re.search('[7]', str(num)) != None or num % 7 == 0:
            res_list.append("BOOM")
        else:
            res_list.append(num)
    return res_list

print(seven_boom(17))
