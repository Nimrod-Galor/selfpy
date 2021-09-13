def copy_file_content(source, destination):
    """
    copy source file to destination file
    :param source file path
    :type string
    :param destination file path
    :type string
    :return none
    """

    sfo = open(source, "r")
    sf_content = sfo.read()
    sfo.close()

    dfo = open(destination, "w")
    dfo.write(sf_content)
    dfo.close()

copy_file_content("copy.txt", "paste.txt")