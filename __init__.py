nombres = input("Entrez des nombres séparés par des espaces : ")

liste_nombres = [int(n) for n in nombres.split()]

max_nombre = liste_nombres[0]

for nombre in liste_nombres:
    if nombre > max_nombre:
        max_nombre = nombre

print("Le nombre maximum est :", max_nombre)
