import numpy as np
import matplotlib.pyplot as plt

##onda quadra

dispari=np.arange(1, 10000, 2)
f=1/5
w=2*np.pi*f

x=np.linspace(0, 10, 1000)
ck=2/(dispari*np.pi)

y=np.array([])
for i in range(len(x)):
    a=(ck*np.sin(w*dispari*x[i])).sum()
    y=np.append(y, a)

yy=np.array([])
for i in x:
    i=i*f
    if(i>round(i)):
        yy=np.append(yy, 0.5)
    elif(i<round(i)):
        yy=np.append(yy, -0.5)
    else:
        yy=np.append(yy, 0)

plt.figure(1)
plt.plot(x,y,linewidth=0.5, color='red')
plt.plot(x,yy,linewidth=0.5,linestyle='--', color='green' )
plt.show()


##onda triangolare


dispari=np.arange(1, 50, 2)
bk=(2/(dispari*np.pi))**2

y=np.array([])
for i in range(len(x)):
    b=(bk*np.cos(w*dispari*x[i])).sum()
    y=np.append(y, b)

yy=np.array([])


plt.figure(1)
plt.plot(x,y,linewidth=0.5, color='red')
#plt.plot(x,yy,linewidth=0.5,linestyle='--', color='green' )
plt.show()
