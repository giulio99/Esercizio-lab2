import numpy as np
import matplotlib.pyplot as plt

##onda quadra

#crea un array da 1 a 10000 ogni due numeri, quindi partendo da 1 fa tutti i dispari
#modificare il secondo numero in arange per decidere quante iterazioni far fare alla serie di fourier
dispari=np.arange(1, 10000, 2)
#decido la frequenza della mia onda
f=40
w=2*np.pi*f

Cd=10**-5
Rd=1600
ftd=1/(2*np.pi*Rd*Cd)
wtd=2*np.pi*ftd

ck=2/(dispari*np.pi)

yd=np.empty((1000))

x=np.linspace(0, 4/f,num=1000)
for i in range(len(x)):
        Akd=1/np.sqrt(1+((wtd/(w*dispari)))**2)
        fi_d=np.arctan(wtd/(w*dispari))
        b=(ck*Akd*np.sin(w*dispari*x[i]+fi_d)).sum()
        yd[i]=b

plt.figure(1)
plt.plot(x,yd,linewidth=0.5, color='red')

plt.show()
