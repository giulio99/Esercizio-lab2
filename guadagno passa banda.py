import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

ff=np.logspace(0, 6, 100)
ww=2*np.pi*ff

dispari=np.arange(1, 5000, 2)

Ci=2.2*10**-7
Ri=68000
fti=1/(2*np.pi*Ri*Ci)
wti=2*np.pi*fti

Cd=2.2*10**-7
Rd=68
ftd=1/(2*np.pi*Rd*Cd)
wtd=2*np.pi*ftd

ck=2/(dispari*np.pi)
yi=np.empty((len(ff), 100))
yd=np.empty((len(ff), 100))

for j in range(len(ff)):
    x=np.linspace(-0.5/ff[j], 1.2/ff[j],100)
    for i in range(len(x)):
        Aki=1/np.sqrt(1+((ww[j]*dispari)/wti)**2)
        fi_i=np.arctan(-(ww[j]*dispari)/wti)
        a=(ck*Aki*np.sin(ww[j]*dispari*x[i] + fi_i)).sum()
        yi[j][i]=a
        Akd=1/np.sqrt(1+((wtd/(ww[j]*dispari)))**2)
        fi_d=np.arctan(wtd/(ww[j]*dispari))
        b=(ck*Aki*Akd*np.sin(ww[j]*dispari*x[i] + fi_i+fi_d)).sum()
        yd[j][i]=b

Ampli=np.empty(len(ff))
Ampld=np.empty(len(ff))

for j in range(len(ff)):
    Ampli[j]=np.abs(max(yi[j])-min(yi[j]))
    Ampld[j]=np.abs(max(yd[j])-min(yd[j]))
    

Afi=1/np.sqrt(1+(ff/fti)**2)
Afd=(1/np.sqrt(1+(ff/fti)**2))*(1/np.sqrt(1+(ftd/ff)**2))
plt.figure(1)

plt.plot(ff,Afi, color='grey', ls='--')
plt.plot(ff,Afd, color='grey', ls=':')
plt.plot(ff,Ampli, color='red')
plt.plot(ff,Ampld, color='blue')
plt.loglog()
plt.show()

f, vin, dvin, va, dva, vb, dvb=np.loadtxt('dati guadagno.txt', unpack=True)

Aa=va/vin
Ab=vb/vin

plt.figure(2)

plt.errorbar(f, Aa,linestyle='', marker='.', color='black')
plt.errorbar(f, Ab,linestyle='', marker='.', color='green')
plt.plot(ff,Afi, color='grey', ls='--')
plt.plot(ff,Afd, color='grey', ls=':')
plt.plot(ff,Ampli, color='red')
plt.plot(ff,Ampld, color='blue')
plt.loglog()


plt.show()