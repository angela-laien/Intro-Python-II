# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

    def display_name(self):
        return f"{self.name}"

    def display_description(self):
        return f"{self.description}"

    def display_items(self):
        tool = "Room items:\n"
        for item in self.items:
            tool += f"{item}\n"
        return tool

    def remove_item(self, tool):
        for t in self.items:
            if t.name == tool:
                self.items.remove(t)
                return t
        else:
            return "No such item in this room."
            
    def add_item(self, item):
        self.items.append(item)