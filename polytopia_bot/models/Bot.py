class Bot:
    def __init__(self, name: str = "default_bot", comp: int = 1):
        self.name = name
        comp = 1 if comp < 1 else comp
        self.complexity = 5 if comp > 5 else comp

    def __str__(self):
        return f"Bot '{self.name}', complexity '{complexity_definition()}'"

    def complexity_definition(self):
        comps = ['Low skill', 'Easy', 'Normal', 'Hard', 'Impossible']
        return comps[self.complexity-1]
