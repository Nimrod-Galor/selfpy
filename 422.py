user_input = input("Enter string: ").replace(" ", "").lower()
if user_input == user_input[::-1]:
    print("OK")
else:
    print("NOT")