def my_mp3_playlist(file_path):
    """
    return a tuple where first item the name of longest song
	second item number of songs in the file and last the name of artist with most songs
    :param file_path path to file containing our list
    :type string
    :return ""
    :rtype tuple
    """

    fo = open(file_path, "r")
    lines = fo.readlines()
    fo.close()

    long_song = ["", 0.0]
    artist_repeat = {}
    for line in lines:
        tmp_list = line.split(";")
        song_time = float(tmp_list[2].replace(":", "."))
        if song_time > long_song[1]:
            long_song[0] = tmp_list[0]
            long_song[1] = song_time
        if tmp_list[1] in artist_repeat.keys():
            artist_repeat[tmp_list[1]] += 1
        else:
            artist_repeat[tmp_list[1]] = 1
    res = (long_song[0], len(lines), max(artist_repeat, key=artist_repeat.get))
    return res

print(my_mp3_playlist("songs.txt"))