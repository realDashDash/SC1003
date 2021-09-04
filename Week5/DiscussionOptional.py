# student_info = {("Group", id):score}

def inputRecored(database, group, id, score):
    database[(group, id)] = score

def query(database, group, id):
    return database[(group, id)]

def listGrades(database, group):
    grades = []
    for i in range(40):
        try: 
            grades.append(database[(group, i)])
        except:
            pass
    return grades

def maxGrade(dataBase, group):
    max = 0
    for i in range(40):
        try:
            if (dataBase[(group, i)] > max):
                max = dataBase[(group, i)]
        except:
            pass
    return max

grades = {}

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

