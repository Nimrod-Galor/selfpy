def last_early(my_str):
    last_letter = my_str[-1]
    index = my_str.lower().find(last_letter, 0, -1)
    if index != -1:
        return True
    else:
        return False

print(last_early("X"))


input()