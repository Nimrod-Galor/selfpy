import re
def main():
    """
    get from user a string of products separated by comas.
    get user input a number.
    if input is 1: print product list
    if input is 2: print number of items in list
    if input is 3: get user input and check if producy exist in list
    if input is 4: get user input and check how many times product appears in list
    if input is 5: get user input and delete product from list
    if input is 6: get user input and add to list
    if input is 7: print all products that have a name with less than 3 letters or have none alphabet signs in them
    if input is 8: remove all product duplications
    if input is 9: exit
    :return none
    """	
    str_products = input("Enter a list of products: ")
    arr_products = str_products.split(",")
    while(True):
        menu_select = input("enter menu selection: ")
        if menu_select == "1":
            print(arr_products)
        elif menu_select == "2":
            print(len(arr_products))
        elif menu_select == "3":
            tmp_input = input("Check if product exists.\n Enter product name:")
            if tmp_input in arr_products:
                print("\"" + tmp_input + "\" exist in list")
            else:
                print("\"" + tmp_input + "\" dose not exist in list")
        elif menu_select == "4":
            tmp_input = input("Check how many times product appears in list.\n Enter product name:")
            num = arr_products.count(tmp_input)
            print("\"" + tmp_input + "\" appear/s " +  str(num) + " time/s")
        elif menu_select == "5":
            tmp_input = input("Delete product from list.\n Enter product name:")
            if tmp_input in arr_products:
                arr_products.remove(tmp_input)
        elif menu_select == "6":
            tmp_input = input("Add product to list.\n Enter product name:")
            arr_products.append(tmp_input)
        elif menu_select == "7":
            for item in arr_products:
                if len(item) < 3 or re.search('[^a-zA-Z]', item) != None:
                    print(item)
        elif menu_select == "8":
            arr_products = list(dict.fromkeys(arr_products))
        elif menu_select == "9":
            break


if __name__ == "__main__":
    main()