from numpy import loadtxt, ones, c_
from numpy import ndarray

from numpy.linalg import solve, qr, norm


point = loadtxt("Ma313_Algèbre_numérique/TP3/py/ressources/TP3_partie2_points.dat")


# 1 . Régression linéaire multiple

data1 = loadtxt("Ma313_Algèbre_numérique/TP3/py/ressources/TP3_partie1_donnees1.dat")
data2 = loadtxt("Ma313_Algèbre_numérique/TP3/py/ressources/TP3_partie1_donnees2.dat")

def splitMatrix(matrix: ndarray):
    return  c_[ones(matrix.shape[0]),matrix[:, :2]] , matrix[:, 2:]

A, b = splitMatrix(data1)

# 1 . 1 Resolution par la méthode des équation normale

def normalEquation(A: ndarray, b:  ndarray):
    return A.T@A, A.T@b

A_, b_ = normalEquation(A, b)
x_1 = solve(A_, b_)
erreur1 = norm(A@x_1 + b)

# 1 . 2 Resolution par la méthode QR

Q, R = qr(A)
x_2 = solve(R, Q.T@b)