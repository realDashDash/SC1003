# student_info = {("Group", id):score}

def inputRecored(database, group, id, score):
    ''' Funcion: Enter a record in the database.
    '''
    key = (group, id)
    value = score
    if key in database.keys():
        print("Sorry. Record already exists.")
        return None
    else:
        database[key] = value

def query(database, group, id):
    ''' Function to query a record in the database
        input: database name(database), record id (group, id)
        output: the scoure of the student
    '''
    key = (group, id)
    if key not in database.keys():
        print("Sorry, the record does not exist.")
        return None
    else:
        return database[(group, id)]

def listGrades(database, group):
    ''' Returns list of scores in a group
    '''
    # grades = []
    # for item in database:
    #     if (item[0] == group):
    #         grades.append(database[item])
    # return grades
    scorelist = []
    for key, value in database.items():
        if key[0] == group:
            scorelist.append(value)
    return scorelist


def maxGrade(database, group):
    # max = 0
    # for item in database:
    #     if (item[0] == group and database[item] > max):
    #         max = database[item]
    # return max
    scorelist = listGrades(database, group)
    maxscore = max(scorelist)
    return maxscore

def getGroup(database):
    names = []
    for item in database:
        if (item[0] in names):
            pass
        else:
            names.append(item[0])
    return names

grades = {}
# grades = {("SC9", 29):99, ("SC9", 28):80, ("SC9", 27):70, ("SC8", 1):100, ("SC9", 1):90}

print("Welcome to the grading system! Please enter your option:")
print("1: input a record")
print("2: query a student")
print("3: list grades in a group")
print("4: get max in a group")
print("5: list all group names")
print("6: exit")

while(True):
    option = int(input("option: "))
    if (option == 6):
        print("Thank you for using our system!")
        break

    elif (option == 1):
        group = input("Enter group: ")
        id = int(input("Enter id: "))
        score = int(input("Enter score: "))
        inputRecored(grades, group, id, score)

    elif (option == 2):
        group = input("Enter group: ")
        id = int(input("Enter id: "))
        print(query(grades, group, id))
        
    elif (option == 3):
        group = input("Enter group: ")
        print(listGrades(grades, group))
    
    elif (option == 4):
        group = input("Enter group: ")
        print(maxGrade(grades, group))
    
    elif (option == 5):
        print(getGroup(grades))
