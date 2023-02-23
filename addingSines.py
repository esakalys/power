import numpy as np

# Function that combines two out-of-phase sines of the same frequency into one and returns its' magnitude and phase

def addSines(a1, angle1, a2, angle2):

    angleDelta = np.deg2rad(angle2 - angle1)
    angle = np.arctan(a2*np.sin(angleDelta)/(a1+a2*np.cos(angleDelta)))
    a = a2*np.sin(angleDelta)/np.sin(angle)

    return a, np.rad2deg(angle)+angle1
