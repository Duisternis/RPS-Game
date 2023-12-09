from tkinter import *
from backend import signup_handler

def signup(name_entry, passw_entry, rept_passw_entry):
    if signup_handler.signup(name_entry.get(), passw_entry.get(), rept_passw_entry.get()):
        name_entry.delete(0, END)
        passw_entry.delete(0, END)
        rept_passw_entry.delete(0, END)

def create_window(frame):

    Label(frame, text="RPS SignUp", font=("calibre", 50, 'normal')).grid(row=0, column=0, columnspan=2, padx=50, pady=0)

    Label(frame, text = 'Username:', font=('calibre',10, 'bold')).grid(row=1, column=0)
    name_entry = Entry(frame, font=('calibre',10,'normal'))
    name_entry.grid(row=1, column=1)

    Label(frame, text = 'Password:', font = ('calibre',10, 'bold')).grid(row=2, column=0)
    passw_entry = Entry(frame, font = ('calibre',10,'normal'), show = '*')
    passw_entry.grid(row=2, column=1)

    Label(frame, text = 'Repeat Password:', font = ('calibre',10, 'bold')).grid(row=3, column=0)
    rept_passw_entry = Entry(frame, font = ('calibre',10,'normal'), show = '*')
    rept_passw_entry.grid(row=3, column=1)

    signup_button = Button(frame, text="Sign Up", width=6, command=lambda: signup(name_entry, passw_entry, rept_passw_entry))
    signup_button.grid(row=4, column=1, pady=(10, 0))

if __name__ == "__main__":
    root = Tk()
    root.geometry("375x310")

    create_window(root)

    root.mainloop()