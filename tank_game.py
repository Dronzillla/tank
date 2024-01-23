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

        # Set shots in direction to 0
        # Set maximum shots in one direction to equal to {N - 2}
        self.S = self.N - 2
        
        self.tank_shots = {"north": 0, "south": 0, "east": 0, "west": 0}
        
        
        self.tank_max_shots = {"north": self.S, "south": self.S, "east": self.S, "west": self.S}
        # Set total shots made
        self.S_made = 0

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
                    print(" X ", end="")
                else:
                    print(" . ", end="")
            print()


    '''
    Improve the program so that:
    - A target is generated in the tank game grid. 
    - The task of the tank is to be in the right position and in the right direction so that a hit is recorded after firing. 
    - When a tank hits, we see the message "hit" on the console and a new target is generated immediately. 
    '''
    def __get_target_coordinates(self) -> tuple:
        while True:
            # Get random cooridante for x
            xnum = random.randint(0, self.N - 1)
            # Get random coordinate for y
            ynum = random.randint(0, self.N - 1)

            if xnum == self.tank_loc_x and ynum == self.tank_loc_y:
                continue
            return xnum, ynum


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
        for key, value in self.tank_shots.items():
            print(f"In '{key}' direction tank made '{value}' shots.")

    # Implement moving of a tank
    def left(self):
        if not self.tank_loc_x == 0:
            self.tank_loc_x -= 1
            self.__no_direction()
            self.tank_direction["east"] = True

    def right(self):
        if not self.tank_loc_x == self.N - 1:
            self.tank_loc_x += 1
            self.__no_direction()
            self.tank_direction["west"] = True

    def forward(self):
        if not self.tank_loc_y == 0:
            self.tank_loc_y -= 1
            self.__no_direction()
            self.tank_direction["north"] = True

    def backward(self):
        if not self.tank_loc_y == self.N - 1:
            self.tank_loc_y += 1
            self.__no_direction()
            self.tank_direction["south"] = True

    def info(self):
        print(f"The tank is facing '{self.__check_direction()}'.")
        print(f"The cordinates of tank for x is: '{self.tank_loc_x}' and for y is: '{self.tank_loc_y}'.")
        print(f"The tank made '{self.S_made}' shots.")
        self.__check_shot_count()

    
    def shoot(self):
        if self.tank_loc_x == self.target_loc_x:
            if self.target_loc_y > self.tank_loc_y and self.tank_direction["south"] == True:
                print("Hit")
                self.target_loc_x, self.target_loc_y = self.__get_target_coordinates()
            elif self.target_loc_y < self.tank_loc_y and self.tank_direction["north"] == True:
                print("Hit")
                self.target_loc_x, self.target_loc_y = self.__get_target_coordinates()
            else:
                print("No hit")
        elif self.tank_loc_y == self.target_loc_y:
            
            if self.target_loc_x > self.tank_loc_x and self.tank_direction["west"] == True:
                print("Hit")
                self.target_loc_x, self.target_loc_y = self.__get_target_coordinates()

            elif self.target_loc_x < self.tank_loc_x and self.tank_direction["east"] == True:
                print("Hit")
                self.target_loc_x, self.target_loc_y = self.__get_target_coordinates()
            else:
                print("No hit")
        else:
            print("Not hit")

    # Instructions
    @staticmethod
    def instructions():
        print("Type 'instructions' to get all possible commands.")
        print("Tank moves by commands: 'left', 'right', forward', 'backword'.")
        print("Tank shoot by command 'shoot'.")

if __name__ == "__main__":
    # Initialize your game object
    tg = TankGame()
    # Start game loop
    tg.instructions()

    while True:
        tg.print_map()

        command = input("Input a command: ")
        
        str_command = "tg." + command + "()"

        try:
            exec(str_command)
        except AttributeError:
            print("Error. Type 'instructions' to get possible commands")
        
        # For debug
        # print(tg.tank_direction)

        continue
        # TODO: Implement handling of commands here
