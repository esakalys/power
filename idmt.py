import matplotlib.pyplot as plt
import numpy as np

# Program that plots the charactersitic of a voltage sensitive IDMT relay

Is = 0.9
TMS = 0.18
PMS = 0.23
CT = 300

I = np.linspace(100, 1000, 100000)

t = TMS * 13.5/((I/(CT*Is))-1)
tS = TMS * 13.5/((I/(CT*PMS*Is))-1)

plt.figure()

plt.plot(I, t, label='Non-Sensitive')
plt.plot(I, tS, label='Sensitive')
plt.grid()
plt.legend()
#plt.xlim([269.99, 270])
plt.ylim([0, 8])

plt.show()
