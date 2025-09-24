import numpy as np
import matplotlib.pyplot as plt

f = 1 * 10 ** 6
lmbd = 3 * 10 ** 8
l = 0.01 * lmbd / 2
k = 2 * np.pi / lmbd

theta = np.linspace(1e-9, np.pi-(1e-9), 2000)

def E(theta): #Т.к. у нас нормированно всё, то часть уравнения просто сокращается
    num = np.cos(k * l * np.cos(theta)) - np.cos(k * l)
    den = np.sin(theta)
    return num/den

def F(theta):
    return abs(E(theta)) / abs(E(theta).max())

def Dmax(theta):
    formula = 4 * np.pi / (F(theta)**2 * np.sin(theta))
    return np.trapezoid(formula, theta)

