grades1 = []
grades2 = []

def input_grades (grades):
    print("Please enter list of grades: ")
    while (True):
        grade = input("Enter grade, finish with 'q': ")
        if (grade != 'q'):
            grades.append(int(grade))
        else:
            break
    
def get_average(grades):
    n = len(grades)
    sum = 0
    
    for i in range(n):
        sum += grades[i]

    return sum/n

input_grades(grades1)
input_grades(grades2)

print("Average of first list of grades: ", get_average(grades1))
print("Average of second list of grades:", get_average(grades2))