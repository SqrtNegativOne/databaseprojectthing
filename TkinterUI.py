#misc
import tkinter as tk

root = tk.Tk()

root.state("zoomed")
root.title("School Portal")

top_frm = tk.Frame(root, bg="red")
dwn_frm = tk.Frame(root, bg="green")
lft_frm = tk.Frame(root, bg="yellow")
rgt_frm = tk.Frame(root, bg="orange")

top_frm.pack(side="top", fill="x")
dwn_frm.pack(side="bottom", fill="x")
lft_frm.pack(side="left", fill="y")
rgt_frm.pack(side="right", fill="y")

tk.Button(top_frm, height=2, width=2).pack(anchor="center")
tk.Button(dwn_frm, height=2, width=2).pack(anchor="center")
tk.Button(lft_frm, height=2, width=2).pack(anchor="center")
tk.Button(rgt_frm, height=2, width=2).pack(anchor="center")


def title_screen() -> list:
    ...

def student_screen():
    ...

def teacher_screen():
    ...

root.mainloop()
