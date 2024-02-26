import csv
import datetime
import os
from format import Format
from person import Person
from tank import TankGame


def main():
    while True:
        # Initialize your game object
        tg = TankGame()

        # Check if file leaderboard file already exists
        filename = "leaderboard.csv"
        if os.path.exists(filename):
            f_exists = True
        else:
            f_exists = False

        # Open a leaderboard file and create Person object
        # Get leader who scored the most points
        # If more than 1 person scored maximum points the one who scored earliest is selected.
        try:
            with open(filename, "r") as csvleaderboard:
                reader = csv.DictReader(csvleaderboard)
                for line in reader:
                    person = Person(line["name"], int(line["score"]), line["date"])
            # Get a person with first maximum result
            leader = Person.get_max_person()
        except:
            leader = ["no data", "no data", "no data"]

        # Get the value to pretty print menu using Format class
        anum = tg.N * 4
        # Print program menu
        Format.bc_print("", anum)
        Format.bc_print("", anum)
        Format.bc_print("WELCOME! THIS IS A TANK GAME!", anum)
        Format.bc_print("'start' TO START A NEW GAME.", anum)
        Format.bc_print("'instructions' TO GET USER INSTRUCTIONS.", anum)
        Format.bc_print("'exit' TO EXIT FROM PROGRAM.", anum)
        Format.bc_print("", anum)
        Format.bc_print("", anum)
        Format.bc_print(
            f"Current leader is '{leader[0]}'. He scored '{leader[1]}' in '{leader[2]}'!",
            anum,
        )
        Format.bc_print("", anum)
        Format.bc_print("", anum)

        try:
            p_command = input("Input a command: ")
            if p_command == "start":
                Format.bc_print("Starting a new game", anum)
                # Get user name
                # Get game day
                user = input("Enter your name: ")
                date = datetime.date.today()
                # Another loop for a new game
                while True:
                    # Break from program when all shots are made
                    if tg.tank_S_made == tg.S_max:
                        print("")
                        Format.bc_print("", tg.N)
                        Format.bc_print("Game is over!", tg.N)
                        Format.bc_print(f"Your score is {tg.score}", tg.N)
                        Format.bc_print("", tg.N)
                        print("")

                        # Record user result to a csv file
                        fields = ["name", "score", "date"]
                        result = {}
                        result["name"] = user
                        result["date"] = date
                        result["score"] = tg.score

                        # Append the results to a file
                        with open(filename, "a") as csvfile:
                            writer = csv.DictWriter(csvfile, fieldnames=fields)
                            # Check if file exists. If so, only append results
                            if f_exists:
                                writer.writerow(result)
                            # If file is created first time
                            else:
                                writer.writeheader()
                                writer.writerow(result)
                        break

                    # Print the score and map
                    # Get user command
                    tg.print_score()
                    tg.print_map()
                    command = input("Input a command: ")

                    # Exit game if command is exit
                    if command == "exit":
                        break

                    # Try executing the command
                    str_command = "tg." + command + "()"
                    try:
                        exec(str_command)
                    except Exception:
                        print("Error. Type 'instructions' to get possible commands")

            elif p_command == "instructions":
                Format.bc_print("Getting instructions", anum)
                tg.instructions()
                continue
            elif p_command == "exit":
                Format.bc_print("Exiting the program", anum)
                break
            # elif p_command == "leaderboard":
            # To be implemented
            else:
                Format.bc_print("Invalid command", anum)
                continue
        except:
            Format.bc_print("Invalid command!", anum)
            continue


if __name__ == "__main__":
    main()
