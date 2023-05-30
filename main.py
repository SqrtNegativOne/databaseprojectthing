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

        self.FONT = Font(family="Century Gothic", size=15)

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

        title_label = tk.Label(self.top_frm, text="Database Project Thing",
                               font=Font(family="Bahnschrift light", size=40))
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
        box_frm.pack(anchor="center", pady=60)

        utype_var = tk.IntVar(value=1)

        lbl1 = tk.Label(box_frm, text="Username", font=self.FONT)
        lbl2 = tk.Label(box_frm, text="Password", font=self.FONT)
        lbl3 = tk.Label(box_frm, text="Subjects", font=self.FONT)
        ety1 = tk.Entry(box_frm, relief="solid", width=30, font=self.FONT)
        ety2 = tk.Entry(box_frm, relief="solid", width=30, font=self.FONT)
        subj = tk.Listbox(box_frm, selectmode="multiple", activestyle="none",
                          justify="center", relief="sunken", width=20, height=7,
                          font=Font(family="Century Gothic", size=10))
        
        rbt1 = tk.Radiobutton(box_frm, text="Teacher", variable=utype_var, value=1, font=self.FONT)
        rbt2 = tk.Radiobutton(box_frm, text="Student", variable=utype_var, value=0, font=self.FONT)

        signup_btn = tk.Button(box_frm, text="Sign Up", font=self.FONT, relief="flat",
                               bg="#2C8CBE", command=verify_user)
        back_btn   = tk.Button(self.lft_frm, text="\u23CE", font=self.FONT, relief="groove",
                               command=self.title_screen)
        gen_btn    = tk.Button(box_frm, text="Generate", font=Font(family="Century Gothic", size=10),
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
        back_btn.pack(side="top", padx=20)
        signup_btn.grid(row=6, column=0, columnspan=2, sticky="ew")

        return [box_frm, back_btn]
    

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
        box_frm.pack(anchor="center", pady=60)
        
        utype_var = tk.IntVar(value=1)

        lbl1 = tk.Label(box_frm, text="Username", font=self.FONT)
        lbl2 = tk.Label(box_frm, text="Password", font=self.FONT)
        ety1 = tk.Entry(box_frm, relief="solid", width=30, font=self.FONT)
        ety2 = tk.Entry(box_frm, relief="solid", width=30, font=self.FONT, show="*")

        rbt1 = tk.Radiobutton(box_frm, text="Teacher", variable=utype_var, value=1, font=self.FONT)
        rbt2 = tk.Radiobutton(box_frm, text="Student", variable=utype_var, value=0, font=self.FONT)

        signin_btn = tk.Button(box_frm, text="Sign in", font=self.FONT, relief="flat",
                               bg="#2C8CBE", command=signin_process)
        signup_btn = tk.Button(box_frm, text="Sign up", font=Font(family="Century Gothic", size=15, underline=True), relief="flat",
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
    

    def init_search_bar(self) -> object:

        suggestions = []

        def callback(*_):
            nonlocal place_1, suggestions

            suggestions = teacher.search_users(text_var.get(), filt_var.get())

            if suggestions and text_var.get():
                if not place_1:
                    search_box.grid(row=2, column=0, columnspan=3)
                    place_1 = True

                search_box.delete(0, "end")
                search_box["height"] = len(suggestions)
                for i, user in enumerate(suggestions):
                    search_box.insert(i, f"{user.name.capitalize()}#{user.emp_no}  >{user.subject}")
            else:
                search_box.grid_forget()
                place_1 = False
        
        def search():
            if search_box.curselection():
                user = suggestions[search_box.curselection()[0]]
                self.user_profile(user)

        def show_filters():
            nonlocal place_2
            if not place_2:
                filter_frm.grid(row=1, column=0, columnspan=3)
                place_2 = True
            else:
                filter_frm.grid_forget()
                place_2 = False

        text_var = tk.StringVar(self)
        filt_var = tk.IntVar(self, value=1)
        text_var.trace("w", callback)
        place_1 = place_2 = False
        
        filter_frm = tk.Frame(self.rgt_frm)
        search_bar = tk.Entry(self.rgt_frm, textvariable=text_var, font=self.FONT, width=18)
        search_box = tk.Listbox(self.rgt_frm, selectmode="single", activestyle="dotbox",
                          justify="left", relief="flat", width=30,
                          font=Font(family="Century Gothic", size=10))
        search_btn = tk.Button(self.rgt_frm, text="\U0001F50D", command=search)
        filter_btn = tk.Button(self.rgt_frm, text="\u25BC", command=show_filters)

        lbl1 = tk.Label(filter_frm, text="Search by: ", font=Font(family="Century Gothic", size=10))
        rbt1 = tk.Radiobutton(filter_frm, value=1, variable=filt_var, text="Username",
                              font=Font(family="Century Gothic", size=10))
        rbt2 = tk.Radiobutton(filter_frm, value=0, variable=filt_var, text="Emp No.",
                              font=Font(family="Century Gothic", size=10))
        
        lbl1.grid(row=0, column=0, columnspan=2)
        rbt1.grid(row=1, column=0)
        rbt2.grid(row=1, column=1)

        search_bar.grid(row=0, column=0)
        search_btn.grid(row=0, column=1, padx=5)
        filter_btn.grid(row=0, column=2)


    @widget_clearer
    def homepage_teacher(self) -> list:
        print(self.user)
        self.init_search_bar()

        return []

        

    @widget_clearer
    def homepage_student(self) -> list:
        print(self.user)
        self.init_search_bar()

        return []
    
    @widget_clearer
    def user_profile(self, user) -> list:
        a = tk.Label(self.mid_frm, text=repr(user))
        a.pack()

        return [a] 


if __name__ == "__main__":
    app = App()
    app.mainloop()
