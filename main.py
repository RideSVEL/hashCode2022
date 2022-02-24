import sys

from objects.contributor import Contributor
from objects.project import Project

fname = sys.argv[1]
filename = fname.split("input/")[1]

# Partie Lecture fichier
with open(fname) as f:
    lines = f.readlines()

line_0 = lines[0].split(" ")
nb_contributors = int(line_0[0])
nb_projects = int(line_0[1])

contributors = []
projects = []

line_index = 1
for i in range(nb_contributors):
    name, nb_skills = lines[line_index].split(" ")
    line_index += 1
    skills = {}
    for j in range(int(nb_skills)):
        skill, level = lines[line_index+j].split(" ")
        skills[skill] = int(level.strip())
    line_index += int(nb_skills)
    contributor = Contributor(name, skills)
    print(contributor)
    contributors.append(contributor)


for i in range(nb_projects):
    project_name, nb_days, score, best_before, nb_roles = lines[line_index].split(" ")
    line_index += 1
    roles = {}
    for j in range(int(nb_roles)):
        role_skill, required_level = lines[line_index+j].split(" ")
        roles[role_skill] = int(required_level.strip())
    line_index += int(nb_roles)
    project = Project(project_name, int(nb_days), int(score), int(best_before), int(nb_roles), roles)
    print(project)
    projects.append(project)


free_contributors = contributors
working_contributors = []

todo_projects = projects
working_projects = {}
terminated_projects = []


day = 0


while len(todo_projects) or len(working_projects):
    project_to_end = working_projects.get(day)
    if project_to_end:
        for proj in project_to_end:
            free_contributors += proj.squad
            terminated_projects.append(proj)

        del working_projects[day]

    started_projects = []
    for proj in todo_projects:
        optimized_contributors = proj.team_can_do(free_contributors)
        if len(optimized_contributors):
            free_contributors = [c for c in free_contributors if c not in optimized_contributors]
            working_contributors.append(optimized_contributors)

            end_day = proj.nbOfDaysToComplete + day
            if not working_projects.get(end_day):
                working_projects[end_day] = []
            working_projects[end_day].append(proj)
            started_projects.append(proj)

    # On ne peut plus faire de nouveaux projets
    if not len(working_projects) and not len(started_projects):
        break

    todo_projects = [project for project in todo_projects if project not in started_projects]
    day += 1


# Partie Ecriture Sortie
fichier = open("output/" + filename, "w+")
nb_projects_done = len(terminated_projects)
fichier.write(str(nb_projects_done) + '\n')
for project in terminated_projects:
    fichier.write(project.name + "\n")
    fichier.write(' '.join(project.squad_names) + "\n")
fichier.close()
