import csv
from hashlib import sha256

databaseprojectthing ="""
█▀▄░█▀█░▀█▀░█▀█░█▀▄░█▀█░█▀▀░█▀▀░█▀█░█▀▄░█▀█░▀▀█░█▀▀░█▀▀░▀█▀░▀█▀░█░█░▀█▀░█▀█░█▀▀
█░█░█▀█░░█░░█▀█░█▀▄░█▀█░▀▀█░█▀▀░█▀▀░█▀▄░█░█░░░█░█▀▀░█░░░░█░░░█░░█▀█░░█░░█░█░█░█
▀▀░░▀░▀░░▀░░▀░▀░▀▀░░▀░▀░▀▀▀░▀▀▀░▀░░░▀░▀░▀▀▀░▀▀░░▀▀▀░▀▀▀░░▀░░░▀░░▀░▀░▀▀▀░▀░▀░▀▀▀"""

"""
user = [name, password, admno, Subjects]
"""

STUDENT_FILE_PATH = 'students.csv'
HW_FILE_PATH = 'homework.txt'
SUBJECTS = ["English", "Mathematics", "Chemistry", "Physics",
            "German", "Computer Science", "Physical Education"]

studentList = []


def fetchDatabase():
    global studentList
    with open(STUDENT_FILE_PATH, 'r+') as databasething:
        studentList = list(csv.reader(databasething))

def rewriteDatabase():
    global studentList
    with open(STUDENT_FILE_PATH, 'w+') as databasething:
        ...

def getUser(admo):
    global studentList, user
    for row in studentList:
        if row[2] == admo:
            user = row
    return user

def login(admno, password):
    if admno not in [row[2] for row in studentList]:
        return
    else:
        user = getUser(admno) # Password for Ark Malhotra = 123456
        if sha256(password.encode('utf-8')).hexdigest() != user[1]:
            return
        else:
            return user

def register(name, password, subjectlist):
    global studentList, user
    with open(STUDENT_FILE_PATH, 'a', newline='') as databasething:
        user = [name, sha256(password.encode('utf-8')).hexdigest(), len(studentList), subjectlist]
        csv.writer(databasething).writerow(user)
        return user

def seeHomework():
    with open(HW_FILE_PATH, 'r') as hw:
        homeworkList = [item[0:-1].split('\t\t') for item in hw.readlines()]
    validHomeworks = []
    for homework in homeworkList:
        if homework[1] in user[3].split(','):
            validHomeworks.append(homework)
    return validHomeworks

def deleteSubjects(deletedSubjects):
    global user, studentList
    for randomUserN in range(len(studentList)):
        if user[2] == studentList[randomUserN]:
            subjectlist = studentList[randomUserN].split(',')
            for subject in subjectlist:
                if subject in deletedSubjects:
                    subjectlist.remove(subject)
            studentList[randomUserN] = subjectlist
    # WORK FROM HERE


def addSubject():
    global user
    ...
    
def deleteAccount():
    ...

def getUsersWithSubject(subject):
    with open(STUDENT_FILE_PATH, "r") as f:
        stlist = list(csv.reader(f))
    print(stlist)
    return [i for i in stlist if subject in i[3]]

if __name__ == '__main__':
    print(databaseprojectthing)
    fetchDatabase()
    
    
    print('Welcome to the student login page.')
    
    user = None
    while not user:
        print('Type "login" to login, "register" to register, and "exit" to exit.')
        command = input('>>> ')
        if command == 'login':
            admno = input('\nEnter your admission number: ')
            password = input('Enter your password: ')
            user = login(admno, password)
        elif command == '.': user = login('1', '123456')
    
        elif command == 'register':
            name = input('\nEnter your name: ')
            password = input('Enter your password: ')
            print('Here is a list of all courses offered:', *SUBJECTS)
            subjects = input('Enter all subjects *separated by a "," (not space!):')
            user = register(name, password, subjects)
            print('\n⇒', len(studentList), 'is your admission number. Use this to login next time.')
    
        elif command == 'exit':
            exit()
        
        if not user: print('Error: username or password was wrong.')
            
    
    print(f'\n\nWelcome, {user[0]}. You are now logged in.\nHere is a list of all the commands:')
    while True:
        print('\n⋅ homework: See all the homework assigned to you.\n⋅ delete-subject: delete a subject\n⋅ add-subject: add a subject.\n⋅ exit: Stops the program.')
        command = input('>>> ')
        if command == 'homework' or command == 'hw': seeHomework()
        elif command == 'delete-subject' or command == 'ds':
            print('Here are the subjects you have taken: ' )
            for subject in user[3].split(','):
                print('⋅', subject)
            error = 0
            while True:
                error = 0
                deletedSubjects = input('Please enter all the subjects you want to drop, separated by ",": ')
                for subject in deletedSubjects.split(','):
                    if subject not in user[3].split(','):
                        error = 1
                        print('Error: you entered a subject which you do not have.')
                if error == 0: break
            deleteSubjects(deletedSubjects)
        elif command == 'add-subject' or command == 'as': addSubject()
        elif command == 'exit' or command == 'e': exit()
