user_input = input("Insert the temperature you would like to convert: ")
if user_input[-1].lower() == "f":
    f = float(user_input[0:-1])
    c = (5 * f - 160) / 9
    print(c)
else:
    c = float(user_input[0:-1])
    f = (9 * c + (32 * 5)) / 5
    print(f)