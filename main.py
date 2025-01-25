# A Mech themed football manager style game
import sqlite3

con = sqlite3.connect('builtdifferent.db')
cur = con.cursor()



def view_team(name):
    for row in cur.execute(f"SELECT * FROM Teams WHERE name IS '{name}'"):
        print(row)

view_team('Blitz Team')