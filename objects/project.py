class Project:

    def __init__(self, name, score, nbOfDaysToComplete, bestBeforeDay, nbOfRoles, roles):
        self.name = name
        self.nbOfDaysToComplete = int(nbOfDaysToComplete)
        self.score = int(score)
        self.bestBeforeDay = int(bestBeforeDay)
        self.nbOfRoles = int(nbOfRoles)
        self.roles = roles
        self.projectDone = False

    def __str__(self) -> str:
        return self.name + ' -days: ' + str(self.nbOfDaysToComplete) + ' - score: ' + str(self.score) + ' - bestBeforeDay:' + str(self.bestBeforeDay) + ' - nbRoles:' + str(self.nbOfRoles) + ' - done:' + str(self.projectDone) + ' - roles:' + str(self.roles.items())