from Locations import OurPlayer, Tower, Cavern, Dungeon, Garden
from sys import exit, argv
from Dialogue import DIALOGUE

class GameMap(OurPlayer):

    locations = {"north_dialogue":Tower()
                 , "east_dialogue": Cavern()
                 , "south_dialogue":Dungeon()
                 , "west_dialogue": Garden()}
    def __init__(self):        #current scene is the enterance of the maze
        super().__init__()
    