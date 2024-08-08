import csv
import datetime
import os
from utils import Format
from person import Person
from tank_game import TankGame


def main():
    # Create main program loop
    while True:
        # File to store leaderboard
        filename = "leaderboard.csv"

        # Initialize game object
        tg = TankGame()

        # Get the value for program menu based on tank game grid size
        program_menu_width = tg.N * 12

        # Print program menu
        print_program_menu(
            program_menu_width=program_menu_width,
            leader=get_leader_from_leaderboard(filename=filename),
        )

        # Handle program commands
        program_command = input("Input a command: ")

        # start
        if program_command == "start":
            Format.print_center("Starting a new game", program_menu_width)

            # Get user name
            user = input("Enter your name: ")

            # Start game
            score = tg.start_game()

            record_result_to_leaderboard(filename=filename, user=user, score=score)

        # instructions
        elif program_command == "instructions":
            Format.print_center("Getting instructions", program_menu_width)
            tg.instructions()
            continue

        # exit
        elif program_command == "exit":
            Format.print_center("Exiting the program", program_menu_width)
            break

        # invalid commands
        else:
            Format.print_center("Invalid command", program_menu_width)
            continue


def print_program_menu(program_menu_width: int, leader: list) -> None:
    # Print program menu
    Format.print_center("", program_menu_width)
    Format.print_center("", program_menu_width)
    Format.print_center("Welcome! This is a tank game.", program_menu_width)
    Format.print_center("'start' To start a new game.", program_menu_width)
    Format.print_center("'instructions' To see game instructions.", program_menu_width)
    Format.print_center("'exit' To exit from program.", program_menu_width)
    Format.print_center("", program_menu_width)
    Format.print_center("", program_menu_width)
    Format.print_center(
        f"Current leader is '{leader[0]}'. He scored '{leader[1]}' in '{leader[2]}'!",
        program_menu_width,
    )
    Format.print_center("", program_menu_width)
    Format.print_center("", program_menu_width)


def get_leader_from_leaderboard(filename: str) -> list:
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
    return leader


def record_result_to_leaderboard(filename: str, user: str, score: int) -> None:
    # Check if file for leaderboard already exists
    if os.path.exists(filename):
        f_exists = True
    else:
        f_exists = False

    # Record user result to a csv file
    fieldnames = ["name", "score", "date"]
    result = {}
    result["name"] = user
    result["date"] = datetime.date.today()  # Get game day
    result["score"] = score

    # Append the results to a file
    with open(filename, "a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # Check if file exists. If so, only append results
        if f_exists:
            writer.writerow(result)
        # If file is created first time
        else:
            writer.writeheader()
            writer.writerow(result)


if __name__ == "__main__":
    main()
