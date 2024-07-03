StudentInfo = []
existing_student_ids = set()
filehandle = open("IDs.txt", "r")
for i in filehandle.readlines():
    existing_student_ids.add(int(i.strip()))

class Student:   #Class declaration
    def __init__(self, id, n, m):    #Class initialisation
        self.__ID = int(id)   #Student ID
        self.__name = str(n)  #Student Name
        self.__marks = int(m) #Student Marks
        
    def getStudentID(self):
        return self.__ID      #Retrieve student ID
        
    def getStudentName(self):
        return self.__name    #Retrieve student name
    
    def getStudentMarks(self):
        return self.__marks   #Retrieve student marks
    
def CalcAvg():    #Function for calculating average
    total = 0
    count = 0
    try:
        for i in StudentInfo:
            total += i.getStudentMarks()
            count += 1
        print (total/count)
    except ZeroDivisionError:
        print("There are no students")

def ValidateName(name):     #Validates name to make sure that name does not have special characters
    retVal = True
    allowed_characters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ")
    for char in str(name):
        if char not in allowed_characters:
            retVal = False
    return retVal
    
def AddStudent():       #Function that adds student
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
    
def ReadFile():    #Function that reads from file to see which students have been added
    fileHandle = open ("Grades.txt", "r")
    for i in fileHandle.readlines():
        print(i)
    fileHandle.close()
    
#Main Program
AddStudent()
AddStudent()
CalcAvg()
ReadFile()