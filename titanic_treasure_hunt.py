print(r"""
*******************************************************************************

                   ,:',:`,:'
                __||_||_||_||___
           ____['''''''''''''''''']___
           \ " '''''''''''''''''''' \
    ~~^~^~^~^^~^~^~^~^~^~^~^~~^~^~^~^~~^~^

*******************************************************************************
""")

weapon = ""
room = ""
red = "you lost"
blue = "you won and next step is"
yellow = "you lost"
answer = "blue"

print("Welcome to Titanic Treasure Hunt.")
print("Your mission is to find the treasure.")
print("There are several hunters on the ship, on each floor.")

choose = int(input("Choose which floor you want to go (1, 2, 3, 4): "))

if choose == 2:
    weapon = input("Which weapon do you want to use? ")
    print(f"That's a nice {weapon}!\n")
    room = input("Two rooms on this floor are suspicious: 201 and 202. Which one do you enter? ")
    print("You got busted!\nPlease try again by picking a different floor.")

elif choose == 1:
    weapon = input("Which weapon do you want to use? ")
    print(f"That's a nice {weapon}!\n")
    room = input("Two rooms on this floor are suspicious: 101 and 102. Which one do you enter? ")
    print("You got busted by cops!\nPlease try again by picking a different floor.")

elif choose == 3:
    weapon = input("Which weapon do you want to use? ")
    print(f"That's a nice {weapon}!\n")
    room = input("Two rooms on this floor are suspicious: 301 and 302. Which one do you enter? ")
    print("You got busted by the FBI!\nPlease try again by picking a different floor.")

elif choose == 4:
    weapon = input("Which weapon do you want to use? ")
    print(f"That's a nice {weapon}!\n")
    room = input("Two rooms on this floor are suspicious: 401 and 402. Which one do you enter? ")

    if room == "401":
        print("You found the treasure!")
        color = input("Pick a color to open the treasure (red, blue, yellow): ").lower()

        if color == "blue":
            print("Blue is correct! You found the treasure 🎉")
        else:
            print("Wrong color. You lost the treasure!")
    else:
        print("You lost again.")
else:
    print("Invalid choice. Please restart the game.")
