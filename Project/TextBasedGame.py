"""
This is my version of the textbased game. You start in the gathering room and move picking up items through each room.
'quit' to quit game. 'inventory' to view your inventory, and 'north' 'south' 'east' 'west' to move.
You must escape the nurse inorder  to do that you must collect your disguise.
'Look' into each room to find key items.
"""

def start_game():
    player_name = input("What is your name? ")
    print(f"Welcome, {player_name}. You wake up in the gathering room...")

    # Room connections given in class (Top dictionary)
    rooms = {
        "gathering room": {"north": "dayroom", "south": "echo chamber", "west": "greenhouse", "east": "ward hall 1"},
        "greenhouse": {"east": "gathering room"},
        "echo chamber": {"north": "gathering room", "east": "ward hall 2"},
        "ward hall 2": {"west": "echo chamber"},
        "ward hall 1": {"west": "gathering room", "north": "patients commons lower"},
        "patients commons lower": {"south": "ward hall 1"},
        "dayroom": {"south": "gathering room", "east": "patients commons"},
        "patients commons": {}  # end room
    }

# Added a description to the rooms to understand dictionaries more.
    descriptions = {
        "gathering room": "This is where all the insane gather.",
        "greenhouse": "Here the patients pass the time.",
        "echo chamber":  "You can hear your thoughts...",
        "ward hall 1": "A long hallway with peeling paints and flickering lights.",
        "ward hall 2": "A room with dim lights and rusty medical devices.",
        "patients commons lower": "An unruly and disorganized room",
        "dayroom": "Sunlight filters through barred windows. Something glimmers on the desk.",
        "patients commons": "You hear someone rummaging around in here!"
}


    # Items placed in rooms
    items = {
        "greenhouse": "evidence",
        "echo chamber": "gloves",
        "ward hall 2": "clothes",
        "ward hall 1": "mask",
        "patients commons lower": "hat",
        "dayroom": "keycard",
    }

    room = "gathering room"
    inventory = set()                                                                                       # Starting inventory defined as empty
    required_items = {"evidence", "gloves", "clothes", "mask", "hat", "keycard"} # What's required to pass the game.

    def look():                                                                                                  # Defines look as add_item command in the program (Google)
        if  room in items and items[room] not in inventory:                    # Checks item_name against inventory if found. If not found in inventory, add items[room] to the inventory.
            found = items[room]
            inventory.add(found)                                                                    # Adds Item to inventory
            print(f"You found", found)
        else:
            print(f"Nothing here to find!")

    def display_inventory():                                                                         # Prints inventory (Googled "python starting inventory text-based")
        print("Your inventory:")
        if inventory:
            print("You have:", ", ".join(inventory))                                        # lists the inventory in comma format
        else:
                print(f"Inventory is empty.")

    while True:                                                                                                # Loop until break.
        print(f'You are in the', room, ".", descriptions.get(room, "It's fuzzy to walk these halls."))

        if room == "patients commons":                                                      # If you are in the room with required items, you pass the nurse and win.
                if inventory == required_items:                                                # If you have collected every item in the game.
                   print(f"You snuck past the nurse! You win {player_name}!")
                else:
                    print(f"You've been caught sneaking out of the asylum! You lost {player_name}!")
                break                                                                                              # Breaks loop equivalent to quitting the game.

        move = input("North? South? East? West?").lower()                    #Inputs "Yes" "yEs" "YeS" as the same. Move as input

        if move in ("north", "south", "east", "west"):                                  # takes the keys in rooms dictionary and makes moving between rooms possible.
            if move in rooms[room]:
                room = rooms[room][move]                                                      # the room you will be in is a combination of the rooms' room and your movement by input.
            else:
                print('No exit exists')                                                                  # Unable to move if that option is other than a move in the dictionary.
        elif move == 'look':                                                                              # otherwise, you can look
            look()                                                                                                  # Prints items[room] but defined as found.
        elif move == "inventory":                                                                    #If move is inventory display inventory
            display_inventory()                                                                         # Prints only when inventory is empty.
        elif move == 'quit':                                                                               # Type 'quit' game breaks.
            print("Game over.")
            break                                                                                                  # Breaks loop
        else:                                                                                                        # Any other combination prints 'invalid' -- verification check and debug.
            print("Invalid command. Please try a valid response.")

start_game()
