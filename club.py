class GamingClub:
    def __init__(self):
        self.members = []
        self.matches = []

    def add_member(self, player_name, player_id):
        self.members.append({"player_name": player_name, "player_id": player_id})

    def modify_member(self, player_id, new_name):
        for member in self.members:
            if member["player_id"] == player_id:
                member["player_name"] = new_name
                break

    def view_members(self):
        return self.members

    def add_match(self, players, date):
        self.matches.append({"players": players, "date": date})

    def view_matches(self):
        return self.matches


def main():
    club = GamingClub()

    while True:
        print("\n--- Gaming Club Menu ---")
        print("1. Add Player")
        print("2. View Players")
        print("3. Modify Player")
        print("4. Create Match")
        print("5. Schedule Match")
        print("6. View Matches")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            name = input("Enter player name: ")
            player_id = int(input("Enter player ID: "))
            club.add_member(name, player_id)
            print("Player added successfully.")

        elif choice == '2':
            players = club.view_members()
            if players:
                print("Players:")
                for player in players:
                    print(f"ID: {player['player_id']}, Name: {player['player_name']}")
            else:
                print("No players found.")

        elif choice == '3':
            player_id = int(input("Enter player ID to modify: "))
            new_name = input("Enter new player name: ")
            club.modify_member(player_id, new_name)
            print("Player modified successfully.")

        elif choice == '4':
            players = list(map(int, input("Enter player IDs for the match (comma separated): ").split(',')))
            club.add_match(players, "Not scheduled yet")
            print("Match created successfully.")

        elif choice == '5':
            players = list(map(int, input("Enter player IDs for the match (comma separated): ").split(',')))
            date = input("Enter match schedule date (e.g., 2024-12-15): ")
            club.add_match(players, date)
            print(f"Match scheduled for {date}.")

        elif choice == '6':
            matches = club.view_matches()
            if matches:
                print("Matches:")
                for match in matches:
                    print(f"Match with players: {', '.join(map(str, match['players']))} - Scheduled on: {match['date']}")
            else:
                print("No matches found.")

        elif choice == '7':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
