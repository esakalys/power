import numpy as np

# Program used to find the firing angle of a thyristor controlled reactor based on the reactive power requirement

# Define parameters
qReq = 9.7e6
L = 80e-3
V = 42e3
omega = 2*np.pi*50
# Parameters defined

# Range of firing angles
alpha = np.linspace(np.pi/2, np.pi, 10000) # From 90 degrees to 180 degrees

# Calculations to find the required angle
qRange = np.zeros(alpha.size)

index = 0
for a in alpha:
    q = V**2/(omega*L) * (2 - a*(2/np.pi) + np.sin(2*a)/np.pi)
    q = abs(q - qReq)
    qRange[index] = q
    index += 1

# Index of angle value that gives us the required reactive power
index = np.argmin(qRange)

# Required firing angle
result = round(np.rad2deg(alpha[index]), 2)

print(f'Required firing angle is {result} degrees.')
