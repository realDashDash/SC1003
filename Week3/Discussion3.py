for i in range(20):
    i += 1
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz")
    elif (i % 3 == 0) and (i % 5 != 0):
        print("Fizz")
    elif (i % 3 != 0) and (i % 5 == 0):
        print("Buzz")
    else:
        print(i)