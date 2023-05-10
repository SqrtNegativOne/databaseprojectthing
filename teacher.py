from collections import namedtuple
import pickle

FILE_PATH = ...

teacher = namedtuple("teacher", ["name", "adm_no", "subject", "password"])

def signup(user):
    with open(FILE_PATH, "wb") as f:
        pickle.dump(user, f)

def signin(password) -> bool:
    with open(FILE_PATH, "rb") as f:
        while True:
            try:
                user = pickle.load(f)
            except EOFError:
                return False
            if user["password"] == password:
                return user

def edit_user_data(user) -> bool:
    with open(FILE_PATH, "rb") as f:
        while True:
            try:
                data = pickle.load(f)
            except EOFError:
                return False
            if data == user:
                break
        
    with open(File)
