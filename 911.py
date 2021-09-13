def are_files_equal(file1, file2):
    """
    check if files content is equal
    :param file1 file path
    :type string
    :param file2 file path
    :type string
    :return true if files content is the same
    :rtype bool
    """
    res = False
    fo1 = open(file1, "r")
    f1l = fo1.read()
    fo2 = open(file2, "r")
    f2l = fo2.read()
    if f1l == f2l:
        res = True
    fo1.close()
    fo2.close()
    return res

print(are_files_equal("726.py", "726.py"))