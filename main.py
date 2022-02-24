import sys

fname = sys.argv[1]
filename = fname.split("input/")[1]

# Partie Lecture fichier
with open(fname) as f:
    lines = f.readlines()

nb_clients = int(lines[0])



# Partie Ecriture Sortie
fichier = open("output/" + filename, "w+")
for ingredient in range(10):
    fichier.write(" ")
fichier.write("\n")
fichier.close()
