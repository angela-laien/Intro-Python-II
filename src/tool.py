class Tool:
    def __init__(self, tool_name, description):
        self.tool_name = tool_name
        self.description = description

    def __str__(self):
        return f'{self.tool_name},{self.description}'