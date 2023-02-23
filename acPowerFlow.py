import numpy as np
import matplotlib.pyplot as plt

# Program that plots the real power flow based on the phase between current and voltage

f = 1
theta = np.linspace(0, 2*np.pi, 100)
t = np.linspace(0, 1, 1000)

index = 0
pAvg = []

for i in theta:
    v = 5*np.cos(2*np.pi*f*t)
    i = 1*np.cos(2*np.pi*f*t + i)
    p = v*i
    pAvg.append(np.average(p))

plt.figure()
plt.plot(theta*180/np.pi, pAvg)
plt.xlabel('Phase Angle, degrees')
plt.ylabel('Average Power')
plt.grid()
plt.show()