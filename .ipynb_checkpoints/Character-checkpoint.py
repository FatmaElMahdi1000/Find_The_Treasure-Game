class player:
    def __init__(self):
        self.gender = ""
        self.name = ""
    def setting(self):
        while True: # Keep asking until valid answer is provided!
            print("Your Gender will be: ")
            print("Type in '1' for Female")
            print("Type in '2' for Male")
            Choice = input("> ")
            if Choice == "1":
                print("Character gender is: Female")
                break
            elif Choice == "2":
                print("Character gender is: Male")
                break
            else:
                print("No Gender has been selected")
                