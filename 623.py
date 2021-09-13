def format_list(my_list):
    format_list = my_list[::2] + ["and " + my_list[-1]]
    return format_list


my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
print(format_list(my_list) )

