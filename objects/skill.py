class Skill:
    def __init__(self, name, level):
        # Assign the argument to the instance's name attribute
        self.name = name
        self.level = level

    def __str__(self) -> str:
        return "Skill " + self.name + " - level " + self.level