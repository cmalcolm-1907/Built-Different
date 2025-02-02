import random
import sqlite3

# Connect to the SQLite database
DATABASE = "builtdifferent.db"


class Pilot:
    def __init__(self, id, name, skill, salary, team_id):
        self.id = id
        self.name = name
        self.skill = skill
        self.salary = salary
        self.team_id = team_id

    def __str__(self):
        return f"{self.name} - Skill: {self.skill} - Salary: {self.salary}"


class Team:
    def __init__(self, id, name, budget):
        self.id = id
        self.name = name
        self.budget = budget
        self.pilots = []
        self.points = 0

    def add_pilot(self, pilot):
        self.pilots.append(pilot)

    def show_squad(self):
        print(f"\n{self.name} Squad:")
        for pilot in self.pilots:
            print(pilot)
        print(f"\nBudget: ${self.budget}M")
        print(f"Points: {self.points}\n")

    def play_match(self, opponent):
        print(f"\n{self.name} vs {opponent.name}")

        # Select up to 3 pilots for each team
        self_pilots = random.sample(self.pilots, min(3, len(self.pilots)))
        opponent_pilots = random.sample(opponent.pilots, min(3, len(opponent.pilots)))

        # Calculate team scores based on selected pilots
        self_score = sum(pilot.skill for pilot in self_pilots) // len(self_pilots)
        opponent_score = sum(pilot.skill for pilot in opponent_pilots) // len(
            opponent_pilots
        )

        # Add some randomness to the match
        self_score += random.randint(-5, 5)
        opponent_score += random.randint(-5, 5)

        # Ensure scores are not negative
        self_score = max(self_score, 0)
        opponent_score = max(opponent_score, 0)

        # Display the selected pilots
        print(f"\n{self.name} starting lineup:")
        for pilot in self_pilots:
            print(pilot)
        print(f"\n{opponent.name} starting lineup:")
        for pilot in opponent_pilots:
            print(pilot)

        # Determine the match outcome
        if self_score > opponent_score:
            print(f"\n{self.name} wins {self_score}-{opponent_score}!")
            self.points += 3
        elif self_score < opponent_score:
            print(f"\n{opponent.name} wins {opponent_score}-{self_score}!")
            opponent.points += 3
        else:
            print(f"\nIt's a draw {self_score}-{opponent_score}!")
            self.points += 1
            opponent.points += 1


def fetch_teams_and_pilots():
    """Fetch teams and pilots from the database."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Fetch teams
    cursor.execute("SELECT id, name, funds FROM teams")
    teams_data = cursor.fetchall()
    teams = {team_id: Team(team_id, name, funds) for team_id, name, funds in teams_data}

    # Fetch pilots
    cursor.execute("SELECT id, name, skill, salary, team_id FROM pilots")
    pilots_data = cursor.fetchall()
    for pilot_id, name, skill, salary, team_id in pilots_data:
        pilot = Pilot(pilot_id, name, skill, salary, team_id)
        if team_id in teams:
            teams[team_id].add_pilot(pilot)

    conn.close()
    return list(teams.values())


def main():
    print("Welcome to Terminal Sports Management!")
    teams = fetch_teams_and_pilots()

    if not teams:
        print("No teams found in the database. Exiting.")
        return

    # Let the user choose their team
    print("\nAvailable Teams:")
    for i, team in enumerate(teams):
        print(f"{i + 1}. {team.name}")

    choice = int(input("Choose your team (enter number): ")) - 1
    if choice < 0 or choice >= len(teams):
        print("Invalid choice. Exiting.")
        return

    user_team = teams[choice]
    print(f"\nYou have chosen {user_team.name}!")

    # Opponent team (for simplicity, choose the first team that's not the user's team)
    opponent_team = next((team for team in teams if team.id != user_team.id), None)
    if not opponent_team:
        print("No opponent team found. Exiting.")
        return

    while True:
        print("\n1. View Squad")
        print("2. Play Match")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            user_team.show_squad()
        elif choice == "2":
            user_team.play_match(opponent_team)
        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
