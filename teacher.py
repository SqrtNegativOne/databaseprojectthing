from collections import namedtuple
from difflib import SequenceMatcher
from hashlib import sha256
import pickle

databaseprojectthing = """
░█▀▄░█▀█░▀█▀░█▀█░█▀▄░█▀█░█▀▀░█▀▀░░█▀█░█▀▄░█▀█░▀▀█░█▀▀░█▀▀░▀█▀░░▀█▀░█░█░▀█▀░█▀█░█▀▀
░█░█░█▀█░░█░░█▀█░█▀▄░█▀█░▀▀█░█▀▀░░█▀▀░█▀▄░█░█░░░█░█▀▀░█░░░░█░░░░█░░█▀█░░█░░█░█░█░█
░▀▀░░▀░▀░░▀░░▀░▀░▀▀░░▀░▀░▀▀▀░▀▀▀░░▀░░░▀░▀░▀▀▀░▀▀░░▀▀▀░▀▀▀░░▀░░░░▀░░▀░▀░▀▀▀░▀░▀░▀▀▀
"""

FILE_PATH = "teacher_data.txt"
HW_FILE_PATH = "homework.txt"

teacher = namedtuple("teacher", ["name", "emp_no", "subject", "password"])


def signup(name, subject, password) -> teacher:

    emp_num = 1

    with open(FILE_PATH, "rb") as f:
        while True:
            try:
                pickle.load(f)
                emp_num += 1
            except EOFError:
                break
   
    emp_num  = "T" + subject.upper()[0] + str(emp_num).rjust(4, "0")
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
                users.append((user, SequenceMatcher(None, keyword.lower(), user_criterion.lower()).ratio()))
            except EOFError:
                break
    
    users.sort(key=lambda x: x[1], reverse=True)
    return [user[0] for user in users[:5] if user[1] > 0.25]

