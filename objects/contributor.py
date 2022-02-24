class Contributor:
    def __init__(self, name, skills):
        # Assign the argument to the instance's name attribute
        self.name = name
        self.skills = skills

    def learning(self, skill, level):
        if (self.skills[skill] <= level):
            self.skills[skill] += 1
            print (self.name + "is learning " + skill + " to " + str(self.skills[skill]))
        else:
            print (self.name + "can't learn " + skill)

    def __str__(self) -> str:
        return 'Name' + self.name + ' - roles:' + str(self.skills.items())