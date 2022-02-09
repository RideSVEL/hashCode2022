import sys

fname = sys.argv[1]
filename = fname.split("input/")[1]

# Partie Lecture fichier
with open(fname) as f:
    for line in f:
        print(line)


# Partie Ecriture Sortie
output = ['1', 2]
fichier = open("output/" + filename, "w+")
fichier.write("Entete\n")
for o in output:
    fichier.write(str(o) + "\n")
fichier.close()
