from .create_env import connection
from tkinter import messagebox

def signup(username, password, repeat_password):

    myDb = connection()
    myCursor = myDb.cursor()

    myCursor.execute(f"SELECT * FROM login_details WHERE username = '{username}'")
    myResult = myCursor.fetchall()

    if len(myResult) == 0:
        if password == repeat_password:
            myCursor.execute(f"INSERT INTO login_details (username, password) VALUES ('{username}', '{password}')")
            myCursor.execute(f"INSERT INTO game_details (username) VALUES ('{username}')")
            messagebox.showinfo("Success", "Account created successfully")
            myDb.commit()
            myCursor.close()
            return True
        else:
            messagebox.showerror("Error", "Passwords do not match")
            myCursor.close()
            return False
    
    messagebox.showerror("Error", "Username already exists")
    myCursor.close()
    return False


