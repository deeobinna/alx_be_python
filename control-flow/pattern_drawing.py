pattern = abs(int(input("Enter the size of the pattern: ")))
while pattern:
    for i in range(pattern):
        print("*", end="")
    print()
    pattern -= 1