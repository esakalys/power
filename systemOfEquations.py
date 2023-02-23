import numpy as np
import recPol as rp

# Solve the system of equations with coefficient Matrix A and right-hand side vector B
A = np.array([[((1/250) + (1/(100 + 125.7j)) + (1/(-159.2j))), (1/(159.2j))],
              [(1/159.2j), (1/400) + (1/-159.2j)]])

B = np.array([[20/(100+125.7j)],
              [0.1]])

x = np.matmul(np.linalg.inv(A), B)


print(f'Rectangular: A = {x[0]}, B = {x[1]}')

vA = rp.rec2pol(x[0], deg=True)
vB = rp.rec2pol(x[1], deg=True)

print(f'Polar: A = {vA}, B = {vB}')
