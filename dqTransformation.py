import numpy as np
import sympy as sp

# Program that carries out the Park Transformation on an imbalanced alpha-beta system

# Define symbolic time variable
t = sp.symbols('t')

# Define amplitudes, phases and rotational frequency
alphaA = 325.12
alphaAngle = 9.83

betaA = 285.53
betaAngle = -75.13

f = 50
omega = 2*np.pi*f

fDq = 50
omegaDq = 2*np.pi*fDq
# Amplitudes, phases and frequency defined

# Defining phasors
alpha = alphaA* sp.sin(omega*t + np.deg2rad(alphaAngle))
beta = betaA * sp.sin(omega*t + np.deg2rad(betaAngle))

# Park Transformation using the symbolic variables
d = sp.simplify(sp.cos(omegaDq*t)*alpha + sp.sin(omegaDq*t)*beta)
q = sp.simplify(-sp.sin(omegaDq*t)*alpha + sp.cos(omegaDq*t)*beta)

print(f'd component = {d}')
print(f'q component = {q}')
