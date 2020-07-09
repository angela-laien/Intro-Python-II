# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item

class Player:
    def __init__(self, name, currentLocation):
        self.name = name
        self.currentLocation = currentLocation
        self.inventory = []
    def take_item(self, item):
        item.on_take()
        self.inventory.append(item)
    def drop_item(self, tool):
        for o in self.inventory:
            if o.name == tool:
                self.inventory.remove(o)
                o.on_drop()
                return o
