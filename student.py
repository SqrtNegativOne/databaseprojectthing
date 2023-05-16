import csv

databaseprojectthing = """
░█▀▄░█▀█░▀█▀░█▀█░█▀▄░█▀█░█▀▀░█▀▀░░█▀█░█▀▄░█▀█░▀▀█░█▀▀░█▀▀░▀█▀░░▀█▀░█░█░▀█▀░█▀█░█▀▀
░█░█░█▀█░░█░░█▀█░█▀▄░█▀█░▀▀█░█▀▀░░█▀▀░█▀▄░█░█░░░█░█▀▀░█░░░░█░░░░█░░█▀█░░█░░█░█░█░█
░▀▀░░▀░▀░░▀░░▀░▀░▀▀░░▀░▀░▀▀▀░▀▀▀░░▀░░░▀░▀░▀▀▀░▀▀░░▀▀▀░▀▀▀░░▀░░░░▀░░▀░▀░▀▀▀░▀░▀░▀▀▀
                                                                                                                                                                          
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
        writerObject.writerow([input('Name: '), hash(input('Password: ')), len(studentList)+1, input('Subjects, separated by a space: ').split()])
        print(len(studentList), 'is your admission number. Use this to login.')


def logined(admo):
    global studentList
    print('You are now logged in.')
    print('homework: Checks all homework assigned to you.\nDelete subject: delete a subject\nAdd subject: add a subject.')
    answer = input('>>>')
    if answer == 'homework':
        with open(HW_FILE_PATH, 'r') as hw:
            pass


admno = input('Enter your admission number: ') # I would have used a walrus operator, but the computer lab only has python 3.7, not the required python 3.8 :harold:
if admno not in [row[0] for row in studentList]:
    print('Error: name was not found in student database...')
else:
    password = input('Password: ')
    if hash(password) not in [row[1] for row in studentList]:
        print('Error: wrong password.')
    else:
        logined(admno)
