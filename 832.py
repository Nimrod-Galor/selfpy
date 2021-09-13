from datetime import date
my_dict = {"first_name": "Mariah", "last_name": "Carey", "birth_date": "27.02.1970", "hobbies": ["Sing", "Compose", "Act"]}

def calculate_age(born):
    """
    calculate age by birth date
    :param born birth date
    :type tuple
    :return age
    :rtype int
    """
    today = date.today()
    return today.year - int(born[2]) - ((today.month, today.day) < (int(born[1]), int(born[0])))
	
while True:
    user_input = input("Enter value 1-7: ")
    if user_input == "1":
        print(my_dict["last_name"])
    elif user_input == "2":
        print(my_dict["birth_date"])
    elif user_input == "3":
        print(len(my_dict["hobbies"]))
    elif user_input == "4":
        print(my_dict["hobbies"][-1])
    elif user_input == "5":
        my_dict["hobbies"].append("Cooking")
    elif user_input == "6":
        birth_date_tuple = (my_dict["birth_date"][0:2], my_dict["birth_date"][3:5], my_dict["birth_date"][6:])
        print(birth_date_tuple)
    elif user_input == "7":
        born = (my_dict["birth_date"][0:2], my_dict["birth_date"][3:5], my_dict["birth_date"][6:])
        my_dict["age"] = calculate_age(born)
        print(my_dict["age"])


