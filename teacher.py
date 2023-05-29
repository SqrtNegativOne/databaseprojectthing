from collections import namedtuple
from difflib import SequenceMatcher
from hashlib import sha256
import pickle
import os

databaseprojectthing = """
░█▀▄░█▀█░▀█▀░█▀█░█▀▄░█▀█░█▀▀░█▀▀░░█▀█░█▀▄░█▀█░▀▀█░█▀▀░█▀▀░▀█▀░░▀█▀░█░█░▀█▀░█▀█░█▀▀
░█░█░█▀█░░█░░█▀█░█▀▄░█▀█░▀▀█░█▀▀░░█▀▀░█▀▄░█░█░░░█░█▀▀░█░░░░█░░░░█░░█▀█░░█░░█░█░█░█
░▀▀░░▀░▀░░▀░░▀░▀░▀▀░░▀░▀░▀▀▀░▀▀▀░░▀░░░▀░▀░▀▀▀░▀▀░░▀▀▀░▀▀▀░░▀░░░░▀░░▀░▀░▀▀▀░▀░▀░▀▀▀
"""

FILE_PATH = "teacher_data.txt"
HW_FILE_PATH = "homework.txt"

teacher = namedtuple("teacher", ["name", "emp_no", "subject", "password"])


def signup(name, subject, password) -> teacher:

    emp_num = 0

    with open(FILE_PATH, "rb") as f:
        while True:
            try:
                pickle.load(f)
                emp_num += 1
            except EOFError:
                break
   
    emp_num  = "T" + {subject.upper()[0]} + str(emp_num).rjust(4, "0")
    password = sha256(password.encode("UTF-8")).hexdigest()

    user = teacher(name, emp_num, subject, password)

    with open(FILE_PATH, "ab") as f:
        pickle.dump(user, f)
    
    return user

def signin(emp_no, password) -> teacher:
    password = sha256(password.encode("UTF-8")).hexdigest()

    with open(FILE_PATH, "rb") as f:
        while True:
            try:
                user = pickle.load(f)
            except EOFError:
                return False
            if user.password == password and emp_no == user.emp_no:
                return user

def edit_user_data(user, attrs) -> None:

    data = []

    with open(FILE_PATH, "rb") as f:
        while True:
            try:
                data.append(pickle.load(f))
            except EOFError:
                break
   
    with open(FILE_PATH, "wb") as f:
        for i in data:
            if i == user:
                pickle.dump(user._replace(**attrs), f)
            else:
                pickle.dump(i, f)
    
    return user._replace(**attrs)

def assign_hw(user, hw_data) -> None:

    with open(HW_FILE_PATH, "a") as f:   
        f.write(user.subject.upper().ljust(10) + hw_data)

def search_users(keyword, name_search: bool) -> list:

    users = []    
    with open(FILE_PATH, "rb") as f:
        while True:
            try:
                user = pickle.load(f)
                user_criterion = user.name if name_search else user.emp_no
                users.append((user, SequenceMatcher(None, keyword, user_criterion).ratio()))
            except EOFError:
                break
    
    users.sort(key=lambda x: x[1], reverse=True)[5:]
    return [user[0] for user in users if users[1] > 0.6]


def print_banner(subtext=None) -> None:
    os.system("cls")
    print(databaseprojectthing)
    if subtext:
        print(subtext)
    print()

if __name__ == "__main__":
    user = None
    subtext = "Welcome!"

    while not user:
        print_banner(subtext)
        login_state = input("Signin/Signup/Exit: ").casefold()

        if login_state == "signin":
            username = input("Employee Number: ")
            password = input("Password: ")
            user = signin(username, password)

        elif login_state == "signup":
            name     = input("Name: ")
            subject  = input("Subject: ")
            password = input("Password: ")
            user = signup(teacher(name, None, subject, password))
        
        elif login_state == "exit":
            exit()

        else:
            input("\n\u26A0 Invalid prompt.\nPress Enter to continue.")


    while True:
        print_banner(f"Signed in as: \t\t{user.name.capitalize()}#{user.emp_no}")

        print("Commands:\n| Edit Personal Data (1)| Assign Homework (2) | Exit (3) |")
        command = input(">>>").casefold()

        if command == "1": #edit personal data
            field = input("Field name: ")
            value = input("New Value: ")

            try: 
                user = edit_user_data(user, {field: value})
            except ValueError:
                input("\n\u26A0 Invalid prompt.\nPress Enter to continue.")

        elif command == "2": #assign homework
            ...
        
        elif command == "3": #exit
            exit()
        
        else:
            input("\n\u26A0 Invalid prompt.\nPress Enter to continue.")

