# student_info = {["Group", id]:score}

def inputRecored(database, group, id, score):
    database[group, id] = score

def getInput():
    group = input("Enter group: ")
    id = int(input("Enter id: "))
    score = int(input("Enter score: "))
    inputRecored(grades, group, id, score)

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

# main function
grades = {("SC9", 29):99, ("SC9", 28):80, ("SC9", 27):70, ("SC8", 1):100, ("SC9", 1):90}
getInput()

print(query(grades, "SC9", 29))
print(listGrades(grades, "SC9"))
print(listGrades(grades, "SC8"))
print(maxGrade(grades, "SC9"))