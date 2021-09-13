def main():
    """
    get user input path to text file
    get user input action: sort rev last
    if sort action print words in file sorted with no duplications
    if rev action print all chars in line in revers order
    if last action get user input a number and print the last (n) rows
    :return none
    """
    file_path = input("Enter a file path: ")
    task = input("Enter a task (sort, rev, last): ")

    fo = open(file_path, "r")
    if task == "sort":
        lines = fo.read()
        words = lines.split()
        words = list(dict.fromkeys(words))
        print(sorted(words))
    elif task == "rev":
        for line in fo:
            print(line[::-1])
    elif task == "last":
        row = int(input("Enter a number: "))
        for line in fo:
            row -= 1
            if row < 0:
                print(line)
    fo.close()

if __name__ == "__main__":
    main()