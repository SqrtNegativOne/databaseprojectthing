import teacher_backend as teacher
import student_backend as student
import tkinter as tk

databaseprojectthing = """
█▀▄░█▀█░▀█▀░█▀█░█▀▄░█▀█░█▀▀░█▀▀░█▀█░█▀▄░█▀█░▀▀█░█▀▀░█▀▀░▀█▀░▀█▀░█░█░▀█▀░█▀█░█▀▀
█░█░█▀█░░█░░█▀█░█▀▄░█▀█░▀▀█░█▀▀░█▀▀░█▀▄░█░█░░░█░█▀▀░█░░░░█░░░█░░█▀█░░█░░█░█░█░█
▀▀░░▀░▀░░▀░░▀░▀░▀▀░░▀░▀░▀▀▀░▀▀▀░▀░░░▀░▀░▀▀▀░▀▀░░▀▀▀░▀▀▀░░▀░░░▀░░▀░▀░▀▀▀░▀░▀░▀▀▀
"""

class App(tk.Tk):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.state("zoomed")
        self.title("Database Project thing")

        self.current_widgets = []

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
    def signin(self, username, password, typ):

        if typ == "Teacher":
            ...
        else:
            ...

    @widget_clearer
    def signup(self):
        ...

    @widget_clearer
    def title_screen(self) -> None:
        box_frm = tk.Frame(self.mid_frm)
        box_frm.pack(anchor="center")

        member_type = tk.StringVar(value="Teacher")

        lbl1 = tk.Label(box_frm, text="Username: ")
        lbl2 = tk.Label(box_frm, text="Password: ")
        ety1 = tk.Entry(box_frm)
        ety2 = tk.Entry(box_frm)
        menu = tk.OptionMenu(box_frm, member_type, "Teacher", "Student")

        ok_btn = tk.Button(box_frm, text="OK",
                           command=lambda: self.signin(ety1.get(), ety2.get(), member_type.get()))
        su_btn = tk.Button(box_frm, text="Signup",
                           command=self.signup)

        lbl1.grid(row=0, column=0)
        lbl2.grid(row=1, column=0)
        ety1.grid(row=0, column=1)
        ety2.grid(row=1, column=1)
        menu.grid(row=2, column=1)
        ok_btn.grid(row=3, column=0)
        su_btn.grid(row=3, column=1)

        return [box_frm]


if __name__ == "__main__":
    app = App()
    app.mainloop()
