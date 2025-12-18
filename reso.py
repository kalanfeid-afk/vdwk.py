a=2.303
b=0.013697
T=773
P=15
R=0.08314
A=P
B=-(P*b+R*T)
C=a 
D=-a*b
coeffs=[A,B,C,D]
import numpy as np
Racine=np.roots(coeffs)
print(Racine)



