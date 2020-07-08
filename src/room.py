# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, tools):
        self.name = name
        self.description = description
        self.tools = tools
    
    def add_tool(self, t):
        self.tools.append(t)

    def __repr__(self):
        def all_tools():
            new_list = []
            if len(self.tools) > 0:
                for t in range(len(self.tools)):
                    new_list.append(self.tools[t].description)
                return ' , '.join(new_list)
            else:
                return 'no interest'
        return f"You are currently at {self.name}, {self.description}. This room got {all_tools()}"