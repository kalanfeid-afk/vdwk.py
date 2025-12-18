import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
C=np.array([0.5,1,2,3,4,5]) # concentrations mg/L
A=np.array([0.138, 0.204, 0.431,0.703,0.828,1.08]) # absorbances
# Calcul de la régression linéaire(A=f(C))
slope, intercept, r_value, p_value, std_err = linregress(C,A)
#DROITE D4ETALONNAGE
C_fit = np.linspace(0, 5, 100)
A_fit = slope * C_fit + intercept
# Affichage des points expérimentaux et de la droite d'étalonnage
plt.figure()
plt.scatter(C, A, color='blue', label='Données expérimentales')
plt.plot(C_fit, A_fit, color='red', label='Droite d\'étalonnage')
plt.xlabel('Concentration (mol/L)')
plt.ylabel('Absorbance')
plt.title('Droite d\'étalonnage')
plt.grid(True)
plt.show()


            