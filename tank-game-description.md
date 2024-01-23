# Tank exercise

Your task is to develop in python a simple [command-line interface](https://en.wikipedia.org/wiki/Command-line_interface) tank game. You will implement this exercise in stages, each stage is a bit more difficult and builds upon the previous stage.

Start with the given file `tank_game.py` because it has some starting code to make it easier for you.

## Stage 1

All tank and information management must be done on the console (actual graphical interface is not required). This will require you to create a menu and accept user instructions. Actions to be performed (methods called) until the user stops the program (for example, by selecting an actual menu item). You can use this management to test your TankGame class during your coding process.

Class: TankGame

Methods to implement: print_map (already implemented), forward, backward, steer_left, steer_right, shoot, info, ...

Store the following variables in the class:
- Tank coordinates.
- Direction of the tank.
- Number of shots in each direction.

The tank can move forward (to the North), to the right (to the East), back (to South), left (West) by one position. For example "the tank is moving left," meaning it turned 90 degrees and moved through one unit to the West.

A tank can only fire in the direction it is facing.

The `info()` method must display:
- Which direction the tank is currently facing.
- What are its coordinates.
- How many total shots did it make.
- How many shots were fired in each direction separately.

![picture](https://github.com/robotautas/kursas/raw/master/tanko%20iliustracija.png)

Text translation: this is only an illustration of the idea of the game, you don't need this kind of graphical interface, we work in the console only.

## Stage 2

Improve the program so that:
- A target is generated in the tank game grid. 
- The task of the tank is to be in the right position and in the right direction so that a hit is recorded after firing. 
- When a tank hits, we see the message "hit" on the console and a new target is generated immediately. 

## Stage 3

- Come up with a point system, e.g. start with 100 points, +50 points for hits, -10 points for each forward drive, sum up total hits. 
- Show the points next to the game grid. 
- When the points run out, the program shows how many targets have been shot down and ends. 
- Perhaps it is possible to store high scores - after the end, the name is entered and the player with the number of downed targets is recorded in the charts. 
- The charts can perhaps be viewed with the 'top' command. 

## Stage 4

Come up with some improvements of your own! This is necessary to score the top grade.