def hunterQuest():
    yes_no = ["yes", "no"]
    directions = ["left", "right", "forward", "backward"]

    # Introduction
    name = input("What is your name, adventurer?\n")
    print("Greetings, " + name + ". Let us go on a quest!")
    print("You find yourself on the edge of a dark forest.")
    print("Can you find your way through?\n")

    # # Start of game
    # response = ""
    # while response not in yes_no:
    #     response = input("Would you like to step into the forest?\nyes/no\n")
    #     if response == "yes":
    #         print("You head into the forest. You hear crows cawwing in the distance.\n")
    #     elif response == "no":
    #         print("You are not ready for this quest. Goodbye, " + name + ".")
    #         quit()
    #     else: 
    #         print("I didn't understand that.\n")

    # # Next part of game
    # response = ""


    print("Welcome to the HunterXHunter Adventure Game, " + name + "!")
    print("You are a rookie hunter setting out on your journey to become a Hunter.")
    print("Your goal is to pass the Hunter Exam and prove yourself worthy.")


    print("\nYou find yourself at the entrance of the Hunter Exam site.")
    print("You see three paths ahead of you: left, right, and forward.")


    response = ""
    while response not in directions:
        response = input("Which path will you take?\nleft/right/forward\n")
        if response == "left":
            print("You chose the left path and encountered a wild beast!")
            print("You must defeat the beast to continue.")
            fight_response = input("Will you fight or flee?\n")
            if fight_response == "fight":
                print("You engage in a fierce battle and emerge victorious!")
                print("You continue on your journey.")
            elif fight_response == "flee":
                print("You run away from the beast, but lose valuable time.")
                print("You decide to take another path.")
                response = ""  
            else:
                print("Invalid response. Try again.")
                response = ""  
        elif response == "right":
            print("You chose the right path and found a hidden treasure!")
            print("Congratulations, you found a valuable artifact.")
            print("You continue on your journey.")
        elif response == "forward":
            print("You chose the forward path and encountered a mysterious gate.")
            print("To unlock the gate, you must solve a riddle.")
            riddle_response = input("What is always in front of you but can't be seen?\n")
            if riddle_response.lower() == "future":
                print("Correct! The gate opens, and you proceed to the next stage of the exam.")
                print("You continue on your journey.")
            else:
                print("Incorrect answer. The gate remains locked.")
                print("You decide to take another path.")
                response = ""  
        else:
            print("Invalid direction. Try again.")

    # End of the game
    print("Congratulations, " + name + "! You have successfully navigated through the Hunter Exam.")
    print("You are now one step closer to becoming a true Hunter.")
    print("Thank you for playing!")