import teacher_backend as teacher
import student_backend as student
import tkinter.messagebox as mssg
from tkinter.font import Font
import tkinter.ttk as ttk
import tkinter as tk
import random

SUBJECTS = ["English", "Mathematics", "Chemistry", "Physics",
            "German", "Computer Science", "Physical Education"]

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
                
                self.init_homescreen()
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
        back_btn   = tk.Button(self.lft_frm, text="\u21A9", font=self.FONT, relief="groove",
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
    def title_screen(self) -> list:

        def signin_process():

            if utype_var.get():
                user = teacher.signin(ety1.get(), ety2.get())
            else:
                user = student.login(ety1.get(), ety2.get())
                
            if user:
                self.user = user
                self.init_homescreen()
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
    

    def init_homescreen(self) -> None:

        suggestions = []

        def callback(*_):
            nonlocal place_1, suggestions

            suggestions = teacher.search_users(text_var.get(), filt_var.get(),
                                               subj_var.get() if subj_var.get() in SUBJECTS else None)

            if suggestions and text_var.get():
                if not place_1:
                    search_box.grid(row=2, column=0, columnspan=3)
                    place_1 = True

                search_box.delete(0, "end")
                search_box["height"] = len(suggestions)
                for i, user in enumerate(suggestions):
                    search_box.insert(i, user.name.capitalize().ljust(25) + f"#{user.emp_no}")
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
                filter_btn["text"] = "\u25B2"
            else:
                filter_frm.grid_forget()
                place_2 = False
                filter_btn["text"] = "\u25BC"

        text_var = tk.StringVar(self)
        filt_var = tk.IntVar(self, value=1)
        subj_var = tk.StringVar(self, value="Subject")
        place_1 = place_2 = False
        
        text_var.trace("w", callback)
        filt_var.trace("w", callback)
        subj_var.trace("w", callback)

        filter_frm = tk.Frame(self.rgt_frm)
        search_bar = tk.Entry(self.rgt_frm, textvariable=text_var, font=self.FONT, width=18)
        search_box = tk.Listbox(self.rgt_frm, selectmode="single", activestyle="dotbox",
                          justify="left", relief="flat", width=30,
                          font=Font(family="Century Gothic", size=10))
        
        search_btn = tk.Button(self.rgt_frm, text="\U0001F50D", command=search)
        filter_btn = tk.Button(self.rgt_frm, text="\u25BC", command=show_filters)

        rbt1 = tk.Radiobutton(filter_frm, value=1, variable=filt_var, text="Username",
                              font=Font(family="Century Gothic", size=10))
        rbt2 = tk.Radiobutton(filter_frm, value=0, variable=filt_var, text="Emp No.",
                              font=Font(family="Century Gothic", size=10))
        cbox = ttk.Combobox(filter_frm, values=SUBJECTS + [None], textvariable=subj_var,
                              font=Font(family="Century Gothic", size=10))

        self.banner1 = tk.Label(self.lft_frm, text=f"Signed in as:\n{self.user.name} #{self.user.emp_no}",
                        font=self.FONT)

        hom_btn = tk.Button(self.lft_frm, relief="flat", font=self.FONT, text="Home",
                            bg="#2C8CBE", fg="white", command=self.homepage_teacher)
        prf_btn = tk.Button(self.lft_frm, relief="flat", font=self.FONT, text="Profile",
                            bg="#2C8CBE", fg="white", command=lambda: self.user_profile(self.user, True))
        hwk_btn = tk.Button(self.lft_frm, relief="flat", font=self.FONT, text="Homework",
                            bg="#2C8CBE", fg="white", command=...)
        grd_btn = tk.Button(self.lft_frm, relief="flat", font=self.FONT, text="Grades",
                            bg="#2C8CBE", fg="white", command=...)
        atn_btn = tk.Button(self.lft_frm, relief="flat", font=self.FONT, text="Attendence",
                            bg="#2C8CBE", fg="white", command=...)
        
        rbt1.grid(row=0, column=0)
        rbt2.grid(row=0, column=1)
        cbox.grid(row=1, column=0, columnspan=2, pady=5)

        search_bar.grid(row=0, column=0)
        search_btn.grid(row=0, column=1, padx=5)
        filter_btn.grid(row=0, column=2)
        
        self.banner1.grid(row=0, column=0, sticky="nsew", pady=2)
        hom_btn.grid(row=1, column=0, sticky="nsew", pady=2)
        prf_btn.grid(row=2, column=0, sticky="nsew", pady=2)
        hwk_btn.grid(row=3, column=0, sticky="nsew", pady=2)
        grd_btn.grid(row=4, column=0, sticky="nsew", pady=2)
        atn_btn.grid(row=5, column=0, sticky="nsew", pady=2)


    @widget_clearer
    def homepage_teacher(self) -> list:
        ...
        return []
    

    @widget_clearer
    def homepage_student(self) -> list:
        ...
        return []
    

    @widget_clearer
    def user_profile(self, user, edit=False) -> list:

        def edit_mode():
            def confirm_edits():
                if not mssg.askyesno("Edit Changes", "Confirm Changes?"):
                    return
                
                ety1.destroy()
                ety3.destroy()
                ok_btn.destroy()

                emp_no = "T" + subj_var.get()[0].upper() + user.emp_no[2:]

                self.user = teacher.edit_user_data(user, {"name" : name_var.get(),
                                                          "emp_no" : emp_no,
                                                          "subject" : subj_var.get()})

                self.banner1.configure(text=f"Signed in as:\n{self.user.name} #{self.user.emp_no}")
                lbl2b.configure(text=emp_no)

                lbl1b.grid(row=1, column=0, sticky="w")
                lbl3b.grid(row=5, column=0, sticky="w")
                edit_btn.grid(row=6, column=0, sticky="w")

            lbl1b.grid_forget()
            lbl3b.grid_forget()
            edit_btn.grid_forget()

            ety1 = tk.Entry(box_frm, justify="left", font=self.FONT, textvariable=name_var)
            ety3 = ttk.Combobox(box_frm, justify="left", values=SUBJECTS, font=self.FONT, textvariable=subj_var)
            ok_btn = tk.Button(box_frm, text="OK", font=self.FONT, command=confirm_edits)

            ety1.grid(row=1, column=0, sticky="w")
            ety3.grid(row=5, column=0, sticky="w")
            ok_btn.grid(row=6, column=0, sticky="w")

        box_frm = tk.Frame(self.mid_frm)
        box_frm.pack(side="top", anchor="center", pady=50)

        FONT2 = Font(family="Century Gothic", weight="bold")

        name_var = tk.StringVar(value=user.name.capitalize())
        subj_var = tk.StringVar(value=user.subject)

        lbl1a = tk.Label(box_frm, justify="left", font=FONT2, text="NAME")
        lbl2a = tk.Label(box_frm, justify="left", font=FONT2, text="EMPLOYEE NUMBER")
        lbl3a = tk.Label(box_frm, justify="left", font=FONT2, text="SUBJECTS")

        lbl1b = tk.Label(box_frm, justify="left", font=self.FONT, textvariable=name_var)
        lbl2b = tk.Label(box_frm, justify="left", font=self.FONT, text=self.user.emp_no)
        lbl3b = tk.Label(box_frm, justify="left", font=self.FONT, textvariable=subj_var)

        lbl1a.grid(row=0, column=0, sticky="w")
        lbl1b.grid(row=1, column=0, sticky="w")
        lbl2a.grid(row=2, column=0, sticky="w")
        lbl2b.grid(row=3, column=0, sticky="w")
        lbl3a.grid(row=4, column=0, sticky="w")
        lbl3b.grid(row=5, column=0, sticky="w")

        if edit:
            edit_btn = tk.Button(box_frm, text="\u270E EDIT", font=self.FONT, command=edit_mode)
            edit_btn.grid(row=6, column=0, sticky="w")
        
        return [box_frm]
    

    @widget_clearer
    def grade_scn(self):
        
        box_frm = tk.Frame(self.mid_frm)
        box_frm.pack()

        return [box_frm]
    
        # for student in enumerate(self.user.students):
        #     tk.Label(box_frm, text=student).grid(row=0, column=0)
        #     ttk.Combobox(box_frm, values=["A", "B", "C", "D", "F"]).grid(row=0, column=0)

        # return [box_frm]
    


if __name__ == "__main__":
    app = App()
    app.mainloop()
