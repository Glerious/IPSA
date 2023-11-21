from numpy import loadtxt, ones, c_
from numpy import ndarray

from numpy.linalg import solve


point = loadtxt("Ma313_Algèbre_numérique/TP3/py/ressources/TP3_partie2_points.dat")


# Régression linéaire multiple

data1 = loadtxt("Ma313_Algèbre_numérique/TP3/py/ressources/TP3_partie1_donnees1.dat")
data2 = loadtxt("Ma313_Algèbre_numérique/TP3/py/ressources/TP3_partie1_donnees2.dat")

def splitMatrix(matrix: ndarray):
    return  c_[ones(matrix.shape[0]),matrix[:, :2]] , matrix[:, 2:]

A, b = splitMatrix(data1)

def normalEquation(A: ndarray, b:  ndarray):
    return A.T@A, A.T@b

A_, b_ = normalEquation(A, b)

print(solve(A_, b_))








