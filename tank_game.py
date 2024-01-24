import random

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
                    print(" T ", end="")
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

    # Implement moving of a tank
    def left(self):
        if not self.tank_loc_x == 0:
            self.tank_loc_x -= 1
            self.__no_direction()
            self.tank_direction["east"] = True
            # Update points
            self.__score_move()

    def right(self):
        if not self.tank_loc_x == self.N - 1:
            self.tank_loc_x += 1
            self.__no_direction()
            self.tank_direction["west"] = True
            # Update points
            self.__score_move()

    def up(self):
        if not self.tank_loc_y == 0:
            self.tank_loc_y -= 1
            self.__no_direction()
            self.tank_direction["north"] = True
            # Update points
            self.__score_move()

    def down(self):
        if not self.tank_loc_y == self.N - 1:
            self.tank_loc_y += 1
            self.__no_direction()
            self.tank_direction["south"] = True
            # Update points
            self.__score_move()
    
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
    def __check_direction(self):
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
        print("In the map you are marked as: 'T'. Your targets are marked as: '☢'.")
        print("The goal of the game is to shoot targets and get highest possible score.")
        print(f"In total you have {self.S_max} shots.")
        print("If you shoot a target you get 50 points.")
        print("If you shoot and miss you loose 25 points.")
        print("Every move you make you loose 5 points.")
        print("Tank moves by commands: 'left', 'right', up', 'down'.")
        print("Tank shoots by command 'shoot'.")
        print("Target is hit only if you are facing direction where is the target.")
        print("Type 'info' to get information about your current direction and state of a game.")
        print("Type 'instructions' to get all possible commands.")
        print("Type 'exit' to exit from game.")

if __name__ == "__main__":
    # Initialize your game object
    tg = TankGame()
    # Start game loop
    tg.instructions()

    while True:
        
        # Break from program when all shots were made
        if tg.tank_S_made == tg.S_max:
            
            print("gg".center(tg.N * 3 + 1, "."))
            print("Game is over!".center(tg.N * 3 + 1, "."))
            print(f"Your score is {tg.score}".center(tg.N * 3 + 1, "."))
            print("gg".center(tg.N * 3 + 1, "."))
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