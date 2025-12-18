import numpy as np
a_co2=0.3658
b_co2=4.267**-5
T=300
R=8.314
P=50**5
# cofficient vander wall
A=1
B=-(b_co2+T*R/P)
C=a_co2/P
D=-a_co2*b_co2/P
coeffs=[A,B,C,D]
Racine=np.roots(coeffs)
print(Racine)