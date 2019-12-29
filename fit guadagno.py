import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

##FIT GUADAGNO IN FUNZIONE DELLA FREQUENZA, IN CORSO
#manca la propagazione degli errori sul guadagno(ci sono degli errori fittizzi per vedere l'approssimazione al modello)
# e tutta la parte di fit effettivo

f, vin, dvin, va, dva, vb, dvb=np.loadtxt('dati guadagno.txt', unpack=True)

Aa=va/vin
dAa= np.sqrt(((1/vin)*2*dva)**2+((va/vin**2)*2*dvin)**2)

Ab=vb/vin
plt.errorbar(f, Aa,dAa,linestyle='', marker='.', color='red')
#plt.errorbar(f, Aa,[0.5,0.3,0.1,0.05,0.02,0.01,0.001,0.0007,0.0003],linestyle='', marker='.', color='red')
plt.loglog()

ff=np.logspace(0, 6, 100)
ww=2*np.pi*ff

C=2.2*10**-7
R=68900
ft=1/(2*np.pi*R*C)
wt=2*np.pi*ft

Af=1/np.sqrt(1+(ff/ft)**2)

plt.plot(ff,Af, color='blue')

#simulazione per varie frequenze 
#ATTENZIONE, fa un sacco di operazioni, non aumentare il numero di dispari, ff , y e x altrimenti ti si pianta il computer
dispari=np.arange(1, 5000, 2)

ck=2/(dispari*np.pi)
y=np.empty((len(ff), 100))

for j in range(len(ff)):
    x=np.linspace(-0.5/ff[j], 1.2/ff[j],100)
    for i in range(len(x)):
        Ak=1/np.sqrt(1+((ww[j]*dispari)/wt)**2)
        fi=np.arctan(-(ww[j]*dispari)/wt)
        a=(ck*Ak*np.sin(ww[j]*dispari*x[i] + fi)).sum()
        y[j][i]=a

Ampl=np.empty(len(ff))

for j in range(len(ff)):
    Ampl[j]=np.abs(max(y[j])-min(y[j]))

plt.plot(ff, Ampl, color='green')

plt.show()
