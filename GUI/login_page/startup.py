from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

from .login import create_window as login_window
from .signup import create_window as signup_window

def start_app():
    root = Tk()

    root.geometry("650x310")
    root.resizable(False, False)

    left = Frame(root)
    left.pack(side=LEFT)

    original_image = Image.open("./GUI/assets/rps_img.png")
    resized_image = original_image.resize((200, 200), Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(resized_image)

    panel = Label(left, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes", padx=(50, 0))

    right = ttk.Notebook(root)

    login_frame = Frame(right)
    sign_frame = Frame(right)

    right.add(login_frame, text="Login Page")
    right.add(sign_frame, text="SignUp Page")
    
    right.pack(side=RIGHT)

    login_window(login_frame, root)
    signup_window(sign_frame)

    root.mainloop()


if __name__ == "__main__":
    start_app()