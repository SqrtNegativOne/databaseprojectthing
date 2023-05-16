from collections import namedtuple
import pickle

FILE_PATH = "teacher_data.txt"
HW_FILE_PATH = "homework.txt"

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

def assign_hw(user, hw_data) -> None:

    with open(HW_FILE_PATH, "a") as f:
       
        f.write(user.subject.upper().ljust(10) + hw_data)
   

signup(teacher("karan", 7439, "phy", "cat"))
signup(teacher("acide", 7436, "chm", "dog"))
signup(teacher("topper", 1000, "PE", "PCC"))

with open(FILE_PATH, "r+b") as f:
    while True:
        try:
            print(pickle.load(f))
        except EOFError:
            break

edit_user_data(teacher("karan", 7439, "phy", "cat"), {"name":"koooo"})
print("-"*10)

with open(FILE_PATH, "r+b") as f:
    while True:
        try:
            print(pickle.load(f))
        except EOFError:
            break

assign_hw(teacher("koooo", 7439, "phy", "cat"), "DO UR WORK NOWWWW!!!!!!!!!!!!!!!!!")

with open(HW_FILE_PATH, "r") as f:
    print(f.read())
