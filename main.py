import teacher_backend as teacher
import student_backend as student

import tkinter.messagebox as mssg
import tkinter.ttk as ttk
import tkcalendar as tkc
import tkinter as tk

from datetime import datetime, date
from random import randint
from textwrap import wrap
from math import erf


teacher.FILE_PATH    = r"...\teacher_data.txt"
student.FILE_PATH    = r"...\students.csv"
teacher.HW_FILE_PATH = r"...\homework.txt"
student.HW_FILE_PATH = r"...\homework.txt"

SUBJECTS = ["English", "Mathematics", "Chemistry", "Physics",
            "German", "Computer Science", "Physical Education"]

FONT1 = ["Century Gothic", 15]
FONT2 = ["Century Gothic", 15, "underline"]
FONT3 = ["Century Gothic", 15, "bold"]
FONT4 = ["Century Gothic", 10]
FONT5 = ["Century Gothic", 20]

_student = teacher.namedtuple("_student", ["name", "id", "subject", "password"])

def deconstructor(std) -> list:
    return [std.name, std.password, std.id, ",".join(std.subject)]

WELCOME_TEXT = """
Welcome to our school database,
your all-in-one solution for
seamless organization and effective
communication. Our powerful platform
allows you to assign homework
effortlessly, ensuring students stay
on track. Additionally, you can easily
view user profiles. Feel free to explore.
"""


class Homepage(tk.Frame):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        lbl = tk.Label(self, text="\n".join(wrap(WELCOME_TEXT.replace("\n", " "), 30)),
                       font=FONT1, justify="left")
        lbl.pack(fill="both", expand=True, pady=20)


class Signin(tk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None


    def signin(self):

        for widget in self.winfo_children():
            widget.destroy()

        def signin_process():


            if utype_var.get():
                user = teacher.signin(ety1.get(), ety2.get())
            else:
                user = student.signin(ety1.get(), ety2.get())
                
            if not user:
                mssg.showwarning("Warning", "Wrong Username or Password.\nPlease try again.")
                return

            self.user = user
            self.event_generate("<<UserSignin>>", when="now")
        
        utype_var = tk.IntVar(self, value=1)

        lbl1 = tk.Label(self, text="Username", font=FONT1)
        lbl2 = tk.Label(self, text="Password", font=FONT1)
        ety1 = tk.Entry(self, relief="solid", width=30, font=FONT1)
        ety2 = tk.Entry(self, relief="solid", width=30, font=FONT1, show="*")

        rbt1 = tk.Radiobutton(self, text="Teacher", variable=utype_var, value=1, font=FONT1)
        rbt2 = tk.Radiobutton(self, text="Student", variable=utype_var, value=0, font=FONT1)

        signin_btn = tk.Button(self, text="Sign in", font=FONT1, relief="flat",
                               bg="#2C8CBE", command=signin_process)
        signup_btn = tk.Button(self, text="Sign up", font=FONT2, relief="flat",
                               fg="blue", cursor="hand2", command=self.signup)

        lbl1.grid(row=0, column=0, sticky="w")
        ety1.grid(row=1, column=0, columnspan=2)
        lbl2.grid(row=2, column=0, sticky="w")
        ety2.grid(row=3, column=0, columnspan=2)
        rbt1.grid(row=4, column=0)
        rbt2.grid(row=4, column=1)

        signin_btn.grid(row=5, column=0, sticky="ew", columnspan=2)
        signup_btn.grid(row=6, column=0, sticky="nw")


    def signup(self):

        for widget in self.winfo_children():
            widget.destroy()

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
                    self.user = student.register(ety1.get(), ety2.get(), ",".join([SUBJECTS[i] for i in subj.curselection()]))

                self.event_generate("<<UserSignin>>", when="now")

        def generate_password():
            ety2.delete(0, "end")
            ety2.insert(0, "".join([chr(randint(33, 122)) for _ in range(10)]))

        utype_var = tk.IntVar(value=1)

        lbl1 = tk.Label(self, text="Username", font=FONT1)
        lbl2 = tk.Label(self, text="Password", font=FONT1)
        lbl3 = tk.Label(self, text="Subjects", font=FONT1)
        ety1 = tk.Entry(self, relief="solid", width=30, font=FONT1)
        ety2 = tk.Entry(self, relief="solid", width=30, font=FONT1)
        subj = tk.Listbox(self, selectmode="multiple", activestyle="none", justify="center",
                          relief="sunken", width=20, height=7, font=FONT4)
        
        rbt1 = tk.Radiobutton(self, text="Teacher", variable=utype_var, value=1, font=FONT1)
        rbt2 = tk.Radiobutton(self, text="Student", variable=utype_var, value=0, font=FONT1)

        signup_btn = tk.Button(self, text="Sign Up", font=FONT1, relief="flat",
                               bg="#2C8CBE", command=verify_user)
        signin_btn = tk.Button(self, text="Sign in", font=FONT2, relief="flat",
                               fg="blue", cursor="hand2", command=self.signin)
        gen_btn    = tk.Button(self, text="Generate", font=FONT4, command=generate_password)

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
        signin_btn.grid(row=7, column=0, sticky="w")


class SearchBar(tk.Frame):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.user = None
        self.users = {}
        self.suggestions = []

        self.Vtext = tk.StringVar(self)
        self.Vfilt = tk.IntVar(self, value=1)
        self.Vsubj = tk.StringVar(self, value="Subject")
        
        self.Vtext.trace("w", self.update_search)
        self.Vfilt.trace("w", self.update_search)
        self.Vsubj.trace("w", self.update_search)

        self.filt_frm = tk.Frame(self)

        search_bar = tk.Entry(self, textvariable=self.Vtext, font=FONT1, width=18)

        self.search_box = ttk.Treeview(self, selectmode="browse", columns=["name", "id"],
                                       show="tree", height=4)

        self.search_box.column("#0", minwidth=0, width=0)
        self.search_box.column("name", width=100)
        self.search_box.column("id", width=100)

        search_btn = tk.Button(self, text="\U0001F50D",  command=self.search)
        self.filter_btn = tk.Button(self, text="\u25BC", command=self.toggle_filter)

        rbt_1 = tk.Radiobutton(self.filt_frm, value=1, variable=self.Vfilt, font=FONT4, text="Username")
        rbt_2 = tk.Radiobutton(self.filt_frm, value=0, variable=self.Vfilt, font=FONT4, text="Emp Num.")
        combo = ttk.Combobox(self.filt_frm, values=SUBJECTS+[None], font=FONT4, textvariable=self.Vsubj)

        rbt_1.grid(row=0, column=0)
        rbt_2.grid(row=0, column=1)
        combo.grid(row=1, column=0, columnspan=2, pady=5)

        search_bar.grid(row=0, column=0, sticky="nsew")
        search_btn.grid(row=0, column=1, padx=5)
        self.filter_btn.grid(row=0, column=2)


    def update_search(self, *_):

        suggestions = teacher.search_users(
                            self.Vtext.get(), self.Vfilt.get(),
                            self.Vsubj.get() if self.Vsubj.get() in SUBJECTS else None
                            )

        if not suggestions or not self.Vtext.get():
            self.search_box.grid_forget()
            return

        if not self.search_box.winfo_ismapped():
            self.search_box.grid(row=2, column=0, pady=2, sticky="nsew")

        self.search_box.delete(*self.search_box.get_children())
        self.search_box["height"] = len(suggestions)

        self.users.clear()

        for user in suggestions:
            iid = self.search_box.insert("", "end", values=(user.name.capitalize(), f"#{user.id}"))
            self.users[iid] = user


    def search(self):

        if self.search_box.focus():
            self.user = self.users[self.search_box.focus()]
            self.event_generate("<<UserProfile>>", when="now")


    def toggle_filter(self):
        if not self.filt_frm.winfo_ismapped():
            self.filt_frm.grid(row=1, column=0, columnspan=3)
            self.filter_btn["text"] = "\u25B2"
        else:
            self.filt_frm.grid_forget()
            self.filter_btn["text"] = "\u25BC"


class Sidebar(tk.Frame):
        
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.sidebar = tk.Frame(self)
        self.sidebar.pack_propagate(0)
        
        self.tglbtn = tk.Button(self, text="\u2630", relief="sunken", borderwidth=0,
                                font=FONT5, command=self.toggle_sidebar)
        self.prfbtn = tk.Button(self, text="\U0001F464", relief="flat", font=FONT5,
                                command=lambda: self.event_generate("<<Profile>>"))

        self.banner = tk.Label(self.sidebar, justify="center", font=FONT1)

        self.togglevar = True
        self.buttons = []

        for text, sym in zip(["Home", "Profile", "Homework", "Exit"],
                             ["\U0001F3E0", "\U0001F464", "\U0001F4D6", ""]):
            
            btn = tk.Button(self.sidebar, bg="#2C8CBE", fg="white", relief="sunken", font=FONT5, text=sym,
                      borderwidth=0, command=lambda t=text: self.event_generate(f"<<{t}>>", when="now"))
            btn.pack(side="top", fill="x", pady=2)

            self.buttons.append((btn, text, sym))
        
        self.buttons[3][0].pack_forget()

        self.tglbtn.pack(side="top", anchor="w")
        self.sidebar.pack(fill="both", expand=True)


    def transition(self, max, target, reverse, n=1):
        if n==20:
            self.sidebar["width"] = target
            return
        self.sidebar["width"] = max*((1-erf(n/5)) if reverse else erf(n/5))
        self.after(20, lambda: self.transition(max, target, reverse, n+1))


    def toggle_sidebar(self):

        self.after_cancel(self.transition)

        if not self.togglevar:
            self.transition(150, 40, True)
            
            for button in self.buttons:
                button[0].configure(text=button[2], font=FONT5)
            
            self.buttons[3][0].pack_forget()
            self.banner.pack_forget()
            self.prfbtn.pack_forget()
        else:
            self.transition(150, 150, False)

            for button in self.buttons:
                button[0].configure(text=button[1], font=FONT1)

            self.buttons[3][0].pack(side="top", fill="x", pady=2)
            self.banner.pack(side="bottom")
            self.prfbtn.pack(side="bottom")

        self.togglevar = not self.togglevar


class UserProfile(tk.Frame):

    def __init__(self, master, user, edit, **kwargs) -> None:
        super().__init__(master, *kwargs)

        self.user = user
        self.edit = edit

        self.isteacher = isinstance(self.user, teacher.teacher)

        self.view_profile()

    
    def view_profile(self):

        for widget in self.winfo_children():
            widget.destroy()

        self.Vname = tk.StringVar(self, value=self.user.name.capitalize())
        self.Vpass = tk.StringVar(self)

        lbl1a = tk.Label(self, justify="left", font=FONT3, text="NAME")
        lbl2a = tk.Label(self, justify="left", font=FONT3,
                         text=("EMP." if self.isteacher else "ADM.") + " NUMBER")
        lbl3a = tk.Label(self, justify="left", font=FONT3, text="SUBJECTS")

        self.lbl1b = tk.Label(self, justify="left", font=FONT1, textvariable=self.Vname)
        self.lbl2b = tk.Label(self, justify="left", font=FONT1, text=self.user.id)
        
        if self.isteacher:
            self.lbl3b = tk.Label(self, justify="left", font=FONT1, text=self.user.subject)
        else:
            self.lbl3b = tk.Menubutton(self, text="View", font=FONT4, relief="raised")
            menu = tk.Menu(self.lbl3b, tearoff=False)
            self.lbl3b["menu"] = menu

            for subject in self.user.subject:
                menu.add_command(label=subject, font=FONT4)


        for i, lbl in enumerate([lbl1a, self.lbl1b, lbl2a,self.lbl2b, lbl3a, self.lbl3b]):
            lbl.grid(row=i, column=0, sticky="w")

        if self.edit:
            self.edit_btn = tk.Button(self, text="EDIT \u270E", font=FONT1, command=self.edit_mode)
            self.edit_btn.grid(row=6, column=0, sticky="w", pady=20)


    def edit_mode(self):

        self.lbl1b.destroy()
        self.lbl3b.destroy()
        self.edit_btn.destroy()

        ety1 = tk.Entry(self, justify="left", font=FONT1, textvariable=self.Vname)
        ety3 = tk.Entry(self, justify="left", font=FONT1, textvariable=self.Vpass)

        if self.isteacher:
            self.Vsubj = tk.StringVar(self ,value=self.user.subject)
            ety2 = ttk.Combobox(self, textvariable=self.Vsubj, values=SUBJECTS, font=FONT1)
        else:
            ety2 = tk.Menubutton(self, text="Select", font=FONT4, relief="raised")
            menu = tk.Menu(ety2, tearoff=False)
            ety2["menu"] = menu

            self.vars = {subject: tk.BooleanVar(self, value=subject in self.user.subject)
                         for subject in SUBJECTS}
            
            for subject in SUBJECTS:
                menu.add_checkbutton(label=subject, font=FONT4,
                                     variable=self.vars[subject])


        lbl3 = tk.Label(self, text="PASSWORD", font=FONT3, justify="left")
        ok_btn = tk.Button(self, text="OK", font=FONT1, command=self.confirm_edits)

        def process_delete():
            if mssg.askyesno("Delete Account", "Are you sure you want to delete your account?"):
                if self.isteacher:
                    teacher.edit_user_data(self.user, {}, True)
                else:
                    student.deleteAccount(deconstructor(self.user))
                
                self.event_generate("<<Exit>>", when="now")

        del_btn = tk.Button(self, text="Delete Account", font=FONT3, bg="red", fg="white",
                            command=process_delete)

        ety1.grid(row=1, column=0, sticky="ew", columnspan=2)
        ety2.grid(row=5, column=0, sticky="ew", columnspan=2)
        lbl3.grid(row=6, column=0, sticky="w")
        ety3.grid(row=7, column=0, sticky="ew", columnspan=2)
        ok_btn.grid(row=8, column=0, pady=(5, 5), sticky="w")
        del_btn.grid(row=8, column=1, sticky="e")


    def confirm_edits(self):
                
        if len(self.Vpass.get()) == 0:
            password = self.user.password
        elif len(self.Vpass.get()) < 5:
            mssg.showerror("Edit Changes", "Password must be at least 5 characters long")
            return
        else:
            password = teacher.sha256(self.Vpass.get().encode("utf-8")).hexdigest()

        if not mssg.askyesno("Edit Changes", "Confirm Changes?"):
            return
        
        if self.isteacher:
            _id = "T" + self.Vsubj.get()[0].upper() + self.user.id[2:]

            self.user = teacher.edit_user_data(self.user, {"name" : self.Vname.get(), "id" : _id,
                                                           "subject" : self.Vsubj.get(),
                                                           "password" : password})
        else:
            new_subjs = {subj for subj in self.vars if self.vars[subj].get()}
            temp_user = deconstructor(self.user)

            student.deleteSubjects(temp_user, set(self.user.subject) - new_subjs)
            student.change_password(temp_user, password)
            student.change_name(temp_user, self.Vname.get())

            for subject in new_subjs - set(self.user.subject):
                student.addSubject(temp_user, subject)
            
            user = student.getUser(self.user.id)
            self.user = _student(user[0], user[2], user[3].split(","), user[1])
            

        
        self.view_profile()
        self.event_generate("<<PostEdit>>", when="now")


class HomeworkFrame(tk.Frame):

    def __init__(self, master, user, *args, **kwargs) -> None:
        super().__init__(master, *args, **kwargs)
        
        self.user = user
        self.isteacher = isinstance(self.user, teacher.teacher)
        
        self.main_screen()

    
    def main_screen(self):

        for widget in self.winfo_children():
            widget.destroy()

        scrolly = tk.Scrollbar(self, orient="vertical")
        scrolly.grid(row=0, column=1, sticky="ns")

        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=FONT4)
        style.configure("mystyle.Treeview.Heading", font=FONT1)

        self.tree = ttk.Treeview(self, selectmode="none", style="mystyle.Treeview",
                                 yscrollcommand=scrolly.set)
        self.tree.grid(row=0, column=0)

        scrolly.config(command=self.tree.yview)

        self.tree.column("#0", width=300, stretch=True)
        self.tree.heading("#0", text="Homework", anchor="center")

        for subject in SUBJECTS:
            self.tree.insert("", index="end", iid=subject, text=subject.upper())
            
            hws = [(i[0], datetime.strptime(i[1], "%d/%m/%Y"), i[2])
                   for i in student.homework(subject)]
            hws.sort()

            for i, hw in enumerate(hws):
                iid2 = self.tree.insert(subject, index="end", text=f"{hw[1]: %d %b %Y}", tag=str(i%2))

                for line in wrap(hw[2], 35):
                    self.tree.insert(iid2, index="end", text=line, tag=str(i%2))
        
        self.tree.tag_configure("0", background="#E8E8E8")
        self.tree.tag_configure("1", background="#DFDFDF")

        if self.isteacher:
            asn_btn = tk.Button(self, text="Assign Homework", font=FONT4, command=self.assign)
            asn_btn.grid(row=2, column=0, columnspan=2)


    def assign(self):

        def exit_btn():
            teacher.assign_hw(self.user, ety1.get("1.0", "end").replace("\n", " "),
                              cal.get_date().strftime(r"%d/%m/%Y"))
            self.main_screen()
            win.destroy()

        win = tk.Toplevel(self, takefocus=True, bd=10)


        lbl1 = tk.Label(win, font=FONT4, text="Homwork: ")
        lbl2 = tk.Label(win, font=FONT4, text="Deadline: ")

        ety1 = tk.Text(win, font=FONT4, width=30, height=5)
        btn1 = tk.Button(win, text="ok", font=FONT4, command=exit_btn)

        today = date.today()

        cal = tkc.DateEntry(win, year=today.year, month=today.month, day=today.day, 
                           mindate=date.today(), selectmode="day")

        
        lbl1.grid(row=0, column=0, sticky="e")
        ety1.grid(row=0, column=1, columnspan=3, sticky="nsew")
        lbl2.grid(row=1, column=0, sticky="e")
        cal.grid(row=1, column=1, pady=10)

        btn1.grid(row=2, column=3)
        win.mainloop()


class App(tk.Tk):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.geometry("800x500")
        self.resizable(False, False)
        self.title("Database Project thing")
        
        self.user = None

        self.signin_frm = Signin(self)
        self.search_frm = SearchBar(self)
        self.sidebar_frm = Sidebar(self)
        self.middle_frm = tk.Frame(self, height=350, width=350)

        title = tk.Label(self, text="Database Project Thing", font=("Bahnschrift light", 40))
        title.pack(side="top", fill="x", pady=10)

        self.bind("<<UserSignin>>", lambda _: self.signin_portal())
        self.bind("<<UserProfile>>", lambda _: self.switcher("Profile1"))
        self.bind("<<PostEdit>>", lambda _: self.post_edit())

        for text in ["Home", "Profile", "Homework", "Exit"]:
            self.bind(f"<<{text}>>", lambda _, t=text: self.switcher(t))

        self.signin_frm.pack()
        self.signin_frm.signin()


    def signin_portal(self):

        self.signin_frm.destroy()
        self.user = self.signin_frm.user

        self.search_frm.pack(side="right", fill="y")
        self.sidebar_frm.pack(side="left", fill="y", anchor="n")
        self.middle_frm.place(x=200, y=100)
        
        frm = Homepage(self.middle_frm)
        frm.pack(fill="both", anchor="center")

        if isinstance(self.user, teacher.teacher):
            pass
        else:
            self.user = _student(self.user[0], self.user[2], self.user[3].split(","), self.user[1])

        self.sidebar_frm.banner["text"] = f"{self.shortname()}\n#{self.user.id}"
    

    def shortname(self) -> str:
        _name = self.user.name.split()
        name, surname = _name[:-1], _name[-1]
        name = " ".join([name[0].upper() for name in name]) + "."
        surname = surname.capitalize()[:10]

        full_name = (name + " " if name != "." else "") + surname
        return full_name
    
    def post_edit(self):
        self.user = self.middle_frm.winfo_children()[0].user
        self.sidebar_frm.banner["text"] = f"{self.shortname()}\n#{self.user.id}"

    
    def switch_frm(self, frm):
        self.middle_frm.winfo_children()[0].destroy()
        frm.pack(anchor="center", fill="y", pady=(50, 0))


    def switcher(self, event):
        
        if event == "Exit":
            self.destroy()
        elif event == "Home":
            self.switch_frm(Homepage(self.middle_frm))
        elif event == "Profile1":
            self.switch_frm(UserProfile(self.middle_frm, self.search_frm.user,
                                        self.user == self.search_frm.user))
        elif event == "Profile":
            self.switch_frm(UserProfile(self.middle_frm, self.user, True))
        elif event == "Homework":
            self.switch_frm(HomeworkFrame(self.middle_frm, self.user))


if __name__ == "__main__":
    app = App()
    app.mainloop()
