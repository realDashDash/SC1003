def inputRecored(database, group, id, score):
    database[(group, id)] = score

def query(database, group, id):
    return database[(group, id)]

def listGrades(database, group):
    grades = []
    for item in database:
        if (item[0] == group):
            grades.append(database[item])
    return grades

def maxGrade(database, group):
    max = 0
    for item in database:
        if (item[0] == group and database[item] > max):
            max = database[item]
    return max