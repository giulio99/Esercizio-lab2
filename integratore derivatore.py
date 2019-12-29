import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
#import plotly.offline as ply


dispari=np.arange(1, 10000, 2)
f=np.array([ 5, 20, 50, 100, 300, 500,1000, 3000,5000, 10000])
w=2*np.pi*f

Ci=10**-7
Ri=32800
fti=1/(2*np.pi*Ri*Ci)
wti=2*np.pi*fti

Cd=10**-7
Rd=67.5
ftd=1/(2*np.pi*Rd*Cd)
wtd=2*np.pi*ftd

ck=2/(dispari*np.pi)
yi=np.empty((len(f), 1000))
yd=np.empty((len(f), 1000))
for j in range(len(f)):
    x=np.linspace(0, 4/f[j],1000)
    for i in range(len(x)):
        Aki=1/np.sqrt(1+((w[j]*dispari)/wti)**2)
        fi_i=np.arctan(-(w[j]*dispari)/wti)
        a=(ck*Aki*np.sin(w[j]*dispari*x[i] + fi_i)).sum()
        yi[j][i]=a
        Akd=1/np.sqrt(1+((wtd/(w[j]*dispari)))**2)
        fi_d=np.arctan(wtd/(w[j]*dispari))
        b=(ck*Aki*Akd*np.sin(w[j]*dispari*x[i] + fi_i+fi_d)).sum()
        yd[j][i]=b


fig1, axs1=plt.subplots(5,2)
fig1.subplots_adjust(hspace=0)

for i in range(5):
    for j in range(2):
        plt.sca(axs1[i, j])
        plt.plot((np.linspace(0, 4/f[2*i+j],1000)), yi[2*i+j])
        plt.xticks(np.arange(0,5/f[2*i+j], 1/f[2*i+j]), [0,1,2,3,4])
        plt.xlim(-0.1/f[2*i+j], 4/f[2*i+j]+0.1/f[2*i+j])
        
for i in range(5):
    for j in range(2):
        if(i!=4):
            plt.setp(axs1[i][j].get_xticklabels(), visible=False)
            
fig2, axs2=plt.subplots(5,2)
fig2.subplots_adjust(hspace=0)

for i in range(5):
    for j in range(2):
        plt.sca(axs2[i, j])
        plt.plot((np.linspace(0, 4/f[2*i+j],1000)), yd[2*i+j],label='f=%d Hz'%(f[2*i+j]))
        plt.xticks(np.arange(0,5/f[2*i+j], 1/f[2*i+j]), [0,1,2,3,4])
        plt.xlim(-0.1/f[2*i+j], 4/f[2*i+j]+0.1/f[2*i+j])
        plt.legend(loc = 'upper right')
        pylab.xlabel('Time [T]')
for i in range(5):
    for j in range(2):
        if(i!=4):
            plt.setp(axs2[i][j].get_xticklabels(), visible=False)
fig2.text(0.04, 0.5, 'Simulated Signal [arb.un.]', va='center', rotation='vertical')

plt.show()
