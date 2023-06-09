import csv
from copy import deepcopy
from os import remove as fileRemove
from hashlib import sha256

databaseprojectthing ="""
█▀▄░█▀█░▀█▀░█▀█░█▀▄░█▀█░█▀▀░█▀▀░█▀█░█▀▄░█▀█░▀▀█░█▀▀░█▀▀░▀█▀░▀█▀░█░█░▀█▀░█▀█░█▀▀
█░█░█▀█░░█░░█▀█░█▀▄░█▀█░▀▀█░█▀▀░█▀▀░█▀▄░█░█░░░█░█▀▀░█░░░░█░░░█░░█▀█░░█░░█░█░█░█
▀▀░░▀░▀░░▀░░▀░▀░▀▀░░▀░▀░▀▀▀░▀▀▀░▀░░░▀░▀░▀▀▀░▀▀░░▀▀▀░▀▀▀░░▀░░░▀░░▀░▀░▀▀▀░▀░▀░▀▀▀"""

# user = [name, password, admno, Subjects]

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
    fileRemove(STUDENT_FILE_PATH)
    for personN in range(len(studentList)):
        if type(studentList[personN][3]) == type(['this is a test']):
            subjects = ''
            for subject in studentList[personN][3]:
                subjects += subject + ','
            studentList[personN][3] = subjects[:len(subjects)-1]
    with open(STUDENT_FILE_PATH, 'w+', newline='') as databasething:
        writer = csv.writer(databasething)
        writer.writerow(studentList[0])
        writer.writerows(studentList[1:])

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
        user = [name, sha256(password.encode('utf-8')).hexdigest(), str(len(studentList)).rjust(4, "0"), subjectlist]
        csv.writer(databasething).writerow(user)
        return user


def seeHomework():
    global user
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
        if user[2] == studentList[randomUserN][2]:
            subjectlist = studentList[randomUserN][3].split(',')
            newsubjectlist = deepcopy(subjectlist)
            for subject in subjectlist:
                if subject in deletedSubjects:
                    newsubjectlist.remove(subject)
            studentList[randomUserN][3] = newsubjectlist
    rewriteDatabase()


def addSubject(addedSubjects):
    global user, studentList
    for randomUserN in range(len(studentList)):
        if user[2] == studentList[randomUserN][2]:
            studentList[randomUserN][3] += ',' + addedSubjects 
    rewriteDatabase()
            

def deleteAccount():
    global user, studentList
    for randomUserN in range(len(studentList)):
        if user[2] == studentList[randomUserN][2]:
            studentList.remove(user)
    rewriteDatabase()

if __name__ == '__main__':
    print(databaseprojectthing)
    fetchDatabase()
    
    print('Welcome to the student login page.')
    user = ['what', 'idk']
    while user[0] == 'what':
        print('Type "login" to login, "register" to register, and "exit" to exit.')
        command = input('>>> ')
        if command == 'login':
            admno = input('\nEnter your admission number: ')
            password = input('Enter your password: ')
            user = login(admno, password)
        elif command == '.': user = login('S001', '123456')
    
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
        if command == 'homework' or command == 'hw':
            homework = seeHomework()
            print(homework) # reformat this

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
            deleteSubjects(deletedSubjects.split(','))
            print('Here are your new subjects: ', *user[3].split(','))

        elif command == 'add-subject' or command == 'as':
            print('Here are the subjects you have not yet taken: ')
            untakenSubjects = deepcopy(SUBJECTS)
            for subj in untakenSubjects:
                if subj in user[3].split(','):
                    untakenSubjects.remove(subj)
            for subj in untakenSubjects:
                print('⋅', subj)
            error = 0
            while True:
                error = 0
                addedSubjects = input('Please enter all the subjects you want to add, separated by ",": ')
                for subject in addedSubjects.split(','):
                    if subject in user[3].split(','):
                        error = 1
                        print('Error: you entered a subject which you already have.')
                if error == 0: break
            addSubject(addedSubjects)
            print('Here are your new subjects: ', *user[3].split(','))

        elif command == 'delete-account' or command == 'da':
            if sha256(input('Are you sure? Please enter your password to delete your account.').encode('utf-8')).hexdigest() == user[1]:
                deleteAccount()
            else:
                print('Error: wrong password.')

        elif command == 'exit' or command == 'e': exit()
