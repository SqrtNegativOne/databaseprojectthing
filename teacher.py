from collections import namedtuple
import pickle

FILE_PATH = "teacher_data.txt"

teacher = namedtuple("teacher", ["name", "adm_no", "subject", "password"])

def signup(user):
    with open(FILE_PATH, "ab") as f:
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

def edit_user_data(user, attrs) -> bool:

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

# signup(teacher("karan", 7439, "phy", "cat"))
# signup(teacher("acide", 7436, "chm", "dog"))

# with open(FILE_PATH, "r+b") as f:
#     while True:
#         try:
#             print(pickle.load(f))
#         except EOFError:
#             break

# edit_user_data(teacher("karan", 7439, "phy", "cat"), {"name":"koooo"})

# with open(FILE_PATH, "r+b") as f:
#     while True:
#         try:
#             print(pickle.load(f))
#         except EOFError:
#             break
