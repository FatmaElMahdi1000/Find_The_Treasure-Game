"""This code is for setting both player's Name and gender"""
class player:
    
    def __init__(self):
        self.gender = ""
        self.name = ""
        
    def setting(self):
        while True: # Keep asking until valid answer is provided!
            print("Your Gender will be: ")
            print("Type in '1' for Female")
            print("Type in '2' for Male")
            self.gender = input("> ")
            if self.gender == "1":
                print("Character gender is: Female")
                break
            elif self.gender == "2":
                print("Character gender is: Male")
                break
            else:
                print("No Gender has been selected")
    
    def PlayerName(self):
        while True:
            print("Your Name will be: ")
            self.name = input("> ")
            if self.name == "":
                print("Error: No Name has been entered")
                print("Try Again!")
                error(1)
            else:
                print(f"Your Name is {self.name}!")
                break
                
    def reset(self):
        while True:
            print("Press 'Enter' to confirm the name and gender and Type in: 'Change' to reset!")
            Confirmation = input("")
            if Confirmation == "":
                if self.gender == '1':
                    self.gender = 'Female'
                    print(f"Congrats! Your character info is ready! Gender: {self.gender} and Name: {self.name} are both SAVED!") 
                    break
                elif self.gender == '2':
                    self.gender = 'Male'
                    print(f"Congrats! Your character info is ready! Gender: {self.gender} and Name: {self.name} are both SAVED!")
                    break
            else:
                print("To Reset select '1'")
                print("1. Resetting Name and Gender")
                resetting = input("> ")
                if resetting == "1":
                    self.setting()    ## Calling the setting method
                    self.PlayerName()
                