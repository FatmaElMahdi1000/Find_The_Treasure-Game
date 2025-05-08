from Character import player
from Locations import OurPlayer
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

playing.player_status1()  # <-- finally print the message