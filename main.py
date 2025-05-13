from Character import player
from Locations import OurPlayer, Tower, Cavern, Dungeon, Garden
from Mymap import GameMap 
from sys import argv, exit

Script, FileName= argv

if (len(argv) != 2):
    print("FILE IS NOT FOUND!")
    exit(1) # Exit with 1 to indicate an error

try:
    with open (FileName, "r", encoding="utf-8")  as txt:
        print(txt.read())
    
except FileNotFoundError:
    print(f"Error: File '{FileName}' not found.")
  
# --- Create player and run methods
playing = OurPlayer()

playing.setting()         # ask gender
playing.PlayerName()      # ask name
playing.reset()           # confirm or reset

#playing.player_status1()  # <-- finally print the message
startLocation = GameMap()
startLocation.player_status1()

print("Have not you decided YET!  👻 ?")
print("Type in 1. for the North!\n")
print("Type in 2. for the East!\n")
print("Type in 3. for the South!\n")
print("Type in 4. for the West!\n")

while True:
    path = input("> ")

    if path == "1":
        a_GameMap = Tower()
        a_GameMap.enter()
        break  # finally heading north, stop looping

    elif path == "2":
        a_GameMap = Cavern()
        a_GameMap.enter()
        print("\n")
        print("That's not a valid path to your Treasure 😝. Try again!")

    elif path == "3":
        a_GameMap = Dungeon()
        a_GameMap.enter()
        print("\n")
        print("That's not a valid path to your Treasure 😝. Try again!")
    
    elif path == "4":
        a_GameMap = Garden()
        a_GameMap.enter()
        print("\n")
        print("That's not a valid path to your Treasure 😝. Try again!")
    else:
        print("That's not a valid path. Try again!")
