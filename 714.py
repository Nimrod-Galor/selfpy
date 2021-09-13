def squared_numbers(start, stop):
"""
return a list of square roots of all number from start to stop.
:param start first number to square in list
:type start int
:param stop last number to square in list
:type stop int
:return a list of square roots of all number from start to stop.
:rtype list
"""
    return_list = []
    while start <= stop:
        return_list.append(start ** 2)
        start += 1
    return return_list

print(squared_numbers(-3, 3))