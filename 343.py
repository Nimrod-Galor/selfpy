user_input = input("Please enter a string: ")
new_str = user_input[:len(user_input) // 2].lower() + user_input[len(user_input) // 2:].upper()
print(new_str)