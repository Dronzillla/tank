import random
import csv
import datetime
import os

# Class to pretty format strings
class Fmt:
    @staticmethod
    def bc_print(astr: str, anumb: int):
        print(astr.center(anumb * 3 + 1, "."))
    
    @staticmethod
    def br_print(astr: str, anumb: int):
        print(astr.rjust(anumb * 3 + 1, "."))

    @staticmethod
    def bl_print(astr: str, anumb: int):
        print(astr.ljust(anumb * 3 + 1, "."))


class TankGame:
    def __init__(self, N: int = 7):
        """Create a tank game object.

        :param N: the size of the map (grid) NxN to generate for the game.
        """
        self.N = N
        # Hard-coded starting tank location is 2, 1
        self.tank_loc_x = 2
        self.tank_loc_y = 1
        
        # Setting starting tank direction
        self.tank_direction = {"north": False, "south": True, "east": False, "west": False}

        # Set maximum total shots available in one game to equal to (N - 2) * 4
        self.S_max = (self.N - 4 )
        
        # Set total shots made in each direction
        # Set total shots made
        # Set total shots left
        self.tank_S_made_dir = {"north": 0, "south": 0, "east": 0, "west": 0}
        self.tank_S_made = 0
        self.tank_S_left = self.S_max - self.tank_S_made

        # Set initial score to 100
        self.score = 100
        # Set total shots hit in each direction
        # Set total shots hit
        self.tank_S_hit_dir = {"north": 0, "south": 0, "east": 0, "west": 0}
        self.tank_S_hit = 0

        # Generate target 
        self.target_loc_x, self.target_loc_y = self.__get_target_coordinates()
        
        # Create logo of a tank which points to certain direction
        self.tank_direction_logo = {"north": "⬆️", "south": "⬇️", "east": "⬅️", "west": "➡️"}

    def print_map(self):
        """Print the current map of the game.

        Example output for a 7x7 map:
           0  1  2  3  4  5  6
        0  .  .  .  .  .  .  .
        1  .  .  T  .  .  .  .
        2  .  .  .  .  .  .  .
        3  .  .  .  .  .  .  .
        4  .  .  .  .  .  .  .
        5  .  .  .  .  .  .  .
        6  .  .  .  .  .  .  .

        where T is the location of the tank,
        where . (the dot) is an empty space on the map,
        where the horizontal axis is the x location of the tank and,
        where the vertical axis is the y location of the tank.
        """
        # Print the numbers for the x axis
        print("   " + "  ".join([str(i) for i in range(self.N)]))

        for i in range(self.N):
            # Print the numbers for the y axis
            print(f"{i} ", end="")
            for j in range(self.N):
                if self.tank_loc_x == j and self.tank_loc_y == i:
                    print(f" {self.tank_direction_logo[self.__check_direction()]} ", end="")
                # Modify loop to input target
                elif self.target_loc_x == j and self.target_loc_y == i:
                    print(" ☢ ", end="")
                else:
                    print(" . ", end="")
            print()

    # A function to print a score
    def print_score(self):
        print("")
        txt = "SCORE:"
        score = f"{self.score}"
        print(txt.rjust(self.N * 3 + 1, "."))
        print(score.rjust(self.N * 3 + 1, "."))
        print("")

    # Check if tank and target location is the same
    def __same_loc(self) -> bool:
        if self.tank_loc_x == self.target_loc_x and self.tank_loc_y == self.target_loc_y:
            return True

    # Implement moving of a tank
    def left(self):
        if not self.tank_loc_x == 0:
            self.tank_loc_x -= 1
            self.__no_direction()
            self.tank_direction["east"] = True
            # Update points
            self.__score_move()
            # Check if tank and target is in the same location
            if self.__same_loc():
                self.target_loc_x, self.target_loc_y = self.__get_target_coordinates()
                self.__score_drive()

    def right(self):
        if not self.tank_loc_x == self.N - 1:
            self.tank_loc_x += 1
            self.__no_direction()
            self.tank_direction["west"] = True
            # Update points
            self.__score_move()
            # Check if tank and target is in the same location
            if self.__same_loc():
                self.target_loc_x, self.target_loc_y = self.__get_target_coordinates()
                self.__score_drive()

    def up(self):
        if not self.tank_loc_y == 0:
            self.tank_loc_y -= 1
            self.__no_direction()
            self.tank_direction["north"] = True
            # Update points
            self.__score_move()
            # Check if tank and target is in the same location
            if self.__same_loc():
                self.target_loc_x, self.target_loc_y = self.__get_target_coordinates()
                self.__score_drive()

    def down(self):
        if not self.tank_loc_y == self.N - 1:
            self.tank_loc_y += 1
            self.__no_direction()
            self.tank_direction["south"] = True
            # Update points
            self.__score_move()
            # Check if tank and target is in the same location
            if self.__same_loc():
                self.target_loc_x, self.target_loc_y = self.__get_target_coordinates()
                self.__score_drive()
    
    # A method to get generate random coordinates of a target in the grid
    def __get_target_coordinates(self) -> tuple:
        while True:
            # Get random cooridante for x
            xnum = random.randint(0, self.N - 1)
            # Get random coordinate for y
            ynum = random.randint(0, self.N - 1)
            if xnum == self.tank_loc_x and ynum == self.tank_loc_y:
                continue
            return xnum, ynum

    # Define a method for what happens when a target is hit
    def __target_hit(self):
        print("Hit")
        # Update score
        self.__score_S_hit()
        # Generate new target
        self.target_loc_x, self.target_loc_y = self.__get_target_coordinates()
        # Update shots hit
        self.tank_S_hit_dir[self.__check_direction()] = self.tank_S_hit_dir.get(self.__check_direction(), 0) + 1
        # Update total shots hit
        self.tank_S_hit = sum(list(self.tank_S_hit_dir.values()))

    # Private method to set no direction
    def __no_direction(self):
        self.tank_direction.update( (k,False) for k in self.tank_direction )

    # Private method to check which direction a tank is facing
    def __check_direction(self) -> str:
        for key, value in self.tank_direction.items():
            if value == True:
                return key
    
    # Check how much shots were made in each direction
    def __check_shot_count(self):
        for key, value in self.tank_S_made_dir.items():
            print(f"In '{key}' direction tank made '{value}' shots.")

    def shoot(self):
        # Update shot made of a current direction
        self.tank_S_made_dir[self.__check_direction()] = self.tank_S_made_dir.get(self.__check_direction(), 0) + 1
        # Update total shots made
        self.tank_S_made = sum(list(self.tank_S_made_dir.values()))
        # Update shots left
        self.tank_S_left = self.S_max - self.tank_S_made

        # Check target location and if tank hit target
        if self.tank_loc_x == self.target_loc_x:
            if self.target_loc_y > self.tank_loc_y and self.tank_direction["south"] == True:
                self.__target_hit()
            elif self.target_loc_y < self.tank_loc_y and self.tank_direction["north"] == True:
                self.__target_hit()
            else:
                print("No hit")
                self.__score_S_nohit()
        elif self.tank_loc_y == self.target_loc_y:
            
            if self.target_loc_x > self.tank_loc_x and self.tank_direction["west"] == True:
                self.__target_hit()

            elif self.target_loc_x < self.tank_loc_x and self.tank_direction["east"] == True:
                self.__target_hit()
            else:
                print("No hit")
                self.__score_S_nohit()
        else:
            print("Not hit")
            self.__score_S_nohit()

    def __score_drive(self):
        self.score -= 75
    
    def __score_S_hit(self):
        self.score += 50

    def __score_S_nohit(self):
        self.score -= 25

    def __score_move(self):
        self.score -= 5

    def info(self):
        print(f"Tank is facing '{self.__check_direction()}'.")
        print(f"The coordinates of tank for x is: '{self.tank_loc_x}' and for y is: '{self.tank_loc_y}'.")
        print(f"Tank made '{self.tank_S_made}' shots.")
        print(f"Shots left '{self.tank_S_left}'.")
        print(f"Tank shot '{self.tank_S_hit}' targets.")
        # Check shot count in each direction
        self.__check_shot_count()

    def exit(self):
        print("'exit' command was typed.")
        
    # Instructions
    def instructions(self):
        print("In the map you are marked as: '⬇️'. Your targets are marked as: '☢'.")
        print("The goal of the game is to shoot targets and get highest possible score.")
        print(f"In total you have {self.S_max} shots.")
        print("If you shoot a target you gain 50 points.")
        print("If you shoot and miss you gain -25 points.")
        print("Every move you make you gain -5 points.")
        print("If you drive on target you gain -75 points")
        print("Tank moves by commands: 'left', 'right', up', 'down'.")
        print("Tank shoots by command 'shoot'.")
        print("Target is hit only if you are facing direction where is the target.")
        print("Type 'info' to get information about your current direction and state of a game.")
        print("Type 'instructions' to get all possible commands.")
        print("Type 'exit' to exit from game.")

if __name__ == "__main__":
    # Start a program loop
    while True:
        # Initialize your game object
        tg = TankGame()
        
        # Print menu
        anum = tg.N * 4
        Fmt.bc_print("", anum)
        Fmt.bc_print("", anum)
        Fmt.bc_print("WELCOME! THIS IS A TANK GAME!", anum)
        Fmt.bc_print("'start' TO START A NEW GAME.", anum)
        Fmt.bc_print("'instructions' TO GET USER INSTRUCTIONS.", anum)
        #Fmt.bc_print("'leaderboard' TO GET LEADERBOARD", anum)
        Fmt.bc_print("'exit' TO EXIT FROM PROGRAM.", anum)
        Fmt.bc_print("", anum)
        Fmt.bc_print("", anum)

        filename = "leaderboard.csv"
        # Check if file leaderboard file already exists
        if os.path.exists(filename):
            f_exists = True
        else:
            f_exists = False

        try:
            p_command = input("Input a command: ")
            if p_command == "start":
                Fmt.bc_print("Starting a new game", anum)
                # Get user name
                # Get game day
                user = input("Enter your name: ")
                date = datetime.date.today()
                # Another loop for a new game
                while True:
                    # Break from program when all shots are made
                    if tg.tank_S_made == tg.S_max:
                        print("")
                        Fmt.bc_print("", tg.N)
                        Fmt.bc_print("Game is over!", tg.N)
                        Fmt.bc_print(f"Your score is {tg.score}", tg.N)
                        Fmt.bc_print("", tg.N)
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

            elif p_command  == "instructions":
                Fmt.bc_print("Getting instructions", anum)
                tg.instructions()
                continue
            elif p_command == "exit":
                Fmt.bc_print("Exiting the program", anum)
                break
            # elif p_command == "leaderboard":
            # To be implemented
            else:
                Fmt.bc_print("Invalid command", anum)
                continue
        except:
            Fmt.bc_print("Invalid command!", anum)
            continue
    