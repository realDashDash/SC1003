#  requirements:
#    - more than 8 characters
#    - at least one upper letter and lower letter
#    - at least one number

def check_pw(password):
    length = 0
    upper = False
    lower = False
    number = False

    length = len(password)
    for ch in password:
        if (ord(ch) >= 97 and  ord(ch) <= 122):
            lower = True
        if (ord(ch) >= 65 and  ord(ch) <= 90):
            upper = True
        if (ord(ch) >= 48 and  ord(ch) <= 57):
            number = True
    if (length >= 8 and upper and lower and number):
        return True
    else:
        return False

pw = input("Please enter password: ")
if (check_pw(pw)):
    print("Success!")
else:
    print("Please enter another password!")
    