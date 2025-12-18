## Affichage des éléments d'une liste avec leurs indices
t=[6,12,9,1,5,10,8,3,4,13]
n=len(t)
for i in range(n):
    print("t[{}]:{}".format(i,t[i]))
#affichage du maximum de tableau 
maximum=t[0]
for valeur in t:
    if valeur>maximum:
        maximum=valeur
print("le maximum est =",maximum)
#affichage du minimum de tableau
minimum=t[0]
for valeur in t:
    if valeur<minimum:
        minimum=valeur
print("le minimum est =",minimum)
print("il se trouve à l'indice",t.index(minimum))
#affichage de la somme des éléments du tableau
somme=0
for valeur in t:
    somme=somme+valeur
print("la somme des éléments du tableau est =",somme)
#affchage le nombre de valeurs>10
compteur=0
for valeur in t:
    if valeur>10:
        compteur=compteur+1
print("le nombre de valeurs supérieures à 10 est =",compteur)
#affichage de la moyenne des éléments du tableau
moyenne=somme/n
print("la moyenne des éléments du tableau est =",moyenne)
#affichage des éléments pairs du tableau
print("les éléments pairs du tableau sont:")
for valeur in t:
    if valeur%2==0:
        print(valeur)
        ## nombre de valeurs paires
compteur_pairs=0
for valeur in t:
    if valeur%2==0:
        compteur_pairs=compteur_pairs+1
print("le nombre de valeurs paires est =",compteur_pairs)
#affichage des éléments impairs du tableau
print("les éléments impairs du tableau sont:")
for valeur in t:
    if valeur%2!=0:
        print(valeur)
        ## nombre de valeurs impaires
compteur_impairs=0
for valeur in t:
    if valeur%2!=0:
        compteur_impairs=compteur_impairs+1
print("le nombre de valeurs impaires est =",compteur_impairs)
#trie du tableau par ordre croissant
for i in range(n):
    for j in range(i+1,n):
        if t[i]>t[j]:
            t[i],t[j]=t[j],t[i]
print("le tableau trié par ordre croissant est:",t)
       