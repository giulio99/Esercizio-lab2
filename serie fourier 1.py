import numpy as np
import pylab
import matplotlib.pyplot as plt

##SIMULAZIONI ONDE QUADRA E TRIANGOLARE, COMPLETO

##onda quadra
#1
#crea un array da 1 a 10000 ogni due numeri, quindi partendo da 1 fa tutti i dispari
#modificare il secondo numero in arange per decidere quante iterazioni far fare alla serie di fourier
dispari=np.arange(1, 10, 2)
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
plt.subplot(2,2,1)
plt.plot(x,y,linewidth=0.5, color='red', label='n=10')
plt.plot(x,yy,linewidth=0.5,linestyle='--', color='green' )
pylab.ylabel('Simulated Signal [arb.un.]')
plt.legend(loc = 'right')


#2
#crea un array da 1 a 10000 ogni due numeri, quindi partendo da 1 fa tutti i dispari
#modificare il secondo numero in arange per decidere quante iterazioni far fare alla serie di fourier
dispari=np.arange(1, 100, 2)
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
plt.subplot(2,2,2)
plt.plot(x,y,linewidth=0.5, color='red', label='n=100')
plt.plot(x,yy,linewidth=0.5,linestyle='--', color='green' )
plt.legend(loc = 'right')


#3
#crea un array da 1 a 10000 ogni due numeri, quindi partendo da 1 fa tutti i dispari
#modificare il secondo numero in arange per decidere quante iterazioni far fare alla serie di fourier
dispari=np.arange(1, 1000, 2)
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
plt.subplot(2,2,3)
plt.plot(x,y,linewidth=0.5, color='red', label='n=1000')
plt.plot(x,yy,linewidth=0.5,linestyle='--', color='green' )
pylab.xlabel('Time [T]')
pylab.ylabel('Simulated Signal [arb.un.]')
plt.legend(loc = 'right')

#4
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
plt.subplot(2,2,4)
plt.plot(x,y,linewidth=0.5, color='red', label='n=1000')
plt.plot(x,yy,linewidth=0.5,linestyle='--', color='green' )
pylab.xlabel('Time [T]')
plt.legend(loc = 'right')

plt.show()


##onda triangolare


#1
#crea un array da 1 a 50 ogni due numeri, quindi partendo da 1 fa tutti i dispari
#modificare il secondo numero in arange per decidere quante iterazioni far fare alla serie di fourier
dispari=np.arange(1, 3, 2)
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
#Onda triangolare artificiale
xx=np.arange(0,11,(1/f)/2)
for i in xx:
    if(i%(1/f)==0.0):
        yy=np.append(yy, 0.5)
    else:
        yy=np.append(yy, -0.5)

plt.subplot(2,2,1)
plt.plot(x,y,linewidth=0.5, color='red', label='n=3')
plt.plot(xx,yy,linewidth=0.5,linestyle='--', color='green')
pylab.ylabel('Simulated Signal [arb.un.]')
plt.legend(loc = 'right')
#2
#crea un array da 1 a 50 ogni due numeri, quindi partendo da 1 fa tutti i dispari
#modificare il secondo numero in arange per decidere quante iterazioni far fare alla serie di fourier
dispari=np.arange(1, 10, 2)
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
#Onda triangolare artificiale
xx=np.arange(0,11,(1/f)/2)
for i in xx:
    if(i%(1/f)==0.0):
        yy=np.append(yy, 0.5)
    else:
        yy=np.append(yy, -0.5)

plt.subplot(2,2,2)
plt.plot(x,y,linewidth=0.5, color='red', label='n=10')
plt.plot(xx,yy,linewidth=0.5,linestyle='--', color='green')
plt.legend(loc = 'right')
#3
#crea un array da 1 a 50 ogni due numeri, quindi partendo da 1 fa tutti i dispari
#modificare il secondo numero in arange per decidere quante iterazioni far fare alla serie di fourier
dispari=np.arange(1, 20, 2)
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
#Onda triangolare artificiale
xx=np.arange(0,11,(1/f)/2)
for i in xx:
    if(i%(1/f)==0.0):
        yy=np.append(yy, 0.5)
    else:
        yy=np.append(yy, -0.5)

plt.subplot(2,2,3)
plt.plot(x,y,linewidth=0.5, color='red',label='n=20')
plt.plot(xx,yy,linewidth=0.5,linestyle='--', color='green')
pylab.xlabel('Time [T]')
pylab.ylabel('Simulated Signal [arb.un.]')
plt.legend(loc = 'right')
#4
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
#Onda triangolare artificiale
xx=np.arange(0,11,(1/f)/2)
for i in xx:
    if(i%(1/f)==0.0):
        yy=np.append(yy, 0.5)
    else:
        yy=np.append(yy, -0.5)

plt.subplot(2,2,4)
plt.plot(x,y,linewidth=0.5, color='red',label='n=50')
plt.plot(xx,yy,linewidth=0.5,linestyle='--', color='green')
pylab.xlabel('Time [T]')
plt.legend(loc = 'right')

plt.show()



