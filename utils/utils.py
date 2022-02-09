# init liste with int val
liste = [i for i in range(50)]
print(liste)

## Parcours liste entre deux valeurs:
liste = liste[2:5]
print(liste)

## Générateur
def _generator():
    for obj in liste:
        if not obj.something:
            yield obj


## CopyArray without modifying source
copy = liste[:]
copy = copy[0:-1]
print(copy)
print(liste)
