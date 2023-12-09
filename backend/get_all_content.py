from .create_env import connection

def get():
    myDb = connection()
    myCursor = myDb.cursor()

    myCursor.execute(f"SELECT * FROM game_details;")
    myResult = myCursor.fetchall()

    myCursor.close()

    return myResult