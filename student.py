import csv
import time

databaseprojectthing = """
█▀▄░█▀█░▀█▀░█▀█░█▀▄░█▀█░█▀▀░█▀▀░█▀█░█▀▄░█▀█░▀▀█░█▀▀░█▀▀░▀█▀░▀█▀░█░█░▀█▀░█▀█░█▀▀
█░█░█▀█░░█░░█▀█░█▀▄░█▀█░▀▀█░█▀▀░█▀▀░█▀▄░█░█░░░█░█▀▀░█░░░░█░░░█░░█▀█░░█░░█░█░█░█
▀▀░░▀░▀░░▀░░▀░▀░▀▀░░▀░▀░▀▀▀░▀▀▀░▀░░░▀░▀░▀▀▀░▀▀░░▀▀▀░▀▀▀░░▀░░░▀░░▀░▀░▀▀▀░▀░▀░▀▀▀
                                                                                                                                                                          
"""
print(databaseprojectthing)

subjects = ['Physics', 'Chemistry', 'Mathematics', 'Biology', 'Computer Science' 'Physical Education']

STUDENT_FILE_PATH = 'students.csv'
HW_FILE_PATH = 'homework.txt'


print('Welcome to the student login page.')
with open(STUDENT_FILE_PATH, 'r+') as databasething:
    studentList = list(csv.reader(databasething))
    print(studentList)

def register():
    global studentList
    with open(STUDENT_FILE_PATH, 'a', newline='') as databasething:
        writerObject = csv.writer(databasething)
        writerObject.writerow([input('Name: '), hash(input('Password: ')), len(studentList), input('Subjects, separated by a comma (no space in between!): ')])
        print('⇒', len(studentList), 'is your admission number. Use this to login next time.')
        time.sleep(5)


def logined(user):
    global studentList
    print('You are now logged in.')
    print('homework: Checks all homework assigned to you.\ndelete subject: delete a subject\nadd subject: add a subject.')
    answer = input('>>>')
    if answer == 'homework':
        with open(HW_FILE_PATH, 'r') as hw:
            print(hw.readlines())
            # THIS CODE IS NOT COMPLETE. can only be completed afte talkng to karan about how to manage the text file
            homeworkList = [item for item in hw.readlines()]
            print(homeworkList)
            # Homework Subject Deadline
        for homework in homeworkList:
            if homework[1] in user[3].split(','):
                print(str(homework[1]) + ': '+ str(homework[0]) + '(Deadline: ' + str(homework[3]) + ')')
    elif answer == 'delete subject':
        while True:
            ...
            # WORK FROM HERE
    else:
        print('What?')



admno = input('Enter your admission number: ') # I would have used a walrus operator, but the computer lab only has python 3.7, not the required python 3.8 :harold:
if admno not in [row[2] for row in studentList]:
    if input('Error: Admission number not found in student database; would you register instead? (y/n)') == 'y': register()
else:
    for row in studentList:
        if row[2] == admno:
            user = row
    print(user)
    password = hash(input('Password: ')) # Password for Ark Malhotra = 123456
    print(password)
    if password != int(user[1]):
        print('Error: wrong password.')
    else:
        print('karan is  the best')
        logined(user)
