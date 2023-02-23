import matplotlib.pyplot as plt
import numpy as np

# Program that plots the realtionship between the voltage ration and duty cycle of a boost converter

D = np.linspace(0, 1, 10000)

vRatio = 1/(1-D)

plt.figure()

plt.plot(D, vRatio)
plt.grid()
plt.ylim([0, 10])
plt.xlim([0, 1])

plt.show()