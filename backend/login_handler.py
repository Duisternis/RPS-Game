from .create_env import connection

def login(username, password):
    myDb = connection()
    myCursor = myDb.cursor()

    myCursor.execute(f"SELECT * FROM login_details WHERE username = '{username}' AND password = '{password}'")
    myResult = myCursor.fetchall()

    myCursor.close()

    if len(myResult) == 0:
        return False
    else:
        return True