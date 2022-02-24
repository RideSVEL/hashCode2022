import sys

from utils.client import Client

fname = sys.argv[1]
filename = fname.split("input/")[1]

clients = []
# Partie Lecture fichier
with open(fname) as f:
    lines = f.readlines()

nb_clients = int(lines[0])
for i in range(1, 2*nb_clients, 2):
    likedIngredients = lines[i]
    dislikedIngredients = lines[i+1]
    client = Client((i-1)/2, likedIngredients, dislikedIngredients)
    clients.append(client)


# print(clients)
# Algo

# Algo 1 : on supprime tous les clients chiants et on satisfait les autres
clientsalgo1 = []
ingredientsOutput = set()
for clientalgo1 in clients:
    if not clientalgo1.hasdislikedingredient():
        ingredientsOutput |= set(clientalgo1.likedIngredients)

# for clientalgo1 in clients:
#     if clientalgo1.hasdislikedingredient():
#         if not clientalgo1.dislikedIngredients.issubset(ingredientsOutput):
#             ingredientsOutput |= set(clientalgo1.likedIngredients)

# Algo 2 : on satisfait les clients dans l'ordre de lecture du fichier
# Algo 3 : on satisfait les clients dans l'ordre inverse de lecture du fichier
# Algo 4 : on groupe les clients qui aiment la même chose 
#               => on satisfait le groupe contenant le plus grand nombre de clients
#               => puis on garde les autres clients qui satisfont les ingrédients choisis
# Algo 5 : on groupe ceux qui n'aiment pas la même chose
#               => on vire ou on garde le groupe contenant le plus grand nombre de clients

# Algo 6: par défaut on ajoute tous les ingrédients (imagine la pizza degueu)
#             on trouve l'élement le moins aimé (en comptant le nombre de dislikes - le nombre de likes) et on l'enleve
#             => on enleve les clients qui aimaient l'ingrédient
#             => et on boucle jusqu'a ne plus avoir de dislikes ?




# Partie Ecriture Sortie
fichier = open("output/" + filename, "w+")
fichier.write(str(len(ingredientsOutput)) + " ")
for ingredient in ingredientsOutput:
    fichier.write(ingredient + " ")
fichier.write("\n")
fichier.close()
