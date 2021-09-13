def are_lists_equal(list1, list2):
    """
    check if lists contain the same items
    :param list1 list of numbers
    :type list
    :param list2 list of numbers
    :type list
    :return true if lists contain the same items
    :rtype bool
    """
    return(set(list1) == set(list2))
list1 = [0.6, 1, 2, 3]
list2 = [3, 2, 0.6, 1]
list3 = [9, 0, 5, 10.5]
print(are_lists_equal(list1, list2))
print(are_lists_equal(list1, list3))