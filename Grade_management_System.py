StudentInfo = []

class Student:
    def __init__(self, n, m):
        self.__name = str(n)
        self.__marks = int(m)
        
    def getStudentName(self):
        return self.__name
    
    def getStudentMarks(self):
        return self.__marks
    
        
def CalcAvg():
    total = 0
    count = 0
    for i in StudentInfo:
        total += i.getStudentMarks()
        count += 1
    print (total/count)
    
def AddStudent():
    name = str(input("Enter name of student: "))
    marks = int(input("Enter marks of student: "))
    while marks < 0 or marks > 100:
        marks = int(input("You entered a wrong value. Enter marks of student: "))
    student = Student(name, marks)
    StudentInfo.append(student)