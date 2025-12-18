import numpy as np
from scipy.optimize import fsolve
T=331.153 #t température K
P=7*10**5 #en pa 
R=8.314
Tc=405.4
Pc=1.135*10**7 # en pa
W=0.256
Pr=P/Pc
Tr=T/Tc
ac=0.45724*(R**2)*(Tc**2)/Pc
b=0.0778*R*Tc/Pc
k=0.37464+1.54226*W-0.26992*W**2
m=(1+k*(1-Tr**0.5))**2
a=ac*m
def peng_robinson(V):
    return P-(R*T)/(V-b)-a*m/(V**2+2*b*V-b**2)
V_initial=R*T/P
V_solution=fsolve(peng_robinson, V_initial)
V=V_solution[0]
print("Le volume molaire V est de {:.4f} m³/mol".format(V))


