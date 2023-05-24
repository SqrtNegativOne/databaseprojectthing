import csv
from hashlib import sha256

databaseprojectthing = """
█▀▄░█▀█░▀█▀░█▀█░█▀▄░█▀█░█▀▀░█▀▀░█▀█░█▀▄░█▀█░▀▀█░█▀▀░█▀▀░▀█▀░▀█▀░█░█░▀█▀░█▀█░█▀▀
█░█░█▀█░░█░░█▀█░█▀▄░█▀█░▀▀█░█▀▀░█▀▀░█▀▄░█░█░░░█░█▀▀░█░░░░█░░░█░░█▀█░░█░░█░█░█░█
▀▀░░▀░▀░░▀░░▀░▀░▀▀░░▀░▀░▀▀▀░▀▀▀░▀░░░▀░▀░▀▀▀░▀▀░░▀▀▀░▀▀▀░░▀░░░▀░░▀░▀░▀▀▀░▀░▀░▀▀▀
                                                                                                                                                                          
"""
print(databaseprojectthing)

subjects = ['Physics', 'Chemistry', 'Mathematics', 'Biology', 'Computer Science', 'Physical Education']

STUDENT_FILE_PATH = 'students.csv'
HW_FILE_PATH = 'homework.txt'

studentList = []

print('Welcome to the student login page.\n')

def refreshDatabase():
    global studentList
    studentList = []
    with open(STUDENT_FILE_PATH, 'r') as databasething:
        databasething.seek(0)
        for row in csv.reader(databasething):
            studentList.append(row)
        print(studentList) # DEBUGPRINTSTATEMENT
        # BUG!! Doesn't read the last lines of the csv file?

def getUser(admo):
    global studentList
    user = []
    for row in studentList:
        if row[2] == admo:
            user = row
    print(user) # DEBUGPRINTSTATEMENT
    return user

def signin():
    admno = input('Enter your admission number: ')
    if admno not in [row[2] for row in studentList]:
        print('Error: Admission number not found.')
        return None
    else:
        user = getUser(admno)
        password = sha256(input('Password: ').encode('utf-8')).hexdigest() # Password for Ark Malhotra = 123456
        print(password) # DEBUGPRINTSTATEMENT
        if password != user[1]:
            print('Error: wrong password.')
            return None
        else:
            return user

def register():
    global studentList
    with open(STUDENT_FILE_PATH, 'a', newline='') as databasething:
        subjectText = 'Subjects, separated by a comma (no space in between!):'
        csv.writer(databasething).writerow([input('Name: '), sha256(input('Password: ').encode('utf-8')).hexdigest(), len(studentList), input(subjectText)])
        admo = len(studentList)
        print('⇒', admo, 'is your admission number. Use this to login next time.\n')
        refreshDatabase()
        return getUser(admo)

def seeHomework(user):
    with open(HW_FILE_PATH, 'r') as hw:
        print(hw.readlines())
        homeworkList = [item for item in hw.readlines()]
        print(homeworkList)
        # Homework Subject Deadline
    for homework in homeworkList:
        if homework[1] in user[3].split(','):
            print(str(homework[1]) + ': '+ str(homework[0]) + '(Deadline: ' + str(homework[3]) + ')')

def deleteSubject(user):
    ...

def addSubject(user):
    ...

refreshDatabase()
user = None
exit = False
while not user:
    print('Type "signin" to sign in, "register" to register, and "exit" to exit.')
    command = input('>>> ')
    if command == 'signin':
        user = signin()
    elif command == 'register':
        user = register()
    elif command == 'exit':
        exit = True
        break

if not exit: print('You are now logged in.\nHere\'s a list of all the commands:\n\n')

while not exit:
    print('homework: See all the homework assigned to you.\ndelete-subject: delete a subject\nadd-subject: add a subject.\nexit: Stops the program.')
    command = input('>>> ')
    if command == 'homework': seeHomework(user)
    elif command == 'delete-subject': deleteSubject(user)
    elif command == 'add-subject': addSubject(user)
    elif command == 'exit': break
