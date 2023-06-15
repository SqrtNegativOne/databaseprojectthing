from collections import namedtuple
from difflib import SequenceMatcher
from hashlib import sha256
import pickle

FILE_PATH = "teacher_data.txt"
HW_FILE_PATH = "homework.txt"

teacher = namedtuple("teacher", ["name", "id", "subject", "password"]) 


def signup(name, subject, password) -> teacher:

    user = None
    with open(FILE_PATH, "rb") as f:
        while True:
            try:
                user = pickle.load(f)
            except EOFError:
                break
    
    _id = int(user.id[2:]) if user else 1

    emp_num  = "T" + subject.upper()[0] + str(_id).rjust(4, "0")
    password = sha256(password.encode("UTF-8")).hexdigest()

    user = teacher(name, emp_num, subject, password)

    with open(FILE_PATH, "ab") as f:
        pickle.dump(user, f)

    return user


def signin(_id, password) -> teacher:
    password = sha256(password.encode("UTF-8")).hexdigest()

    with open(FILE_PATH, "rb") as f:
        while True:
            try:
                user = pickle.load(f)
            except EOFError:
                return False
            if user.password == password and _id == user.id:
                return user


def edit_user_data(user, attrs, delete_user=False) -> None:

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
                if delete_user:
                    continue
                pickle.dump(user._replace(**attrs), f)
            else:
                pickle.dump(i, f)
    
    return user._replace(**attrs)


def assign_hw(user, homework, deadline) -> None:
    
    hw_data = "|".join([user.subject, deadline, homework]) + "\n" 
    
    with open(HW_FILE_PATH, "a") as f:   
        f.write(hw_data)


def search_users(keyword, name_search: bool, subj) -> list:

    users = []
    with open(FILE_PATH, "rb") as f:
        while True:
            try:
                user = pickle.load(f)
                user_criterion = user.name if name_search else user.id
                users.append((user, SequenceMatcher(None, keyword.lower(),
                                                    user_criterion.lower()).ratio()))
            except EOFError:
                break
    
    if subj:
        users = list(filter(lambda x: x[0].subject == subj, users))
    
    users.sort(key=lambda x: x[1], reverse=True)
    return [user[0] for user in users[:5] if user[1] > 0.3]
