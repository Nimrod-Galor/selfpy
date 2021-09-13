user_input = input("enter a 3 digit number: ")
first = user_input[0:1]
second = user_input[1:2]
third = user_input[2:3]
sum = int(first) + int(second) + int(third)
print(sum)
print(sum / 3)
print(sum % 3)
print(sum % 3 == 0)