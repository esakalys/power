import numpy as np

# Functions to convert between polar and rectangular vector representations

def pol2rec(polar, deg=True):
    if deg:
        angleRad = polar[1]*(np.pi/180)
        rec = np.complex(polar[0]*np.cos(angleRad), (polar[0]*np.sin(angleRad)))
    else:
        rec = np.complex(polar[0]*np.cos(polar[1]), (polar[0]*np.sin(polar[1])))
    return rec


def rec2pol(rec, deg=True):
    polar = np.array([0, 0], dtype='float')
    polar[0] = np.sqrt(rec.real**2 + rec.imag**2)
    polar[1] = np.arctan(rec.imag/rec.real)
    if deg:
        polar[1] = polar[1]*(180/np.pi)
    return polar
