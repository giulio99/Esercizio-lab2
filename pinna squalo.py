import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
import plotly.offline as ply

##SIMULAZIONE PINNA DI SQUALO, COMPLETO

#crea un array da 1 a 10000 con un numero si e uno no, quindi partendo da 1 tutti i dispari
dispari=np.arange(1, 10000, 2)
#array contenente le frequenze delle onde in entrata
f=np.array([ 50, 70, 100, 300, 500, 1000,3000, 5000,10000, 20000])
w=2*np.pi*f

#valori del condensatore e della resistenza, con il calcolo delle relative frequenze di taglio
C=10**-7
R=3300
ft=1/(2*np.pi*R*C)
wt=2*np.pi*ft

#calcola i coefficienti della serie di fourier per una quadra
ck=2/(dispari*np.pi)
#crea una matrice vuota(10*1000 in questo caso) da vedere come un 'array di array', dove andranno le y a seconda delle varie frequenze
y=np.empty((len(f), 1000))

#cicli for per le serie di fourier
for j in range(len(f)):
    x=np.linspace(0, 4/f[j],1000)#crea un array di mille punti in un intervallo di 4 periodi a seconda della frequenza
    for i in range(len(x)):
        #calcola Ak e fi attenuazione e sfasamento a seconda della frequenza, poi somma tutti i termini della serie di fourier e li
        # introduce nella corretta riga della matrice y
        Ak=1/np.sqrt(1+((w[j]*dispari)/wt)**2)
        fi=np.arctan(-(w[j]*dispari)/wt)
        a=(ck*Ak*np.sin(w[j]*dispari*x[i] + fi)).sum()
        y[j][i]=a
    
#crea 10 subplots in maniera da essere selezionabili attraverso degli indici i e j
fig, axs=plt.subplots(5,2)
fig.subplots_adjust(hspace=0)
'''
questo era una versione precedente, equivalente al for di sotto

axs[0][0].plot((np.linspace(0, 4/f[0],1000)), y[0])
axs[0][1].plot((np.linspace(0, 4/f[1],1000)), y[1])
axs[1][0].plot((np.linspace(0, 4/f[2],1000)), y[2])
axs[1][1].plot((np.linspace(0, 4/f[3],1000)), y[3])
axs[2][0].plot((np.linspace(0, 4/f[4],1000)), y[4])
axs[2][1].plot((np.linspace(0, 4/f[5],1000)), y[5])
axs[3][0].plot((np.linspace(0, 4/f[6],1000)), y[6])
axs[3][1].plot((np.linspace(0, 4/f[7],1000)), y[7])
axs[4][0].plot((np.linspace(0, 4/f[8],1000)), y[8])
axs[4][1].plot((np.linspace(0, 4/f[9],1000)), y[9])
'''
#plotta  tutte e dieci le onde quadre integrate a varie frequenze, limitando gli estremi delle x a 4 periodi e settando i ticks
#in unità di periodo, inoltre mette solo gli assi delle x in fondo

for i in range(5):
    for j in range(2):
        plt.sca(axs[i, j])
        plt.plot((np.linspace(0, 4/f[2*i+j],1000)), y[2*i+j], label='f=%d'%(f[2*i+j]))
        plt.xticks(np.arange(0,5/f[2*i+j], 1/f[2*i+j]), [0,1,2,3,4])
        plt.xlim(-0.1/f[2*i+j], 4/f[2*i+j]+0.1/f[2*i+j])
        pylab.xlabel('Time [T]')
        plt.legend(loc = 'right')
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







