from item import Item
from room import Room
from player import Player


# INSTANCES OF ROOM/CLASSES
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),
    
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

# Declare Loot
items = {
    "Meat": Item("Meat", "A pile of rotten meat"),
    "Poison": Item("Poison", "Used in an assassination attempt, be wary!"),
    "Ice": Item("Ice", "Be careful, slippery"),
    "Gold": Item("Gold", "very shiny and bright!")
}

# Add Loot to rooms
room['foyer'].items.append(items['Meat'])
room['outside'].items.append(items['Poison'])
room['narrow'].items.append(items['Ice'])
room['overlook'].items.append(items['Gold'])



# Create an input parser 
def input_parser():
    command = input("Please type one of the following commands: \nn (to go north), \ns (to go south), \ne (to go east), \nw (to go west), \nor q (to exit the game)\n").strip().lower().split()[0]
    command = command[0]
    return command

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed. **


# AN INSTANCE OF THE PLAYER/CLASS
# Make a new player object that is currently in the 'outside' room.
player = Player('Bobby', room['outside'], [])
# room = Room("", "", )

# Write a loop that:
# * Prints the current room name

print("=====================================================\n")

print(f"Welcome, {player.name}")
print("______________" + "\n")

print("=====================================================\n")
while True:
    # print player name, current location, and location description

    print(f"You currently reside in the {player.current_room.name}")
    print(player.current_room.description + "\n")
    
    
    # Items 
    if (len(player.current_room.items) < 1):
        print("Loot: ")
    else:
        print(f"Loot/Items: ")
        print("============\n\n")
        # for item in player.current_room.items:
        print(str(player.current_room))
        print(f"{player.current_room}  \n")
    
    # Inventory
    print("=====================================================")
    if (len(player.inventory) < 1):
        print("Your inventory is empty!!!")
    else:
        print(f"INVENTORY: \n {player.inventory} \n")
    print("=====================================================")
        
    
    ## INPUTS ##
    command = input_parser()
    print(command)
    
    # if player input == 'q'
    if command == 'q':
        print(f"Goodbye, {player.name}")
        exit()
    
    #if player input == 'n'
    if command == 'n':
        player = Player(player.name, player.current_room.n_to, [])
        print(f"You move north and enter the {player.current_room.name}")
    
    #if player input == 's'
    if command == 's':
        player = Player(player.name, player.current_room.s_to, [])
        print(f"You move south and enter the {player.current_room.name}")
    
    #if player input == 'e'
    if command == 'e':
        player = Player(player.name, player.current_room.e_to, [])
        print(f"You move east and enter the {player.current_room.name}")
        
    #if player input == 'w'
    if command == 'w':
        player = Player(player.name, player.current_room.w_to, [])
        print(f"You move west and enter the {player.current_room.name}")
        
    if command == 'bb':
        player = Player(player.name, player.current_room.w_to, []) ## no an obj ^^
    


    #ITEM FUNCTIONS
    if command == "p":
        
        player.pickup(items)
        # Room.remove(player.current_room.items)
        ## working on this ^^
        ## moved on to drop item
    
    if command == "d":
        
        player.drop(items)
        
        
    
    
    
        