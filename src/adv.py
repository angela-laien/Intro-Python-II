import random
from player import Player
from room import Room
from item import Item

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

#Items
room['treasure'].add_item(Item("Star of Africa", "The largest diamond in the world"))
room['overlook'].add_item(Item("Paraglider", "Free-flying wing"))
room['foyer'].add_item(Item("Match lighter", "Fire starter"))
room['narrow'].add_item(Item("Gun", "Safety protection"))

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

print('welcome to the adventure game!')

answer = input("Would you like to play? (yes/no) ")

if answer.lower().strip() == "yes":

    name = input("what is your name?: ")

    currentLocation = room['outside']

    player = Player(name, currentLocation)

    print(f"Hi {player.name}, you are in {player.currentLocation.display_name()}")

    print ("what would you like to do now?")

    def to_do():
        return str(input("['n'] go north ['e'] go east ['s'] go south ['w'] go east ['p'] pick up item ['d'] drop item ['q'] quit "))

    todo = to_do()

    def next_move():
        print(f"Current Location: {player.currentLocation.display_name()}")
        print('what would you like to do now? ')
        global todo
        todo = to_do()

    def dead_end():
        print('you have reached a dead end, try again')
        global todo
        todo = to_do()

    while not todo == 'q':
        if player.currentLocation == room['outside']:
            if todo == 'n':
                player.currentLocation = player.currentLocation.n_to
                next_move()
            else: 
                dead_end()

        elif player.currentLocation == room['foyer']:
            if todo == 's':
                player.currentLocation = player.currentLocation.s_to
                next_move()
            elif todo == 'e':
                player.currentLocation = player.currentLocation.e_to
                next_move()
            elif todo == 'n':
                player.currentLocation = player.currentLocation.n_to
                next_move()
            elif todo == 'p':
                item = player.currentLocation.take_item("Match Lighter")
                player.take_item(item)
            elif todo == 'd':
                item = player.currentLocation.drop_item("Match Lighter")
                player.drop_item(item)
            else: 
                dead_end()
            
        elif player.currentLocation == room['overlook']:
            if todo == 's':
                player.currentLocation = player.currentLocation.s_to
                next_move()
            elif todo == 'p':
                item = player.currentLocation.take_item("Paraglider")
                player.take_item(item)
            elif todo == 'd':
                item = player.currentLocation.drop_item("Paraglider")
                player.drop_item(item)
            else: 
                dead_end()

        elif player.currentLocation == room['narrow']:
            if todo == 'w':
                player.currentLocation = player.currentLocation.w_to
                next_move()
            elif todo == 'n':
                player.currentLocation = player.currentLocation.n_to
                next_move()
            elif todo == 'p':
                item = player.currentLocation.take_item("Gun")
                player.take_item(item)
            elif todo == 'd':
                item = player.currentLocation.drop_item("Gun")
                player.drop_item(item)
            else: 
                dead_end()

        elif player.currentLocation == room['treasure']:
            if todo == 'p':
               item = player.currentLocation.take_item("Star of Africa")
               player.take_item(item)
               print("You won the game!")
            else: 
                dead_end()
        
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
