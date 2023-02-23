import matplotlib.pyplot as plt
import numpy as np

# Program that plots the voltage ripple as a function of output current for 2 equivalent Buck-Boost and Buck converters

Io = np.linspace(0, 0.1, 10000)

vB = 0.00026
vBB = Io * (10/297)

plt.figure()

plt.plot(Io, vBB, label='Buck-Boost')
plt.plot([0, 0.1], [vB, vB], label='Buck')
plt.legend()
plt.xlabel('Load Current, A')
plt.ylabel('Voltage Ripple, V')
plt.grid()

plt.show()