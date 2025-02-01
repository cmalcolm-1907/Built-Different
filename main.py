import sqlite3


class GameUI:
    def __init__(self):
        self.conn = sqlite3.connect("builtdifferent.db")
        self.cursor = self.conn.cursor()
        self.teams = {}
        self.load_teams()

    def load_teams(self):
        for row in self.cursor.execute("SELECT id, name, funds FROM teams"):
            self.teams[row[0]] = {
                "name": row[1],
                "funds": row[2],
            }

    def list_teams(self):
        if not self.teams:
            print("No teams available.")
        else:
            for team_id, team_data in self.teams.items():
                print(f"{team_id}: {team_data['name']} - Funds: {team_data['funds']}")

    def add_team(self):
        team_name = input("Enter team name: ")
        self.cursor.execute(
            "INSERT INTO teams (name,funds) VALUES (?, 200000)", (team_name,)
        )
        self.conn.commit()
        self.load_teams()
        print(f"Team '{team_name}' added.")

    def update_team_funds(self, team_id, amount):
        if team_id in self.teams:
            self.teams[team_id]["funds"] += amount
            self.cursor.execute(
                "UPDATE teams SET funds = ? WHERE id = ?",
                (self.teams[team_id]["funds"], team_id),
            )
            self.conn.commit()

    def close(self):
        self.conn.close()


if __name__ == "__main__":
    game = GameUI()
    game.list_teams()
    game.close()
