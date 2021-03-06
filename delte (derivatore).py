import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
import pylab
#import plotly.offline as ply

#DERIVATA QUADRATA

dispari=np.arange(1, 10000, 2)
f=np.array([ 50, 70, 100, 300, 500, 1000,3000, 5000,10000, 20000])
w=2*np.pi*f

C=10**-6
R=680
ft=1/(2*np.pi*R*C)
wt=2*np.pi*ft

ck=2/(dispari*np.pi)
y=np.empty((len(f), 1000))

for j in range(len(f)):
    x=np.linspace(0, 4/f[j],1000)
    for i in range(len(x)):
        Ak=1/np.sqrt(1+((wt/(w[j]*dispari)))**2)
        fi=np.arctan(wt/(w[j]*dispari))
        a=(ck*Ak*np.sin(w[j]*dispari*x[i] + fi)).sum()
        y[j][i]=a
    

fig, axs=plt.subplots(5,2)
fig.subplots_adjust(hspace=0)

for i in range(5):
    for j in range(2):
        plt.sca(axs[i, j])
        plt.plot((np.linspace(0, 4/f[2*i+j],1000)), y[2*i+j], label='f=%d Hz'%(f[2*i+j]))
        plt.xticks(np.arange(0,5/f[2*i+j], 1/f[2*i+j]), [0,1,2,3,4])
        pylab.xlabel('Time [T]')
        plt.xlim(-0.1/f[2*i+j], 4/f[2*i+j]+0.1/f[2*i+j])
        plt.legend(loc = 'upper right')
        
for i in range(5):
    for j in range(2):
        if(i!=4):
            plt.setp(axs[i][j].get_xticklabels(), visible=False)
            
            
# add a big axis, hide frame
fig.add_subplot(111, frameon=False)
# hide tick and tick label of the big axis
plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
#plt.xlabel("common X")
plt.ylabel("Simulated Signal [arb.un.]")

plt.show()

