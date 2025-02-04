from engine import *


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

    # Remove the user's team from the list of opponents
    opponent_teams = [team for team in teams if team.id != user_team.id]
    opponent_index = 0  # Start with the first opponent

    while True:
        print("\n1. View Squad")
        print("2. Play Match")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            user_team.show_squad()
        elif choice == "2":
            if not opponent_teams:
                print("No opponents available. Exiting.")
                break

            # Select the next opponent
            opponent_team = opponent_teams[opponent_index]
            print(f"\nYou will be playing against {opponent_team.name}!")

            # Play the match
            user_team.play_match(opponent_team)

            # Increment the opponent index for the next match
            opponent_index = (opponent_index + 1) % len(opponent_teams)
        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
