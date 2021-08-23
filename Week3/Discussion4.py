n = int(input("Please enter pattern width: "))
print()

# pattern 1 - nested for loop
for i in range(2 * n):
    if (i < n):
        for j in range(0, i + 1):
            print("*", end = "")
    else:
        for j in range(10 - i - 1, 0, -1):
            print("*", end = "")
    print('\n', end="")

# pattern 1 - only two for loops
for i in range(2*n):
    if (i < n):
        index = i
    else:
        index = 10 - i
        
    for j in range (index):
        print("*", end="")
    print('\n', end = "")

# pattern 1 - only one for loops
for i in range(2*n):
    if (i < n):
        index = i
    else:
        index = 10 - i
    print("*" * index)


# pattern 2
for i in range(2*n):
    if ( i < n):
        index = i
    else:
        index = 10 - i
        
    for j in range (0, n - index):
        print(" ", end = "")
    for j in range (n - index, n):
        print("*", end = "")
    print("\n", end = "")

# pattern 3
for i in range(2*n):
    if (i < n):
        index = i
    else:
        pass
    # todo 
