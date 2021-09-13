# 1A2B Inverse Game

unused = [x for x in range(0, 10)]
used = []
guess = []

def check_guess(guess):
    for i in len(guess):
        print(guess[i], end = '')
    print()
    x, y = input("Check: ")
    return x, y

def if_0(guess):
    for i in range(len(guess)):
        used.append(guess[i])
        unused.remove(guess[i])

def if_4A(guess):
    print("The answer is ", guess, ".")

def if_AB4(guess, x, y):
    pass

def if_others(guess, x, y):
    pass

def replace_list(ip_list, p):
    ''' input: list, position to replace
        output: replaced list
    '''
    ip_list[p] = unused[0]
    return ip_list

def swap_list(ip_list, a, b):
    ''' Swap elements with index a and b in input list'''
    temp = ip_list[a]
    ip_list[a] = ip_list[b]
    ip_list[b] = temp
    return ip_list

def Game():
    guess = [x for x in range(4)] # inital guess
    used = guess

    x, y = check_guess(guess)

    if (x == 4):
        if_0(guess)
    elif (x+y == 4):
        if_AB4(guess, x, y)
    elif (x+y == 0):
        if_0(guess)
    else:
        if_others(guess, x, y)

if __name__ == "__main__":
    Game()
