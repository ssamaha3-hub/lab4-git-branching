def intro():
    print("You wake up in a dark forest. You can go left or right.")
    choice = input("Which direction do you choose? (left/right/center): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    elif choice == "center":
        center_path()
    else:
        print("You stand alone, unsure what to do. The forest swallows you.")

def left_path():
    print("You walk left and find a mysterious glowing sword stuck in a stone.")
    print("Then a massive dragon attacks you and you slay it in one hit.")
    print("You headed back to your village knowing you saved the day.")

def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")
    print("You slay the squirrel and take his acorns")
    print("You take the acorns back to the village and show off your loot.")

def center_path():
    print("you walk center and sit at a nearby lake.")

if __name__ == "__main__":
    intro()
