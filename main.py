from typing import List

quitFlag = True

fox = True
hen = True
grain = True

start = []
finish = []


def checkStart(self, start: List[bool]) -> bool:
    if start is [fox, hen, grain]:
        pass
    elif start is [hen, grain]:
        print("You take the fox to the other side leaving the Hen alone with the grain")
        print("Would you like to return to the starting point?\n Enter 1 for yes\n Enter 2 to return with the Fox")
        res_return_fox = int(input("Enter choice here:"))
        if res_return_fox == 1:
            print("Game Over!")
        else:
            print("Game Over!")
    elif start is [fox, grain]:
        print("You've arrived at the other side of the bridge...\nWould you like to take anything/anyone back\n"
              "Enter 1 to take back the Hen\nEnter 2 to return without anything")
        res_return_hen = int(input("Enter choice here: "))
        if res_return_hen == 1:
            


while quitFlag:
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

    if play_game == 1:
        start.append(fox)
        start.append(hen)
        start.append(grain)

        print("""enter 1 to take the FOX across\nenter 2 to take the HEN across\nenter 3 to take the GRAIN across""")
        res = int(input("Enter a your choice here:"))

        if res == 1:
            start.remove(fox)

        # if res == 2:
        #
        # if res == 3:
