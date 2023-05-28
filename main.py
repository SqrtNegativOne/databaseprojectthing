import teacher_backend as teacher
import student_backend as student
import tkinter.messagebox as mssg
from tkinter.font import Font
import tkinter as tk
import random

SUBJECTS = ["english", "mathematics", "chemistry", "physics",
            "german", "Computer Science", "Physical Education"]

databaseprojectthing = """
░█▀▄░█▀█░▀█▀░█▀█░█▀▄░█▀█░█▀▀░█▀▀░░█▀█░█▀▄░█▀█░▀▀█░█▀▀░█▀▀░▀█▀░░▀█▀░█░█░▀█▀░█▀█░█▀▀
░█░█░█▀█░░█░░█▀█░█▀▄░█▀█░▀▀█░█▀▀░░█▀▀░█▀▄░█░█░░░█░█▀▀░█░░░░█░░░░█░░█▀█░░█░░█░█░█░█
░▀▀░░▀░▀░░▀░░▀░▀░▀▀░░▀░▀░▀▀▀░▀▀▀░░▀░░░▀░▀░▀▀▀░▀▀░░▀▀▀░▀▀▀░░▀░░░░▀░░▀░▀░▀▀▀░▀░▀░▀▀▀
"""

class App(tk.Tk):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.state("zoomed")
        self.title("Database Project thing")

        self.current_widgets = []
        self.user = None

        self.FONT = Font(family="Cambria", size=15)

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


    @widget_clearer
    def signup(self) -> list:

        def verify_user():
            if len(ety1.get()) == 0:
                mssg.showwarning("Warning", "Name field cannot be empty")
            elif len(ety2.get()) < 5:
                mssg.showwarning("Warning", "Minimum password length must be 5 characters")
            elif utype_var.get() == 1 and len(subj.curselection()) != 1:
                mssg.showwarning("Warning", "Please Select one Subject")
            elif utype_var.get() == 0 and len(subj.curselection()) == 0:
                mssg.showwarning("Warning", "Please Select at least one Subject")
            else:
                if utype_var.get():
                    self.user = teacher.signup(ety1.get(), SUBJECTS[subj.curselection()[0]], ety2.get())
                else:
                    self.user = student.register(ety1.get(), ety2.get(), [SUBJECTS[i] for i in subj.curselection()]) 
                self.homepage_teacher() if utype_var.get() else self.homepage_student()
        
        def generate_password():
            password = [chr(random.randint(33, 122)) for _ in range(10)]
            random.shuffle(password)

            ety2.delete(0, "end")
            ety2.insert(0, "".join(password))
                

        box_frm = tk.Frame(self.mid_frm)
        box_frm.pack(anchor="center")

        utype_var = tk.IntVar(value=1)

        lbl1 = tk.Label(box_frm, text="Username", font=self.FONT)
        lbl2 = tk.Label(box_frm, text="Password", font=self.FONT)
        lbl3 = tk.Label(box_frm, text="Subjects", font=self.FONT)
        ety1 = tk.Entry(box_frm, relief="solid", width=30, font=self.FONT)
        ety2 = tk.Entry(box_frm, relief="solid", width=30, font=self.FONT)
        subj = tk.Listbox(box_frm, selectmode="multiple", activestyle="none",
                          justify="center", relief="sunken", width=20, height=7,
                          font=Font(family="Cambria", size=10))
        
        rbt1 = tk.Radiobutton(box_frm, text="Teacher", variable=utype_var, value=1, font=self.FONT)
        rbt2 = tk.Radiobutton(box_frm, text="Student", variable=utype_var, value=0, font=self.FONT)

        signup_btn = tk.Button(box_frm, text="Sign Up", font=self.FONT, relief="flat",
                               bg="#2C8CBE", command=verify_user)
        gen_btn    = tk.Button(box_frm, text="Generate", font=Font(family="Cambria", size=10),
                               command=generate_password)

        for i, j in enumerate(SUBJECTS):
            subj.insert(i, j.capitalize())

        lbl1.grid(row=0, column=0, sticky="w")
        ety1.grid(row=1, column=0, columnspan=2)
        lbl2.grid(row=2, column=0, sticky="w")
        ety2.grid(row=3, column=0, columnspan=2)
        lbl3.grid(row=4, column=0)
        subj.grid(row=4, column=1, sticky="nsew", pady=(15, 0))
        rbt1.grid(row=5, column=0)
        rbt2.grid(row=5, column=1)
        gen_btn.grid(row=3, column=2, padx=5)
        signup_btn.grid(row=6, column=0, columnspan=2, sticky="ew")

        return [box_frm]
    

    @widget_clearer
    def title_screen(self) -> None:

        def signin_process():

            if utype_var.get():
                user = teacher.signin(ety1.get(), ety2.get())
            else:
                user = student.login(ety1.get(), ety2.get())
                
            if user:
                self.user = user
                self.homepage_teacher() if utype_var.get() else self.homepage_student()
            else:
                mssg.showwarning("Warning", "Wrong Username or Password.\nPlease try again.")

        box_frm = tk.Frame(self.mid_frm)
        box_frm.pack(anchor="center")
        
        utype_var = tk.IntVar(value=1)

        lbl1 = tk.Label(box_frm, text="Username", font=self.FONT)
        lbl2 = tk.Label(box_frm, text="Password", font=self.FONT)
        ety1 = tk.Entry(box_frm, relief="solid", width=30, font=self.FONT)
        ety2 = tk.Entry(box_frm, relief="solid", width=30, font=self.FONT, show="*")

        rbt1 = tk.Radiobutton(box_frm, text="Teacher", variable=utype_var, value=1, font=self.FONT)
        rbt2 = tk.Radiobutton(box_frm, text="Student", variable=utype_var, value=0, font=self.FONT)

        signin_btn = tk.Button(box_frm, text="Sign in", font=self.FONT, relief="flat",
                               bg="#2C8CBE", command=signin_process)
        signup_btn = tk.Button(box_frm, text="Sign up", font=self.FONT, relief="flat",
                               fg="blue", cursor="hand2", command=self.signup)

        lbl1.grid(row=0, column=0, sticky="w")
        ety1.grid(row=1, column=0, columnspan=2)
        lbl2.grid(row=2, column=0, sticky="w")
        ety2.grid(row=3, column=0, columnspan=2)
        rbt1.grid(row=4, column=0)
        rbt2.grid(row=4, column=1)
        signin_btn.grid(row=5, column=0, sticky="ew", columnspan=2)
        signup_btn.grid(row=6, column=0, sticky="nw")

        return [box_frm]
    

    @widget_clearer
    def homepage_teacher(self) -> list:
        print(self.user)
    

    @widget_clearer
    def homepage_student(self) -> list:
        print(self.user)


if __name__ == "__main__":
    app = App()
    app.mainloop()
