import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
import pylab
from scipy.optimize import curve_fit

plt.loglog()

ff=np.logspace(-2, 8, 100)
ww=2*np.pi*ff

C=10**-7
R=67.5
ft=1/(2*np.pi*R*C)
wt=2*np.pi*ft

Af=1/np.sqrt(1+(ft/ff)**2)

plt.plot(ff,Af, color='gray', ls='--', label='sinosoidale')
plt.legend(loc = 'upper right')
dispari=np.arange(1, 5000, 2)

ck=2/(dispari*np.pi)
y=np.empty((len(ff), 100))

for j in range(len(ff)):
    x=np.linspace(-0.5/ff[j], 1.2/ff[j],100)
    for i in range(len(x)):
        Akd=1/np.sqrt(1+((wt/(ww[j]*dispari)))**2)
        fi_d=np.arctan(wt/(ww[j]*dispari))
        b=(ck*Akd*np.sin(ww[j]*dispari*x[i] +fi_d)).sum()
        y[j][i]=b

Ampl=np.empty(len(ff))

for j in range(len(ff)):
    Ampl[j]=np.abs(max(y[j])-min(y[j]))

plt.plot(ff, Ampl, color='green', label='onda quadra')
plt.legend(loc = 'upper right')
pylab.xlabel('$f$ [Hz]')
pylab.ylabel('$A(f)$')

plt.show()
