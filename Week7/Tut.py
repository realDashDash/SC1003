# Base Function:
def reverse(str):
    if (len(str) == 1):
        return str
    else:
        new_str = reverse(str[1:]) + str[0]
        return new_str

# Discussion 1
def reverseAndRepeat(str, num):
    if (len(str) == 1):
        return str * num
    else:
        new_str = reverseAndRepeat(str[1:], num) + str[0]*num
        return new_str

# Discussion 2
def reverseAndOppositeCase(str):
    if (len(str) == 1):
        if (str.islower()):
            return str.upper()
        else:
            return str.lower()
    else:
        if (str[0].islower()):
            new_str = reverseAndOppositeCase(str[1:]) + str[0].upper()
        else:
            new_str = reverseAndOppositeCase(str[1:]) + str[0].lower()
        return new_str

# Discussion 3
def symmetricString(str):
    rev_str = reverse(str)
    new_str = str + rev_str
    return new_str 


## test ##

# myStr1 = "ABC"
# myStr2 = "AbCdE"

# # Discussion1:
# print(reverseAndRepeat(myStr1, 2))
# print(reverseAndRepeat(myStr1, 3))

# # Discussion2:
# print(reverseAndOppositeCase(myStr2))

# # Discussion3:
# print(symmetricString(myStr2))
