import numpy as np

# Transformations between the abc, alpha beta and dq frames.

def abc2ab(x):
    transform = (2/3)*np.array([[1, -0.5, -0.5], [0, np.sqrt(3)/2, -np.sqrt(3)/2]])
    return np.matmul(transform, x)

def abc2dq(x, theta):
    transform = (2/3)*np.array([[np.cos(theta), np.cos(theta-(2/3)*np.pi), np.cos(theta+(2/3)*np.pi)],
                               [-np.sin(theta), -np.sin(theta-(2/3)*np.pi), -np.sin(theta+(2/3)*np.pi)]])
    return np.matmul(transform, x)

def ab2dq(x, theta):
    transform = np.array([[np.cos(theta), np.sin(theta)], [-np.sin(theta), np.cos(theta)]])
    return np.matmul(transform, x)

def ab2abc(x):
    transform = np.array([[1, 0], [-0.5, np.sqrt(3)/2], [-0.5, -np.sqrt(3)/2]])
    return np.matmul(transform, x)

def dq2abc(x):
    transform = np.array([[np.cos(theta), -np.sin(theta)],
                          [np.cos(theta-(2/3)*np.pi), -np.sin(theta-(2/3)*np.pi)],
                          [np.cos(theta+(2/3)*np.pi), -np.sin(theta+(2/3)*np.pi)]])
    return np.matmul(transform, x)

def dq2ab(x):
    transform = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    return np.matmul(transform, x)