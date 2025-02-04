import sqlite3
import random

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


class Mech:
    def __init__(self, id, name, hp, pow, spd, cost, colour, team):
        self.id = id
        self.name = name
        self.durability = hp
        self.power = pow
        self.speed = spd
        self.cost = cost
        self.colour = colour
        self.team = team

    def __str__(self):
        return f"{self.name}: Durability: {self.durability} - Power: {self.power} - Speed: {self.speed}"


class Team:
    def __init__(self, id, name, budget):
        self.id = id
        self.name = name
        self.budget = budget
        self.pilots = []
        self.mechs = []
        self.points = 0

    def add_pilot(self, pilot):
        self.pilots.append(pilot)

    def add_mech(self, mech):
        self.mechs.append(mech)

    def show_squad(self):
        print(f"\n{self.name} Squad:")
        for pilot in self.pilots:
            print(pilot)
        for mech in self.mechs:
            print(mech)

        print(f"Budget: ${self.budget}M")
        print(f"Points: {self.points}\n")

    # match logic
    def play_match(self, opponent):
        print(f"\n{self.name} vs {opponent.name}")

        # Select up to 3 pilots for each team
        if len(self.pilots) >= 3:
            self_pilots = random.sample(self.pilots, min(3, len(self.pilots)))
        else:
            self_pilots = self.pilots
        if len(self.mechs) >= 3:
            self_mechs = random.sample(self.mechs, min(3, len(self.mechs)))
        else:
            self_mechs = self.mechs

        if len(opponent.pilots) >= 3:
            opponent_pilots = random.sample(
                opponent.pilots, min(3, len(opponent.pilots))
            )
        else:
            opponent_pilots = opponent.pilots
        if len(opponent.mechs) >= 3:
            opponent_mechs = random.sample(opponent.mechs, min(3, len(self.mechs)))
        else:
            opponent_mechs = opponent.mechs

        # Calculate team scores based currently just pilot scores as a multiplier to mech stats
        self_score = int(
            (
                sum(pilot.skill / 100 for pilot in self_pilots)
                * sum(
                    (mech.durability + mech.power + mech.speed) / 3
                    for mech in self_mechs
                )
            )
        )

        opponent_score = int(
            (
                sum(pilot.skill / 100 for pilot in opponent_pilots)
                * sum(
                    (mech.durability + mech.power + mech.speed) / 3
                    for mech in opponent_mechs
                )
            )
        )

        # Add some randomness to the match
        self_score += random.randint(int(-self_score / 4), int(self_score / 4))
        opponent_score += random.randint(
            int(-opponent_score / 4), int(opponent_score / 4)
        )

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


# fetch info from teh database
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

    # Fetch mechs
    cursor.execute(
        "SELECT c.id, m.name, m.durability, m.power, m.speed, m.cost, c.colour, c.team_id FROM base_mechs m LEFT JOIN custom_mechs c on m.id=c.base_mech_id"
    )
    custom_mech_data = cursor.fetchall()
    for (
        mech_id,
        name,
        durability,
        power,
        speed,
        cost,
        colour,
        team_id,
    ) in custom_mech_data:
        mech = Mech(mech_id, name, durability, power, speed, cost, colour, team_id)
        if team_id in teams:
            teams[team_id].add_mech(mech)

    conn.close()
    return list(teams.values())
