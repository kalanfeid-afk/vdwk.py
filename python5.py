X=int(input("entrer X"))
Y=int(input("entre Y"))
Z=int(input("entrer Z"))
if X>=Y and X>=Z:
    max=X
elif Y>=X and Y>=Z:
    max=Y
else:
    max=Z
print("la valeur de max est=",max)
    