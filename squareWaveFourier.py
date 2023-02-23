import numpy as np
import matplotlib.pyplot as plt

# Program that sums a specified number of sine waves to generate a square wave

n = range(1, 12)

Vdc = 5

x = Vdc/2 * np.ones(10000)
t = np.linspace(-1, 2*np.pi+1, 10000)

for i in n:
    if (i % 2) != 0:
        x = x + (2*Vdc/(np.pi*i)) * np.sin(i*t)

plt.figure(figsize=(4, 4), dpi=200)
plt.plot(t, x)
plt.show()
