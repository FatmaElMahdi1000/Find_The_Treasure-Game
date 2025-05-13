"""4 main locations the player is going to explore. we'll navigate the 4 to get the treasure through the MAP (I'll use map.py file for this"""
from random import randint
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
    
class Tower:
    RandomFeelingHits = [
    "You stand before the path, a cold shiver crawling down your spine. \"I... I'm scared,\" you whisper.",
    "\"There's no turning back,\" you remind yourself. Despite the uneasy feeling growing in your stomach, you step forward.",
    "A sudden surge of courage fills you. \"I fear nothing but God,\" you declare, boldly heading NORTH."]
    def enter(self):
        print(Tower.RandomFeelingHits[randint(0, len(self.RandomFeelingHits)-1)])
        print(DIALOGUE["north_dialogue"])

class Cavern:
    def enter(self):
        print(DIALOGUE["east_dialogue"])

class Dungeon:
    def enter(self):
        print(DIALOGUE["south_dialogue"]) 

class Garden:
    def enter(self):
        print(DIALOGUE["west_dialogue"])