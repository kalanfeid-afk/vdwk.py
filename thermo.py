import numpy as np 
x=3
y=4
z=x+y
v=np.exp(z)
print(v)
T=250
B0=-1.503**-4
B1=-2.130**-4
B2=252.5
K=[250,300,350,400,450,500]
for T in K:
    B=B0+B1*np.exp(-B2/T)
    print("T =",T,"B =",B)
L=list(range(1,10))
R=8,31
P=1
T=300
for P in L:
    Z=1+B*P*1**5/(R*T)
    print("P =",P,"Z =",Z)








