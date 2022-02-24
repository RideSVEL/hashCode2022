class Project:

    def __init__(self, name, nbOfDaysToComplete, score, bestBeforeDay, nbOfRoles, roles):
        self.name = name
        self.nbOfDaysToComplete = int(nbOfDaysToComplete)
        self.score = int(score)
        self.bestBeforeDay = int(bestBeforeDay)
        self.nbOfRoles = int(nbOfRoles)
        self.roles = roles
        self.projectDone = False
        self.squad = []

    def possible_score(self, current_day):
        if self.bestBeforeDay >= current_day + self.nbOfDaysToComplete:
            return self.score
        else:
            return max([0, self.score - (current_day + self.nbOfDaysToComplete) + self.bestBeforeDay])

    def team_can_do(self, all_contributors):
        workers = []
        contributors = all_contributors[:]
        # Chercher pour chaque skill si quelqu'un existe
        for skill, value in self.roles:
            matched_skill = False
            for contributor in contributors:
                if skill in contributor.skills and contributor.skills[skill] >= value:
                    workers.append(contributor)
                    # print (contributor.name + " can do " + skill + " level " + str(self.roles[skill]))
                    contributors.remove(contributor)
                    matched_skill = True
                    break
                if matched_skill:
                    break


        if len(workers) == len(self.roles):
            if self.name == 'CollectionsNextv1':
                print(self.roles)
                print(workers)
            self.squad = workers
            self.squad_names = list(map(lambda x: x.name, workers))
            return workers
        return []

    def end(self):
        for i in range(len(self.squad)):
            member = self.squad[i]
            skill, value = self.roles[i]
            member.learning(skill, value)
