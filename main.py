fox = True
hen = True
grain = True

start = []
finish = []
win = "You Win!"

print("""
Welcome to the Bridge game. You must bring the Fox, Hen, and Grain to the other side
one at a time in order to keep the fox from eating the hen or the hen from eating the grain.
Once you take one of them to the other side of the bridge you may choose to come back with one
item to the start essentially being able to bring one thing with you each time you cross the
bridge.


Enter 1 to begin...""")
play_game = int(input("enter '1' to play: "))
if play_game != 1:
    quitFlag = False
    print("Thanks for playing!")
elif play_game == 1:
    start.append(fox)
    start.append(hen)
    start.append(grain)
    print("""enter 1 to take the FOX across\nenter 2 to take the HEN across\nenter 3 to take the GRAIN across""")
    res = int(input("Enter your choice here:"))
    if res == 2:
        start.remove(hen)
        finish.append(hen)
        if start == [fox, grain]:
            print(
                "You've arrived at the other side of the bridge and set the hen down. Would you like\nto return with the "
                "hen or just yourself: 1 to return just yourself, or 2 to return with the hen.")
            res_return_hen_or_yourself = int(input("Enter choice here: "))
            if res_return_hen_or_yourself == 1:
                print(
                    "You return to the starting point, what would you like to take next?\n Enter 1 for the Fox\nEnter 2 for"
                    " the grain.")
                res_return_fox_or_grain = int(input("Enter choice here: "))
                if res_return_fox_or_grain == 1:
                    start.remove(fox)
                    finish.append(fox)
                    print("you usher the fox over to the other side of the bridge leaving just the grain behind."
                          "\nYou are now at the other side with the Fox and the Hen. Would you like to return with...\n"
                          "1: just yourself...\n2: The Hen\n or, 3: The Fox")
                    res_return_with_yourself_hen_fox = int(input("Enter choice: "))
                    if res_return_with_yourself_hen_fox == 2:
                        finish.remove(hen)
                        start.append(hen)
                        print("You return to the starting point and place the Hen down next to the grain.\n"
                              "What would you like to bring to the other side next?\n"
                              "Enter 1 for the Hen\nEnter 2 for the Grain")
                        start_return_to_finish_hen_or_grain = int(input("Enter choice: "))
                        if start_return_to_finish_hen_or_grain == 2:
                            start.remove(grain)
                            finish.append(grain)
                            print(
                                "You pick up the grain and set it down at the other side of the bridge next to the Fox\n"
                                "Would you like to return with...\n1: Yourself\n 2: the Grain\n 3: the Fox")
                            res_finish_you_grain_fox = int(input("Enter choice: "))
                            if res_finish_you_grain_fox == 1:
                                print("You return to the starting point\n Would you like to take the Hen to the other\n"
                                      "side of the bridge?\n"
                                      "Enter 1 for yes, 2 for no...")
                                res_winning_move = int(input("Enter choice: "))
                                if res_winning_move == 1:
                                    start.remove(hen)
                                    finish.append(hen)
                                    print("You pick up the Hen and place it at the other side of the bridge.\n"
                                          "Looks like your job here is done!")
                                    print("Congratulations! You've won the game...Goodbye!")
