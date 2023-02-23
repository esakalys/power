import numpy as np
import matplotlib.pyplot as plt

# Program calculates and plots the DC side voltages of a thyristor rectifier based on the given firing angle

# Firing angle of the thyristor
alpha = np.pi/4

# Range of phase angles
angle = np.linspace(0, 2*np.pi, 100000)

# Defining the three-phase voltage phasors
Va = 230*np.sin(angle)
Vb = 230*np.sin(angle + np.pi * (2 / 3))
Vc = 230*np.sin(angle + np.pi * (4 / 3))

# Calculates the voltage of the upper leg based on the firing angle
Vup = []
for a in angle:
    if a <= np.pi/6 + alpha:
        Vup.append(230 * np.sin(a + np.pi * (2 / 3)))
    if (a > np.pi/6 + alpha) and (a <= np.pi*(5/6) + alpha):
        Vup.append(230 * np.sin(a))
    if (a > np.pi*(5/6) + alpha) and (a <= np.pi*(3/2) + alpha):
        Vup.append(230 * np.sin(a + np.pi * (4 / 3)))
    if a > np.pi*(3/2) + alpha:
        Vup.append(230 * np.sin(a + np.pi * (2 / 3)))

# Calculates the voltage of the lower leg based on the firing angle
Vlo = []
for a in angle:
    if a <= np.pi/2 + alpha:
        Vlo.append(230 * np.sin(a + np.pi * (4 / 3)))
    if (a > np.pi/2 + alpha) and (a <= np.pi*(7/6) + alpha):
        Vlo.append(230 * np.sin(a + np.pi * (2 / 3)))
    if (a > np.pi*(7/6) + alpha) and (a <= np.pi*(11/6) + alpha):
        Vlo.append(230 * np.sin(a))
    if a > np.pi*(11/6) + alpha:
        Vlo.append(230 * np.sin(a + np.pi * (4 / 3)))

VupNp = np.array(Vup)
VloNp = np.array(Vlo)

# DC side voltage
Vdc = VupNp - VloNp

# Calculating the average DC side voltage numerically and analytically for comparison
avgVdcN = 230*np.sqrt(3) * 3/np.pi * np.cos(alpha)
avgVdcA = np.average(Vdc)

print('Comparing the average DC voltage results:')
print('Analytical: ' + str(avgVdcA))
print('Numerical: ' + str(avgVdcN))

plt.figure(figsize=(6, 4), dpi=200)
plt.plot(angle, Va, label='Va')
plt.plot(angle, Vb, label='Vb')
plt.plot(angle, Vc, label='Vc')
plt.plot(angle, Vup, label='Vupper')
plt.plot(angle, Vlo, label='Vlower')
plt.plot(angle, Vdc, label='Vdc')
plt.grid()
plt.legend()
plt.show()
