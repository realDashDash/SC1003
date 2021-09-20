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
        elif (str.isupper()):
            return str.lower()
        else: # Consider about special chars
            return str
    else:
        if (str[0].islower()):
            new_str = reverseAndOppositeCase(str[1:]) + str[0].upper()
        elif (str[0].isupper()):
            new_str = reverseAndOppositeCase(str[1:]) + str[0].lower()
        else:
            new_str = reverseAndOppositeCase(str[1:]) + str[0]
        return new_str

# Discussion 3
def symmetricString(str):
    # rev_str = reverse(str)
    # new_str = str + rev_str
    # return new_str
    if (len(str) == 1):
        return str * 2
    else:
        new_str = str[0] + symmetricString(str[1:]) + str[0]
        return new_str
     

# Additional: check is a string is palidrome(symmatric)
def is_symmetric(str):
    if (len(str) == 1 or len(str) == 0):
        return True
    else:
        if str[0] != str[-1]:
            return False
        else:
            return is_symmetric(str[1:-1])
     
## test ##

# myStr1 = "ABC"
# myStr2 = "AbCdE"
# palindrome = "dogmaiamgod"

# # Discussion1:
# print(reverseAndRepeat(myStr1, 2))
# print(reverseAndRepeat(myStr1, 3))

# # Discussion2:
# print(reverseAndOppositeCase(myStr2))

# # Discussion3:
# print(symmetricString(myStr2))

# # Additional:
# print(is_symmetric(palindrome))
# print(is_symmetric(symmetricString("Singapore")))
