import numpy as np

import matplotlib 

import matplotlib.pyplot as plt

#import plotly.offline as ply

from scipy.optimize import curve_fit



##APPROSSIMAZIONE DATI CON LA SIMULAZIONE DI PINNA DI SQUALO, NON COMPLETO

t1, v1=np.loadtxt('pinnet10.txt', unpack=True)

t2, v2=np.loadtxt('pinnet20.txt', unpack=True)

t3, v3=np.loadtxt('pinnet50.txt', unpack=True)

t4, v4=np.loadtxt('pinnet120.txt', unpack=True)

t5, v5=np.loadtxt('pinnet290.txt', unpack=True)

t6, v6=np.loadtxt('pinnet1k.txt', unpack=True)

t6=t6-t6[0]

t=np.array([t1,t2,t3,t4,t5,t6])

t=t/1000000
dt=(t*63)/1000000

#si è misurata v_ref= 4.86 +- 0.03. Da questo si ricava l'errore di calibrazione secondo la calibrazione alternativa e lo si somma in quadratura con l'errore di digitalizzazione
dv1=np.sqrt(1 + (v1*(0.03/1023))**2)
dv2=np.sqrt(1 + (v2*(0.03/1023))**2)
dv3=np.sqrt(1 + (v3*(0.03/1023))**2)
dv4=np.sqrt(1 + (v4*(0.03/1023))**2)
dv5=np.sqrt(1 + (v5*(0.03/1023))**2)
dv6=np.sqrt(1 + (v6*(0.03/1023))**2)

v=np.array([v1,v2,v3,v4,v5,v6])
dv=np.array([dv1,dv2,dv3,dv4,dv5,dv6])

f=np.array([10.448, 25.097, 49.85, 120.78, 289.86, 1001.2])

fig, axs=plt.subplots(3,2)


##simulazione

dispari=np.arange(1, 10000, 2)

w=2*np.pi*f

ampl=max(v[0])-min(v[0])

C=10**-7
dC=10**-8
R=68900
dR=700

ft=1/(2*np.pi*R*C)

wt=2*np.pi*ft

#errore sulla frequenza di taglio
dft=np.sqrt((1/(2*np.pi*R*C**2)*dC)**2+(1/(2*np.pi*C*R**2)*dR)**2)

ck=2/(dispari*np.pi)

y=np.empty((len(f), 1000))

for j in range(len(f)):

    x=np.linspace(0, 5/f[j],1000)

    offset=(max(v[j])-min(v[j]))/2+min(v[j])

    for i in range(len(x)):

        Ak=1/np.sqrt(1+((w[j]*dispari)/wt)**2)

        fi=np.arctan(-(w[j]*dispari)/wt)

        a=offset+ampl*((ck*Ak*np.sin(w[j]*dispari*x[i] + fi+np.pi)).sum())

        y[j][i]=a

#plot

for i in range(3):

    for j in range(2):

        plt.sca(axs[i, j])

        plt.errorbar(t[2*i+j], v[2*i+j], dv[2*i+j], dt[2*i+j], linestyle='', marker='.')

        plt.plot((np.linspace(0, 5/f[2*i+j],1000)), y[2*i+j])

        plt.xticks(np.arange(0,6/f[2*i+j], 1/f[2*i+j]), [0,1,2,3,4,5])

        plt.xlim(-0.1/f[2*i+j], 5/f[2*i+j]+0.1/f[2*i+j])

plt.show()
