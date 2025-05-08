"""4 main locations the player is going to explore. we'll navigate the 4 to get the treasure through the MAP (I'll use map.py file for this"""
from Character import player
from sys import argv, exit
from Dialogue import DIALOGUE


class OurPlayer(player):
    def __init__(self):
        super().__init__()
        
    def player_status1(self):
        print(f"{self.name} will enter the maze!")
        print("\n")
        print(DIALOGUE["Maze_Entrance"])
        print(DIALOGUE["MAZE_OURMAP"])


class enterance:
    pass
    
class Tower:
    pass

class Cavern:
    pass

class Dungeon:
    pass 

class Garden:
    pass