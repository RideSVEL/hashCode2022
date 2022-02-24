class Contributor:
    def __init__(self, name, skills):
        # Assign the argument to the instance's name attribute
        self.name = name
        self.skills = skills

    def __str__(self) -> str:
        print self.skills[0]