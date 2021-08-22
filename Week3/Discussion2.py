counter = 0
while (True):
    input_str = input("enter a string (enter #### to stop): ")
    if (input_str != "####"):
        for str in input_str:
            if (str == 'a'):
                counter += 1
                break
            else:
                continue
    else:
        break

print(counter, "strings with letter 'a'")

