def my_mp4_playlist(file_path, new_song):
    """
    update the name of the third song on the list in file and print the updated list	
    :param file_path path to song list file
    :type string
    :param new_song the name of the new song
    :type string
    :return none
    """

    fo = open(file_path, "r")
    lines = fo.readlines()
    fo.close()

    index = 0
    for line in lines:
        if index == 2:
            tmp_list = line.split(";")
            tmp_list[0] = new_song
            lines[2] = ";".join(tmp_list)
        print(lines[index])
        index += 1

    fo = open(file_path, "w")
    for line in lines:
        fo.write(line)
    fo.close()

my_mp4_playlist("songs.txt", "Python Love Story")