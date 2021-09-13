user_input = input("Please enter a sentence: ")
first_char = user_input[0:1]
new_str = first_char + user_input[1:].replace(first_char, "e")
print(new_str)