import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
import plotly.offline as ply
from scipy.optimize import curve_fit

t1, v1=np.loadtxt('pinnat10.txt', unpack=True)
t2, v2=np.loadtxt('pinnat20.txt', unpack=True)
t3, v3=np.loadtxt('pinnat50.txt', unpack=True)
t4, v4=np.loadtxt('pinnat120.txt', unpack=True)
t5, v5=np.loadtxt('pinnat290.txt', unpack=True)
t6, v6=np.loadtxt('pinnat1k.txt', unpack=True)

t6=t6-t6[0]
t=np.array([t1,t2,t3,t4,t5,t6])
t=t/1000000
v=np.array([v1,v2,v3,v4,v5,v6])
f=np.array([10.448, 25.097, 49.85, 120.78, 289.86, 1001.2])

fig, axs=plt.subplots(3,2)


##simulazione
dispari=np.arange(1, 10000, 2)
w=2*np.pi*f

ampl=max(v[0])-min(v[0])

C=10**-7
R=68900
ft=1/(2*np.pi*R*C)
wt=2*np.pi*ft

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
        plt.errorbar(t[2*i+j], v[2*i+j], linestyle='', marker='.')
        plt.plot((np.linspace(0, 5/f[2*i+j],1000)), y[2*i+j])
        plt.xticks(np.arange(0,6/f[2*i+j], 1/f[2*i+j]), [0,1,2,3,4,5])
        plt.xlim(-0.1/f[2*i+j], 5/f[2*i+j]+0.1/f[2*i+j])

plt.show()



















