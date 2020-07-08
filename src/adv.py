from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", 
                    "Dim light filters in from the south. Dusty passages run north and east."),

    'overlook': Room("Grand Overlook", 
                    "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."),

    'narrow':   Room("Narrow Passage", 
                    "The narrow passage bends here from west to north. The smell of gold permeates the air."),

    'treasure': Room("Treasure Chamber", 
                    "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
while True:
    play = input("Would you like to play a game? ( y / n ) ")

    if play.lower().strip() == "y":
        char_name = input("Please enter a name for your character: ").strip()
        room_number = input("""Please enter a room number (1 - 5) to enter:
        1. Outside
        2. Foyer
        3. Overlooky
        4. Narrow
        5. Treasure
        """).lower().strip()
        if room_number == "1":
            char_room = room["outside"]
            print(char_room)
            new_room = input("Go to foyer? (y/n)")
            if new_room == "y":
                char_room = room["foyer"]
                print(char_room)
        elif room_number == "2":
            print(room["foyer"])
        elif room_number == "3":
            print(room["overlook"])
        elif room_number == "4":
            print(room["narrow"])
        elif room_number == "5":
            print(room["treasure"])
        else:
            print("Not a valid choice")
    else: 
        print("Thank you for playing.")
        break


# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
