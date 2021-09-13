def is_greater(my_list, n):
    """
    return all numbers in the list that are greater than numbers
    :param my_list list of numbers
    :type my_list int
    :param n number
    :type n int
    :return all numbers in the list that are greater than numbers
    :rtype list
    """
    new_list = []
    for item in my_list:
        if item > n:
            new_list.append(item)
    return new_list


result = is_greater([1, 30, 25, 60, 27, 28], 28)
print(result)