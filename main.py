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

#print(nb_contributors)
#print(nb_projects)
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
    project = Project(project_name, score, nb_days, best_before, int(nb_roles), roles)
    print(project)
    projects.append(project)


# Partie Ecriture Sortie
fichier = open("output/" + filename, "w+")
for ingredient in range(10):
    fichier.write(" ")
fichier.write("\n")
fichier.close()
