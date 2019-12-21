import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

f, vin, va, vb=np.loadtxt('dati guadagno.txt', unpack=True)

Aa=va/vin

Ab=vb/vin

plt.plot(f, Aa, linestyle='', marker='.')
plt.loglog()
plt.show()
