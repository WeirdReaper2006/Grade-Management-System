StudentInfo = []
existing_student_ids = set()
filehandle = open("IDs.txt", "r")
for i in filehandle.readlines():
    existing_student_ids.add(int(i.strip()))

class Student:
    def __init__(self, id, n, m):
        self.__ID = int(id)
        self.__name = str(n)
        self.__marks = int(m)
        
    def getStudentID(self):
        return self.__ID
        
    def getStudentName(self):
        return self.__name
    
    def getStudentMarks(self):
        return self.__marks
    
    def getStudentDetails(self):
        retVal = f"{self.__name} with student ID {self.__ID} got {self.__marks} marks"
        return retVal
    
def ValidateName(name):
    retVal = True
    allowed_characters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ")
    for char in str(name):
        if char not in allowed_characters:
            retVal = False
    return retVal

def CalcAvg():
    total = 0
    count = 0
    for i in StudentInfo:
        total += i.getStudentMarks()
        count += 1
    print (total/count)
    
def AddStudent():
    global existing_student_ids
    id = int(input("Enter Student ID: "))
    while id < 1 or id in existing_student_ids:
        if id < 1:
            id = int(input("You have entered an invalid ID. Enter Student ID: "))
        elif id in existing_student_ids:
            id = int(input("This ID is already taken. Enter a different Student ID: "))
    name = str(input("Enter name of student: "))
    while ValidateName(name) == False:
        name = str(input("You have entered a wrong value. Enter name of student again: "))
    marks = int(input("Enter marks of student: "))
    while marks < 0 or marks > 100:
        marks = int(input("You entered a wrong value. Enter marks of student: "))
    student = Student(id, name, marks)
    existing_student_ids.add(id)
    fileHandle = open("Grades.txt", "a")
    fileHandle.write(f"{name} with student ID {id} got {marks}\n")
    fileHandle.close()
    fileHandle2 = open("IDs.txt", "a")
    fileHandle2.write(f"{id}\n")
    fileHandle2.close()
    StudentInfo.append(student)
    
#Main Program
AddStudent()
AddStudent()
CalcAvg()
for i in range(len(StudentInfo)):
    print(StudentInfo[i].getStudentDetails())