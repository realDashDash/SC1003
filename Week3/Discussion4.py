n = int(input("Please enter pattern width: "))
print()

# nested for loop
for i in range(2 * n):
    if (i < n):
        for j in range(0, i + 1):
            print("*", end = "")
    else:
        for j in range(10 - i - 1, 0, -1):
            print("*", end = "")  
    print('\n', end="")

# only two for loops
for i in range(2*n):
    if (i < n):
        index = i
    else:
        index = 10 - i
    for j in range (index):
        print("*", end="")
    print('\n', end = "")