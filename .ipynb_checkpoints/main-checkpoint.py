from Character import player
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
  
character = player()
character.setting()
character.PlayerName()
character.reset()