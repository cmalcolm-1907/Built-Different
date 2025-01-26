# A Mech themed football manager style game
# Modules
import sqlite3


# Constants and Variables
# datbase connection and cursor
con = sqlite3.connect("builtdifferent.db")
cur = con.cursor()


# Custom Methods/Functions


# sql test
def View_team(name):
    for row in cur.execute(f"SELECT * FROM Teams WHERE name IS '{name}'"):
        print(row)


def View_Pilot(name):
    for row in cur.execute(f"SELECT * FROM Pilots WHERE name IS '{name}'"):
        print(row)
