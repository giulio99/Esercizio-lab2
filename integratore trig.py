import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
import plotly.offline as ply


dispari=np.arange(1, 50, 2)
f=np.array([ 5, 20, 50, 100, 300, 500,1000, 3000,5000, 10000])
w=2*np.pi*f

C=10**-7
R=3300
ft=1/(2*np.pi*R*C)
wt=2*np.pi*ft

bk=(2/(dispari*np.pi))**2
y=np.empty((len(f), 1000))

for j in range(len(f)):
    x=np.linspace(0, 4/f[j],1000)
    for i in range(len(x)):
        Ak=1/np.sqrt(1+((w[j]*dispari)/wt)**2)
        fi=np.arctan(-(w[j]*dispari)/wt)
        a=(bk*Ak*np.cos(w[j]*dispari*x[i] + fi)).sum()
        y[j][i]=a
    

fig, axs=plt.subplots(5,2)
fig.subplots_adjust(hspace=0)

for i in range(5):
    for j in range(2):
        plt.sca(axs[i, j])
        plt.plot((np.linspace(0, 4/f[2*i+j],1000)), y[2*i+j])
        plt.xticks(np.arange(0,5/f[2*i+j], 1/f[2*i+j]), [0,1,2,3,4])
        plt.xlim(-0.1/f[2*i+j], 4/f[2*i+j]+0.1/f[2*i+j])
        
for i in range(5):
    for j in range(2):
        if(i!=4):
            plt.setp(axs[i][j].get_xticklabels(), visible=False)

plt.show()