def print_to_file(value):
    """
    print value to file
    :param value the file content
    :type int
    :return none
    """
    fo = open("found.txt", "w")
    fo.write(str(value))
    fo.close()

def who_is_missing(file_name):
    """
    return and writ to file the missing number from a set
    :param file_name file path containing the set
    :type string
    :return missing number
    :rtype int
    """

    fo = open(file_name, "r")
    content = fo.read()
    set = content.split(",")
    fo.close()

    set.sort()
    index = 1
    next_value = 0
    for number in set:
        next_value = int(number) + 1
        if next_value != int(set[index]):
            print_to_file(next_value)
            break
        index += 1

    return next_value

print(who_is_missing("findMe.txt"))