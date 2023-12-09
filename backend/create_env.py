import mysql.connector

from settings import HOST, USER, PASSWD
# HOST = "localhost"
# USER = "root"
# PASSWD = "pass@123"

login_table_create_query = """
CREATE TABLE `login_details` (
	`username` VARCHAR(255) NOT NULL,
	`password` VARCHAR(255) NOT NULL,
	PRIMARY KEY (`username`)
);
"""

game_table_create_query = """
CREATE TABLE `game_details` (
    `username` VARCHAR(255) NOT NULL,
    `wins` INT NOT NULL DEFAULT '0',
    `loss` INT NOT NULL DEFAULT '0',
    `draw` INT NOT NULL DEFAULT '0',
    PRIMARY KEY (`username`),
    FOREIGN KEY (`username`) REFERENCES `login_details`(`username`)
);
"""


def connection():
    try:
        mydb = mysql.connector.connect(
            host=HOST,
            user=USER,
            passwd=PASSWD,
            database="rps_game"
        )
        print("Connection Successful")
    except:
        mydb = mysql.connector.connect(
            host=HOST, 
            user=USER,
            passwd=PASSWD
        )

        myCursor = mydb.cursor()
        myCursor.execute("CREATE DATABASE rps_game")
        myCursor.execute("USE rps_game")
        myCursor.execute(login_table_create_query)
        myCursor.execute(game_table_create_query)
        mydb.commit()
        myCursor.close()

        print("Database Created")

    return mydb


if __name__ == "__main__":
    myDb = connection()
    myCursor = myDb.cursor()
    myCursor.execute("SHOW TABLES")
    for x in myCursor:
        print(x)

    myCursor.close()
    myDb.close()