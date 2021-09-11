from random import randint

def generate_digits():
    ''' Function: generate four different digits as target number
        Input: Null
        Output: four digit numbers
    '''
    num = 0
    digits = []
    i = 0
    while (i < 4):
        digit = randint(0, 9)
        if (not digit in digits):
            digits.append(digit)
            i += 1
        else:
            continue
    for i in range(0, 4):
        num += digits[i] * (10**i)
    return num

def int2list(num_i):
    ''' Funcion: convert 4 digit number to list
        Input: 4-digit int number
        Output: list
    '''
    num_l = []
    for i in range(0, 4):
        num_l.append(num_i // (10 ** (4-i-1)))
        num_i -= num_l[i] * (10 ** (4-i-1))
    return num_l

def judge(i_num, t_num):
    ''' Function: compare input number and target number 
        Input: input number list, target number list
        Output: tupple of (A, B)
    '''
    A = B = 0
    for i in range(0, 4):
        if (i_num[i] == t_num[i]):
            A += 1
        elif (i_num[i] in t_num):
            B += 1
        else:
            continue
    return (A, B)

counter = 1
isWin = False

target = generate_digits()

while(not isWin):
    input_num = int(input("Please input 4 digits: "))
    AB = judge(int2list(input_num), int2list(target))
    if (AB == (4, 0)):
        isWin = True
    else:
        print(AB[0], " A (Bulls)", AB[1], " B (Cows)")
        counter += 1
else:
    print("You Win!")
    print("Attempts: ", counter)