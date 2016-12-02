try:
    with open("file") as file:
        for line in file:
            print(line, end="")
except IOError:
    print("can not open")
