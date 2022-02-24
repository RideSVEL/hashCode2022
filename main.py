import sys

fname = sys.argv[1]
filename = fname.split("input/")[1]

# Partie Lecture fichier
with open(fname) as f:
    lines = f.readlines()

line_0 = lines[0].split(" ")
nb_contributors = int(line_0[0])
nb_projects = int(line_0[1])

print(nb_contributors)
print(nb_projects)


line_index = 1
for i in range(nb_contributors):
    name, nb_skills = lines[line_index].split(" ")
    print(name)
    line_index += 1
    for j in range(int(nb_skills)):
        skill, level = lines[line_index+j].split(" ")
        print(skill)
        print(int(level))
    line_index += int(nb_skills)


for i in range(nb_projects):
    project_name, nb_days, score, best_before, nb_roles = lines[line_index].split(" ")
    print("project", project_name)
    print("nb_days", nb_days)
    print("score", score)
    print("best_before", best_before)
    print("nb_roles", int(nb_roles))
    line_index += 1
    for j in range(int(nb_roles)):
        role_skill, required_level = lines[line_index+j].split(" ")
        print(role_skill)
        print(int(required_level))
    line_index += int(nb_roles)


# Partie Ecriture Sortie
fichier = open("output/" + filename, "w+")
for ingredient in range(10):
    fichier.write(" ")
fichier.write("\n")
fichier.close()
