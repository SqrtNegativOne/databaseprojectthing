from copy import deepcopy
from os import remove, rename
from hashlib import sha256
import csv

databaseprojectthing ="""
█▀▄░█▀█░▀█▀░█▀█░█▀▄░█▀█░█▀▀░█▀▀░█▀█░█▀▄░█▀█░▀▀█░█▀▀░█▀▀░▀█▀░▀█▀░█░█░▀█▀░█▀█░█▀▀
█░█░█▀█░░█░░█▀█░█▀▄░█▀█░▀▀█░█▀▀░█▀▀░█▀▄░█░█░░░█░█▀▀░█░░░░█░░░█░░█▀█░░█░░█░█░█░█
▀▀░░▀░▀░░▀░░▀░▀░▀▀░░▀░▀░▀▀▀░▀▀▀░▀░░░▀░▀░▀▀▀░▀▀░░▀▀▀░▀▀▀░░▀░░░▀░░▀░▀░▀▀▀░▀░▀░▀▀▀"""

# user = [name, password, admno, Subjects]

FILE_PATH = 'students.csv'
HW_FILE_PATH = 'homework.txt'
SUBJECTS = ["English", "Mathematics", "Chemistry", "Physics",
            "German", "Computer Science", "Physical Education"]

studentList = []

def fetchDatabase():
    global studentList
    with open(FILE_PATH, 'r+') as databasething:
        studentList = list(csv.reader(databasething))

def rewriteDatabase():
    tmpFile = "tmp.csv"

    with open(tmpFile, "w", newline='') as f:
        writer = csv.writer(f, delimiter=',')

        for user in studentList:
            writer.writerow(user)
    
    remove(FILE_PATH)
    rename(tmpFile, FILE_PATH)
    
def getUser(admo):
    global studentList, user
    fetchDatabase()
    for row in studentList:
        if row[2] == admo:
            user = row
    return user

def signin(admno, password):
    fetchDatabase()
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
    fetchDatabase()
    admn_no = "ST" + str(int(studentList[-1][2][2:]) + 1).rjust(4, "0") if studentList else "ST0001"
    with open(FILE_PATH, 'a', newline='') as databasething:
        user = [name, sha256(password.encode('utf-8')).hexdigest(), admn_no, subjectlist]
        csv.writer(databasething).writerow(user)
        return user


def homework(subject, all_=False):
    fetchDatabase()
    with open(HW_FILE_PATH, 'r') as hw:
        homeworkList = [item.strip("\n").split("|") for item in hw.readlines()]
    validHomeworks = []

    for homework in homeworkList:
        if homework[0] == subject or all_:
            validHomeworks.append(homework)
    return validHomeworks

def deleteSubjects(user, deletedSubjects):
    global studentList
    fetchDatabase()
    for randomUserN in range(len(studentList)):
        if user[2] == studentList[randomUserN][2]:
            studentList[randomUserN][3] = ",".join(list(set(user[3].split(",")) - set(deletedSubjects)))
    rewriteDatabase()


def addSubject(user, addedSubjects):
    fetchDatabase()
    global studentList
    for randomUserN in range(len(studentList)):
        if user[2] == studentList[randomUserN][2]:
            studentList[randomUserN][3] += ',' + addedSubjects 
    rewriteDatabase()


def change_password(user, password):
    fetchDatabase()
    global studentList
    for randomUserN in range(len(studentList)):
        if user[2] == studentList[randomUserN][2]:
            studentList[randomUserN][1] = password
    rewriteDatabase()

def change_name(user, name):
    fetchDatabase()
    global studentList
    for randomUserN in range(len(studentList)):
        if user[2] == studentList[randomUserN][2]:
            studentList[randomUserN][0] = name
    rewriteDatabase()      

def deleteAccount(user):
    fetchDatabase()
    global studentList

    for randomUserN in range(len(studentList)):
        if user[2] == studentList[randomUserN][2]:
            studentList.remove(user)
            break
    rewriteDatabase()
