import numpy as np
import sympy as sp
from addingSines import addSines

# Program that carries out the Clarke Transformation on a three-phase system

# Define symbolic time variable
t = sp.symbols('t')

# Define amplitudes, phases and rotational frequency
aA = np.sqrt(2)*230
aAngle = 10

bA = np.sqrt(2)*230
bAngle = -110

cA = np.sqrt(2)*230
cAngle = 130

f = 50
omega = 2*np.pi*f
# Amplitudes, phases and frequency defined

# Defining phasors
a = aA* sp.sin(omega*t + np.deg2rad(aAngle))
b = bA * sp.sin(omega*t + np.deg2rad(bAngle))
c = cA * sp.sin(omega*t + np.deg2rad(cAngle))

# Clarke Transformation using the symbolic variables
alpha = sp.simplify(2/3*(a - 0.5*b - 0.5*c))
beta = sp.simplify(2/3*((np.sqrt(3)/2)*b - (np.sqrt(3)/2)*c))

print('Symbolic Toolbox:')
print(f'Alpha component = {alpha}')
print(f'Beta component = {beta}\n')

# Clarke Transformation using addition of sines
alphaA, alphaAngle = addSines(2/3*aA, aAngle, -2/3*0.5*bA, bAngle)
alphaA, alphaAngle = addSines(alphaA, alphaAngle, -2/3*0.5*cA, cAngle)

betaA, betaAngle = addSines((2/3)*(np.sqrt(3)/2)*bA, bAngle, -(2/3)*(np.sqrt(3)/2)*cA, cAngle)

print('Adding Sines Method:')
print(f'Alpha component = {round(alphaA, 2)}*sin(wt + ({round(alphaAngle, 2)}))')
print(f'Alpha component = {round(alphaA, 2)}*cos(wt + ({round(alphaAngle-90, 2)})) (converted to cos)')
print(f'Beta component = {round(betaA, 2)}*sin(wt + ({round(betaAngle, 2)}))')
