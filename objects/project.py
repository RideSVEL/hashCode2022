class Project:

    def __init__(self, name, score, nbOfDaysToComplete, bestBeforeDay, nbOfRoles, roles):
        self.name = name
        self.nbOfDaysToComplete = int(nbOfDaysToComplete)
        self.score = int(score)
        self.bestBeforeDay = int(bestBeforeDay)
        self.nbOfRoles = int(nbOfRoles)
        self.roles = roles
        self.projectDone = False
        self.squad = []

    def team_can_do(self, contributors):
        workers = []
        # Chercher pour chaque skill si quelqu'un existe
        for skill in self.roles:
            for contributor in contributors:
                if skill in contributor.skills and contributor.skills[skill] >= self.roles[skill]:
                    workers.append(contributor)
                    print (contributor.name + " can do " + skill + " level " + str(self.roles[skill]))
                    contributors.remove(contributor)
                    continue

        if len(workers) == len(self.roles):
            self.squad = workers
            self.squad_names = list(map(lambda x: x.name, workers))
            return workers
        return []