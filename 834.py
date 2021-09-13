def inverse_dict(my_dict):
    """
    return dictionary where keys are values from old dictionary and the values are the keys
    :param my_dict a dictionary
    :type dictionary
    :return dictionary where keys are values from old dictionary and the values are the keys
    :rtype dictionary
    """
    new_dict = {}
    for key, value in my_dict.items():
        if value in new_dict.keys():
            new_dict[value].append(key)
        else:
            new_dict.update({value: [key]})
    return new_dict

course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
print(inverse_dict(course_dict))