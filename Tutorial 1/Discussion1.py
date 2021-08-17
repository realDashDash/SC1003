student_counter = 0
total = 0

while student_counter < 10:
    total += int(input("Enter student's scores: "))
    student_counter += 1

print("Average score: ", total / (student_counter+1))