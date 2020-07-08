# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, currentLocation, tools):
        self.name = name
        self.currentLocation = currentLocation
        self.tools = tools

    def get_tool(self, tool_list, tool):
        for t in range(0, len(tool_list)):
            if tool_list[t].tool_name == tool:
                self.tools.append(tool_list[t])

    def search_tools(self):
        for t in self.tools:
            print(t)

    def __str__(self):
        return f"{self.name} is at {self.currentLocation}"