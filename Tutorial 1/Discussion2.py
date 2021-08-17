passes = 0
failures = 0
student_counter = 1
while student_counter <= 10:
    score = int(input("Input next score: "))
    if score < 60:
        failures += 1
    else:
        passes += 1
    student_counter += 1
print("Passes: ", passes, "\nFailures: ", failures)
