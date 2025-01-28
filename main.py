# A Mech themed football manager style game
# Modules
import sqlite3


# Constants and Variables
player = {"name": "", "team": [], "pilots": [], "zoids": []}

# datbase connection and cursor
con = sqlite3.connect("builtdifferent.db")
cur = con.cursor()


# Custom Methods/Functions


# sql test
def View_team(name):
    for row in cur.execute(f"SELECT * FROM Teams WHERE name IS '{name}'"):
        print(row)


def Get_Free_Agents():
    for row in cur.execute(
        "SELECT name, skill, salary FROM pilots WHERE team IS NULL order by skill desc;"
    ):
        print(row)


def Get_Zoids(price_range):
    for row in cur.execute(
        f"SELECT name, ((durability+power+speed)/3) as overall, cost FROM zoids WHERE cost <= {price_range} ORDER BY cost ASC;"
    ):
        print(row)


def Start_Game():
    # get player name
    player["name"] = input("name: ")
    print(
        f"Welcome {player['name']}, choose a team to manage using the id number from the following:"
    )
    # list available teams
    for row in cur.execute(f"SELECT * FROM teams;"):
        print(f"{row[0]}: {row[1]}")
    team_choice = input(
        "Choose a team by typeing the corresponding number and pressing enter."
    )
    # add team to player
    for row in cur.execute(f"SELECT * FROM teams WHERE id = {team_choice};"):
        for item in row:
            player["team"].append(item)
    # get team pilots and zoids
    for row in cur.execute(
        f"SELECT * FROM pilots WHERE team = {player['team'][0]} group by name;"
    ):
        player["pilots"].append(row)
    zoids_ids = []
    for pilot in player["pilots"]:
        print(f"{pilot[1]}\nSkill: {pilot[5]}\nSalary: {pilot[6]}\n")
        if pilot[8]:
            zoids_ids.append(pilot[8])
    for item in zoids_ids:
        for row in cur.execute(f"SELECT * FROM zoids WHERE id = {item};"):
            player["zoids"].append(row)

    for zoid in player["zoids"]:
        print(
            f"{zoid[1]}\nOverall: {(zoid[2]+zoid[3]+zoid[4])/3}\nDurability: {zoid[2]}\nPower: {zoid[3]}\nSpeed: {zoid[4]}\nCost: {zoid[7]}\n"
        )


Start_Game()
