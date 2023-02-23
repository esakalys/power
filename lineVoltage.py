import numpy as np
import matplotlib.pyplot as plt

# Program the plots ll the line voltages of a three phase system

theta = np.linspace(0, 2*np.pi, 10000)

Va = 230*np.sin(theta)
Vb = 230*np.sin(theta + np.pi*(2/3))
Vc = 230*np.sin(theta - np.pi*(2/3))

Vab = abs(Va - Vb)
Vac = abs(Va - Vc)
Vbc = abs(Vb - Vc)

plt.figure(figsize=(6, 4), dpi=200)
plt.plot(theta, Va, label='Va')
plt.plot(theta, Vb, label='Vb')
plt.plot(theta, Vc, label='Vc')
plt.plot(theta, Vac, label='Vac')
plt.plot(theta, Vab, label='Vab')
plt.plot(theta, Vbc, label='Vbc')
plt.legend()
plt.grid()
plt.show()
