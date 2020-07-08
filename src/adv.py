import random
from room import Room
from player import player
from tool import Tool

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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

print('welcome to the adventure game!')

answer = input("Would you like to play? (yes/no) ")

if answer.lower().strip() == "yes":

    playerName = input("what is your name?: ")

    location = room['outside']

    backpack = []

    player = Player(playerName, location, backpack)

    print(f"Hi {playerName}, you are in {location}")

    print ("what would you like to do now?")

    def to_do():
        return str(input("['n'] go north ['e'] go east ['s'] go south ['w'] go est ['p'] pick up tool ['q'] quit"))

    todo = to_do():
    
    backpack_action = 0

    def search_backpack():
        print('backpack: ')
        player.search_backpack()
        global todo
        todo = str(input("['n'] go north ['e'] go east ['s'] go south ['w'] go est ['p'] pick up tool ['q'] quit"))

    def next_move():
        print(location)
        print('what would you like to do now?')
        global todo
        todo = to_do()

    def dead_end():
        print('you have reached a dead end, try again')
        global todo
        todo = to_do()

    while not todo = 'q':
        if location == room['outside']:
        elif location == room['foyer']:
        elif location == room['overlook']:
        elif location == room['narrow']:
        elif location == room['treasure']:
            print("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")
        
else:
    print("That's too bad!")

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
