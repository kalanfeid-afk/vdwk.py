import numpy as np
import matplotlib.pyplot as plt
R=8.314  # J/(mol·K), universal gas constant
a=3.59  # L²·bar/mol², Van der Waals constant for attraction
b=0.0427  # L/mol, Van der Waals constant for volume
def pression_vdw(V, T):
    return (R * T) / (V - b) - a / V**2 
T_liste= []  # Temperatures en Kelvin
p_liste= []  # Correspond presions en bar
v=1 # Volume en L
for T in range(300, 320,1):
    T_liste.append(T)
    p_liste.append(pression_vdw(v, T))
plt.plot(T_liste, p_liste)
plt.xlabel("Température (K)")
plt.ylabel("Pression (atmosphères)")
plt.title("courbe p=f(T)")
plt.grid(True)
plt.show()




        
        