import numpy as np
import matplotlib.pyplot as plt

##SIMULAZIONI ONDE QUADRA E TRIANGOLARE, COMPLETO


##onda quadra

#crea un array da 1 a 10000 ogni due numeri, quindi partendo da 1 fa tutti i dispari
#modificare il secondo numero in arange per decidere quante iterazioni far fare alla serie di fourier
dispari=np.arange(1, 10000, 2)
#decido la frequenza della mia onda
f=1/5
w=2*np.pi*f

x=np.linspace(0, 10, 1000)
#calcolo i coefficienti della serie
ck=2/(dispari*np.pi)

#creo un array vuoto 
y=np.array([])
for i in range(len(x)):
    #calcolo per ogni x la serie di fourier e la accoda all'array y
    a=(ck*np.sin(w*dispari*x[i])).sum()
    y=np.append(y, a)

#crea un'onda quadra artificiale, e quindi perfetta
yy=np.array([])
for i in x:
    i=i*f
    if(i>round(i)):
        yy=np.append(yy, 0.5)
    elif(i<round(i)):
        yy=np.append(yy, -0.5)
    else:
        yy=np.append(yy, 0)

#plotta la serie di fourier e l'onda artificiale
plt.figure(1)
plt.plot(x,y,linewidth=0.5, color='red')
plt.plot(x,yy,linewidth=0.5,linestyle='--', color='green' )
plt.show()


##onda triangolare

#crea un array da 1 a 50 ogni due numeri, quindi partendo da 1 fa tutti i dispari
#modificare il secondo numero in arange per decidere quante iterazioni far fare alla serie di fourier
dispari=np.arange(1, 50, 2)
#decido la frequenza della mia onda
f=1/5
w=2*np.pi*f
#calcolo i coefficienti della serie
bk=(2/(dispari*np.pi))**2

#come sopra crea un array vuoto, calcola i vari termini e li accoda nell'array
y=np.array([])
for i in range(len(x)):
    b=(bk*np.cos(w*dispari*x[i])).sum()
    y=np.append(y, b)
    
yy=np.array([])
#creo un array dei tempi equispaziati da 0 a 11 (in modo da comprendere anche il 10) di un fattore f/2
xx=np.arange(0,11,(1/f)/2)
for i in xx:
    if(i%(1/f)==0.0):
        yy=np.append(yy, 0.5)
    else:
        yy=np.append(yy, -0.5)

plt.figure(1)
plt.plot(x,y,linewidth=0.5, color='red')
plt.plot(xx,yy,linewidth=0.5,linestyle='--', color='green' )
plt.show()


