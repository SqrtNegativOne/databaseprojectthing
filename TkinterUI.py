import teacher_backend as teacher
import student_backend as student
import tkinter.messagebox as mssg
import tkinter as tk
import random

SUBJECTS = ["english", "mathematics", "chemistry", "physics",
            "german", "Computer Science", "Physical Educations"]

databaseprojectthing = """
█▀▄░█▀█░▀█▀░█▀█░█▀▄░█▀█░█▀▀░█▀▀░░█▀█░█▀▄░█▀█░▀▀█░█▀▀░█▀▀░▀█▀░░▀█▀░█░█░▀█▀░█▀█░█▀▀
█░█░█▀█░░█░░█▀█░█▀▄░█▀█░▀▀█░█▀▀░░█▀▀░█▀▄░█░█░░░█░█▀▀░█░░░░█░░░░█░░█▀█░░█░░█░█░█░█
▀▀░░▀░▀░░▀░░▀░▀░▀▀░░▀░▀░▀▀▀░▀▀▀░░▀░░░▀░▀░▀▀▀░▀▀░░▀▀▀░▀▀▀░░▀░░░░▀░░▀░▀░▀▀▀░▀░▀░▀▀▀
"""

class App(tk.Tk):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.state("zoomed")
        self.title("Database Project thing")

        self.current_widgets = []
        self.user = None

        self.top_frm = tk.Frame(self)
        self.dwn_frm = tk.Frame(self)
        self.lft_frm = tk.Frame(self)
        self.rgt_frm = tk.Frame(self)
        self.mid_frm = tk.Frame(self)

        self.top_frm.pack(side="top", fill="x")
        self.dwn_frm.pack(side="bottom", fill="x")
        self.lft_frm.pack(side="left", fill="y")
        self.rgt_frm.pack(side="right", fill="y")
        self.mid_frm.pack(anchor="center", fill="both", expand=1)

        title_label = tk.Label(self.top_frm, text=databaseprojectthing, font="helvatica 15 bold")
        title_label.pack(anchor="center", pady=10)

        self.title_screen()

    def widget_clearer(func):
        def in_func(*args):
            for i in args[0].current_widgets:
                i.destroy()
            widgets = func(*args)
            args[0].current_widgets = widgets

        return in_func

    def signin(self, username, password, typ) -> bool:

        if typ == "Teacher":
            return teacher.signin(username, password)
        else:
            return student.login(username, password)


    @widget_clearer
    def signup(self) -> list:

        def verify_user():
            if len(ety1.get()) == 0:
                mssg.showwarning("Warning", "Name field cannot be empty")
            elif len(ety2.get()) < 5:
                mssg.showwarning("Warning", "Minimum password length must be 5 characters")
            elif typ.get() == "Teacher" and len(subj.curselection()) != 1:
                mssg.showwarning("Warning", "Please Select one Subject")
            elif typ.get() == "Student" and len(subj.curselection()) == 0:
                mssg.showwarning("Warning", "Please Select at least one Subject")
            else:
                if typ.get() == "Teacher":
                    teacher.signup(ety1.get(), SUBJECTS[subj.curselection()[0]], ety2.get())
                else:
                    student.register(ety1.get(), ety2.get(), [SUBJECTS[i] for i in subj.curselection()])
                self.homepage()
        
        def generate_password():
            password = [chr(random.randint(33, 122)) for _ in range(10)]
            random.shuffle(password)

            ety2.delete(0, "end")
            ety2.insert(0, "".join(password))
                

        box_frm = tk.Frame(self.mid_frm)
        box_frm.pack(anchor="center")

        typ  = tk.StringVar(value="Teacher")

        lbl1 = tk.Label(box_frm, text="Name: ")
        lbl2 = tk.Label(box_frm, text="Password: ")
        lbl3 = tk.Label(box_frm, text="Subject(s): ")
        ety1 = tk.Entry(box_frm)
        ety2 = tk.Entry(box_frm)
        subj = tk.Listbox(box_frm, selectmode="multiple")
        menu = tk.OptionMenu(box_frm, typ, "Teacher", "Student")


        ok_btn = tk.Button(box_frm, text="OK", command=verify_user)
        gn_btn = tk.Button(box_frm, text="Generate", command=generate_password)

        for i, j in enumerate(SUBJECTS):
            subj.insert(i, j.capitalize())

        lbl1.grid(row=0, column=0)
        lbl2.grid(row=1, column=0)
        lbl3.grid(row=2, column=0)
        ety1.grid(row=0, column=1)
        ety2.grid(row=1, column=1)
        subj.grid(row=2, column=1, pady=10)
        menu.grid(row=3, column=0, columnspan=2)
        ok_btn.grid(row=4, column=0, columnspan=2)
        gn_btn.grid(row=1, column=3)

        return [box_frm]
    

    @widget_clearer
    def title_screen(self) -> None:

        def signin_process():
            user = self.signin(ety1.get(), ety2.get(), typ.get())
            if user:
                self.user = user
                self.homepage(typ.get())
            else:
                mssg.showwarning("Warning", "Wrong Username or Password.\nPlease try again.")

        box_frm = tk.Frame(self.mid_frm)
        box_frm.pack(anchor="center")

        typ  = tk.StringVar(value="Teacher")

        lbl1 = tk.Label(box_frm, text="Username: ")
        lbl2 = tk.Label(box_frm, text="Password: ")
        ety1 = tk.Entry(box_frm)
        ety2 = tk.Entry(box_frm, show="*")
        menu = tk.OptionMenu(box_frm, typ, "Teacher", "Student")

        ok_btn = tk.Button(box_frm, text="OK", command=signin_process)
        su_btn = tk.Button(box_frm, text="Signup", command=self.signup)

        lbl1.grid(row=0, column=0)
        lbl2.grid(row=1, column=0)
        ety1.grid(row=0, column=1)
        ety2.grid(row=1, column=1)
        menu.grid(row=2, column=1)
        ok_btn.grid(row=3, column=0)
        su_btn.grid(row=3, column=1)

        return [box_frm]
    
    @widget_clearer
    def homepage(self, *args):
        ...


if __name__ == "__main__":
    app = App()
    app.mainloop()
