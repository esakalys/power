
import dqabTransforms as tr
import matplotlib.pyplot as plt
import numpy as np
from plotVector import plotVector

# Program that shows the initial angle of the alpha beta vector at t = 0

V = 690 * (np.sqrt(2)/np.sqrt(3))

a = V*np.sin(0)
b = V*np.sin(-np.pi*(2/3))
c = V*np.sin(-np.pi*(4/3))

v = np.array([[a],[b],[c]])

res = tr.abc2ab(v)

alpha = float(res[0])
beta = float(res[1])

print(f'Alpha = {alpha}, Beta = {beta}')

plt.figure(figsize=(4, 4), dpi=200)
plt.plot([0, alpha], [0, beta], marker='x', label='alpha beta')
plt.plot([0, a*np.cos(0)],[0, a*np.sin(0)], marker='x', label='a')
plt.plot([0, b*np.cos(np.pi*(2/3))],[0, b*np.sin(np.pi*(2/3))], marker='x', label='b')
plt.plot([0, c*np.cos(np.pi*(4/3))],[0, c*np.sin(np.pi*(4/3))], marker='x', label='c')
plt.grid()
plt.legend()
plt.show()