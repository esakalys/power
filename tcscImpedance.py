import numpy as np
import matplotlib.pyplot as plt

# Program that plots the impedance of a thyristor controlled series compensator (TCSC) 
# as a function of the thyrisor firing angle

# Define parameters
Xc = 10
Xl = 2
# Parameters defined

# Range of firing angles
alpha = np.linspace(np.pi/2, np.pi, 1000)

# Calculating the impedance of the thyristor controlled reactor
Xtcr = Xl * np.pi/(2*np.pi - 2*alpha + np.sin(2*alpha))

# Calculating the impedance of the TCSC
Xtcsc = (Xtcr*Xc)/(Xc-Xtcr)

# Converting to degrees for the plot
alpha = np.rad2deg(alpha)

plt.figure(figsize=(6, 3), dpi=200)
plt.plot(alpha, Xtcsc)
plt.grid()
plt.ylim([-50, 50])
plt.show()
