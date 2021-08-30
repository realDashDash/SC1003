#  requirements:
#    - more than 8 characters
#    - at least one upper letter and lower letter
#    - at least one number
#    - at least one special character

# todo regular expression operations

def check_pw(password):
    length = 0
    upper = False
    lower = False
    number = False
    special = False
    notValid = False

    Special_char = ['@', '#', '$', '^', '&', '*']

    length = len(password)
    for ch in password:
        if (ord(ch) >= 97 and  ord(ch) <= 122): # if (password.islower():)
            lower = True
        elif (ord(ch) >= 65 and  ord(ch) <= 90): # if (password.isupper():)
            upper = True
        elif (ord(ch) >= 48 and  ord(ch) <= 57): # if (password.isdigit():)
            number = True
        elif (ch in Special_char): # if(not password.isalnum)
            special = True
        else:
            notValid = True

    if (length >= 8 and upper and lower and number and special and notValid):
        return True
    else:
        return False

while (True):
    pw = input("Please enter password: ")
    if (check_pw(pw)):
        print("Success!")
        break;
    else:
        print("Please enter another password!")
