import csv

databaseprojectthing = """
░█▀▄░█▀█░▀█▀░█▀█░█▀▄░█▀█░█▀▀░█▀▀░░█▀█░█▀▄░█▀█░▀▀█░█▀▀░█▀▀░▀█▀░░▀█▀░█░█░▀█▀░█▀█░█▀▀
░█░█░█▀█░░█░░█▀█░█▀▄░█▀█░▀▀█░█▀▀░░█▀▀░█▀▄░█░█░░░█░█▀▀░█░░░░█░░░░█░░█▀█░░█░░█░█░█░█
░▀▀░░▀░▀░░▀░░▀░▀░▀▀░░▀░▀░▀▀▀░▀▀▀░░▀░░░▀░▀░▀▀▀░▀▀░░▀▀▀░▀▀▀░░▀░░░░▀░░▀░▀░▀▀▀░▀░▀░▀▀▀
                                                                                                                                                                          
"""
print(databaseprojectthing)
print('Welcome to the student login page.')
with open('students.csv', 'r+') as databasething:
    studentList = list(csv.reader(databasething))
    print(studentList)
while True:
    name = input('Enter your name: ') # I would have used a walrus operator, but the computer lab only has python 3.7, not the required python 3.8 :harold:
    if name not in [row[0] for row in studentList]:
        print('Error: name was not found in student database. Kindly contact the school administrator.')
    else:
        admno = input('Enter your admission number: ')
        if admno not in [row[1] for row in studentList]:
            print('Error: wrong admission number. Make sure your name wasn\'t mispelled.')
        else:
            # Now it begins.
            pass
    if input('Continue? (y/n): ') == 'n':
        break
