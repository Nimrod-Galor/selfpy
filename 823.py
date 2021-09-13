def mult_tuple(tuple1, tuple2):
    """
    return all possible pair combination from two tuples
    :tuple1 tuple of int
    :type tuple
    :tuple2 tuple of int
    :type tuple
    :return a tuple contain all possible pair combination from two tuples
    :rtype tuple
    """
    comb = []
    for ia in tuple1:
        for ib in tuple2:
            comb.append((ia, ib))
            comb.append((ib, ia))
    return tuple(comb)
 
first_tuple = (1, 2)
second_tuple = (4, 5)
print(mult_tuple(first_tuple, second_tuple))

first_tuple = (1, 2, 3)
second_tuple = (4, 5, 6)
print(mult_tuple(first_tuple, second_tuple))