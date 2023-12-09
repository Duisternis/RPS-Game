from .create_env import connection

def post(username, status):
    myDb = connection()
    myCursor = myDb.cursor()

    if (status == 0):
        myCursor.execute(f"SELECT draw from game_details where username='{username}'")
        score = myCursor.fetchall()
        score = score[0][0] + 1
        myCursor.execute(f"UPDATE game_details set draw={score} where username='{username}'")

    if (status == 1):
        myCursor.execute(f"SELECT wins from game_details where username='{username}'")
        score = myCursor.fetchall()
        score = score[0][0] + 1
        myCursor.execute(f"UPDATE game_details set wins={score} where username='{username}'")

    if (status == -1):
        myCursor.execute(f"SELECT loss from game_details where username='{username}'")
        score = myCursor.fetchall()
        score = score[0][0] + 1
        myCursor.execute(f"UPDATE game_details set loss={score} where username='{username}'")

    
    myDb.commit()
    myCursor.close()