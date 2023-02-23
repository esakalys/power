import numpy as np

# Program that estimates the amplitude of a voltage waveform and a current waveform as well as the phase angle between them
# using 2 consecutive measurements at a given sampling frequency

# Define parameters
v = [9.415, 18.772]
i = [45.312, 50.346]
f = 50
omega = 2*np.pi*f
fSam = 4e3
tSam = 1/fSam
# Parameters defined

V = np.sqrt((v[0]**2 + v[1]**2 - 2*v[0]*v[1]*np.cos(omega*tSam))/(np.sin(omega*tSam)**2))
I = np.sqrt((i[0]**2 + i[1]**2 - 2*i[0]*i[1]*np.cos(omega*tSam))/(np.sin(omega*tSam)**2))
theta = np.arccos((i[0]*v[0] + i[1]*v[1] - (i[0]*v[1] + i[1]*v[0])*np.cos(omega*tSam))/(V*I*np.sin(omega*tSam)**2))
theta = np.rad2deg(theta)

print(f'Voltage = {V}')
print(f'Current = {I}')
print(f'Phase angle = {theta}')