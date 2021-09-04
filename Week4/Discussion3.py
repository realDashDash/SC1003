# Method 1: oop - class
class Student:
    
    def __init__(self, s_group = "", s_id = "", s_grade = 0):
        self.group = s_group
        self.ID = s_id
        self.grade = s_grade
    
    def printInfo(self):
        print("Student group:", self.group, "id:", self.ID, "grade:", self.grade)

tim = Student("SC9", 29, 100)
tim.printInfo()

# Method 2: dictionary
student = {["SC9", 29]:100, ["SC1", 20]:99}
# todo