from room import Room
from player import Player
import sys

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

# Create input parser 
def input_parser():
    command = input("Please type one of the following commands: n (to go north), s (to go south), e (to go east), w (to go west), or q (to exit the game)\n")
    return command

# Make a new player object that is currently in the 'outside' room.
player = Player('Bobby', room['outside'])

# Write a loop that:
# * Prints the current room name
while True:
    # print player name, current location, and location description
    print(f"Welcome, {player.name}")
    print(f"You currently reside in the {player.current_room.name}")
    print(player.current_room.description)
    command = input_parser()

    # if player input == 'q'
    if command == 'q':
        print(f"Goodbye, {player.name}")
        exit()
    
    #if player input == 'n'
    if command == 'n':
        player = Player(player.name, player.current_room.n_to)
        print(f"You move north and enter the {player.current_room.name}")
    
    #if player input == 's'
    if command == 's':
        player = Player(player.name, player.current_room.s_to)
        print(f"You move south and enter the {player.current_room.name}")
    
    #if player input == 'e'
    if command == 'e':
        player = Player(player.name, player.current_room.e_to)
        print(f"You move east and enter the {player.current_room.name}")
        
    #if player input == 'w'
    if command == 'w':
        player = Player(player.name, player.current_room.w_to)
        print(f"You move west and enter the {player.current_room.name}")
    
    
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
