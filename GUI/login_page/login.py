from tkinter import *
from tkinter import messagebox

from ..game_page import startup
from ..reset_frame import reset_elements
from backend import login_handler

def login(username, password, root):
    if login_handler.login(username, password):
        reset_elements(root)
        startup.start_app(root, username)
    else:
        messagebox.showerror("Error", "Incorrect username or password")

def create_window(frame, root):

    Label(frame, text="RPS Login", font=("calibre", 50, 'normal')).grid(row=0, column=0, columnspan=2, padx=75, pady=(0, 20))

    Label(frame, text = 'Username:', font=('calibre',10, 'bold')).grid(row=1, column=0)
    name_entry = Entry(frame, font=('calibre',10,'normal'))
    name_entry.grid(row=1, column=1)

    Label(frame, text = 'Password:', font = ('calibre',10, 'bold')).grid(row=2, column=0)
    passw_entry = Entry(frame, font = ('calibre',10,'normal'), show = '*')
    passw_entry.grid(row=2, column=1)

    login_button = Button(frame, text="Login", width=6, command=lambda: login(name_entry.get(), passw_entry.get(), root))
    login_button.grid(row=3, column=1, pady=(10, 0))

if __name__ == "__main__":
    root = Tk()
    root.geometry("375x310")

    create_window(root)

    root.mainloop()