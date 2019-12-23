import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

##FIT GUADAGNO IN FUNZIONE DELLA FREQUENZA, IN CORSO
#manca la propagazione degli errori sul guadagno(ci sono degli errori fittizzi per vedere l'approssimazione al modello)
# e tutta la parte di fit effettivo

f, vin, va, vb=np.loadtxt('dati guadagno.txt', unpack=True)

Aa=va/vin

Ab=vb/vin

plt.errorbar(f, Aa,[0.5,0.3,0.1,0.05,0.02,0.01,0.001,0.0007,0.0003],linestyle='', marker='.', color='red')
plt.loglog()

ff=np.logspace(0, 6, 1000)

C=2.2*10**-7
R=68900
ft=1/(2*np.pi*R*C)
wt=2*np.pi*ft

Af=1/np.sqrt(1+(ff/ft)**2)

plt.plot(ff,Af, color='blue')

plt.show()
