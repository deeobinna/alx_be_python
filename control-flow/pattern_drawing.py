positive_number = int(input("Enter the size of the pattern: "))

while positive_number > 0:
    for i in range(positive_number):
        print("*", end="")
    print()
    positive_number -= 1