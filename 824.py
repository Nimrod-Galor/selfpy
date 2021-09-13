def sort_anagrams(list_of_strings):
    """
    return list of strings of anagrams
    :list_of_strings list of words
    :type list
    :return list of anagrams
    :rtype list
    """
    res_list = []
    used_list = []
    master_index = 0
    for word in list_of_strings:
        if word in used_list:
            continue
        used_list.append(word)
        tmp_list = [word]
        for anagram in list_of_strings:
            if anagram in used_list:
                continue
            if sorted(word) == sorted(anagram):
                tmp_list.append(anagram)
                used_list.append(anagram)
        res_list.append(tmp_list)
    return res_list

list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
print(sort_anagrams(list_of_words))