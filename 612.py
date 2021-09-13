def shift_left(list):
    first_item = list[0]
    list[0] = list[1]
    list[1] = list[2]
    list[2] = first_item
    return list

print(shift_left(['monkey', 2.0, 1]))
