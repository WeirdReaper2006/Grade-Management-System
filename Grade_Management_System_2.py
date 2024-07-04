import ast

# List to hold student data
Stu_DB = [] # list to store dictionaries


def validInput(userIn):
    while userIn < 0 or userIn > 100:  #ensures marks are between 0 and 100 inclusive
        userIn = int(input('Invalid input. Please try again. Enter: '))
    return userIn #returns validated marks


def sort():
    global Stu_DB
    Stu_DB = readfile('myfile.txt')
    for i in range(1, len(Stu_DB)):
        key = Stu_DB[i]
        place = i - 1
        while place >= 0 and key['Average'] > Stu_DB[place]['Average']:
            Stu_DB[place + 1] = Stu_DB[place]
            place -= 1
        Stu_DB[place + 1] = key


def readData(): #to display student data
    for thisrec in Stu_DB:
        print(thisrec.items())


def writeFile(Dictionary):
    with open('myfile.txt', 'a') as filehandle: #opening file
        filehandle.write(str(Dictionary) + '\n')


def readfile(myfile):
    global Stu_DB
    Stu_DB = []
    with open(myfile, 'r') as filehandle:
        lines = filehandle.readlines()
        for line in lines:
            if line.strip(): #checks if line is empty or not
                thisrec = ast.literal_eval(line.strip())
                Stu_DB.append(thisrec)
    return Stu_DB


def AddStu():
    stuN = input('Enter Name: ')
    while not stuN.isalpha():
        stuN = input('Invalid input. Enter a student name: ')

    math = validInput(int(input('Enter Math marks: ')))
    english = validInput(int(input('Enter English marks: ')))
    chem = validInput(int(input('Enter Chem marks: ')))
    phy = validInput(int(input('Enter Physics marks: ')))
    compu = validInput(int(input('Enter Computer marks: ')))

    stuID = len(Stu_DB) + 1
    avg = (math + english + chem + phy + compu) / 5
    Dictionary = {'ID': stuID, 'Name': stuN, 'Math': math, 'English': english, 'Chemistry': chem, 'Physics': phy,
                  'Computer': compu, 'Average': avg}
    writeFile(Dictionary)
    sort()


n = int(input('How many records you want to enter: '))
for i in range(n):
    AddStu()
    for thisrec in Stu_DB:
        print(thisrec)
        print('shown')