from numpy import loadtxt, ones, c_
from numpy import ndarray

from numpy.linalg import solve, qr, norm


point = loadtxt("Ma313_Algèbre_numérique/TP3/py/ressources/TP3_partie2_points.dat")


# 1 . Régression linéaire multiple

data1 = loadtxt("Ma313_Algèbre_numérique/TP3/py/ressources/TP3_partie1_donnees1.dat")
data2 = loadtxt("Ma313_Algèbre_numérique/TP3/py/ressources/TP3_partie1_donnees2.dat")

def splitMatrix(matrix: ndarray):
    """
    Parameters
    -------
    matrix : Matrice de taille (n, p)

    Return
    -------
    A_ : Matrice de taille (n, p) avec une première colomne de 1. Cette matrice reprend le paramètre matrix en laissant la dernière colomne.
    b_ : Matrice de taille (n, 1) qui reprend le paramètre matrix en prenant la dernière colomne.
    """
    return  c_[ones(matrix.shape[0]),matrix[:, :matrix.shape[1] - 1]] , matrix[:, matrix.shape[1] - 1:]


# 1 . 1 . Resolution par la méthode des équation normale

def normalEquation(A: ndarray, b:  ndarray):
    return A.T@A, A.T@b

def methodNormal(A: ndarray, b: ndarray):
    A_, b_ = normalEquation(A, b)
    x = solve(A_, b_)
    erreur = norm(A@x - b)
    return x, erreur


# 1 . 2 . Resolution par la méthode QR

# Méthode QR plus longue (note rendu)

def methodQR(A: ndarray, b: ndarray):
    Q, R = qr(A) # avec Q (n, p) et R (p, p) matrice carrée
    x = solve(R, Q.T@b)
    erreur = norm(A@x -  b)
    return x, erreur

# 1 . 2 . Résolution

A1, b1 = splitMatrix(data1)
x11, erreur11 = methodNormal(A1, b1)
x12, erreur12 = methodQR(A1, b1)


A2, b2 = splitMatrix(data2)
x21, erreur21 = methodNormal(A2, b2)
x22, erreur22 = methodQR(A2, b2)