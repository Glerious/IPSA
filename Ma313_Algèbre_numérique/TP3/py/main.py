from numpy import loadtxt, ones, c_
from numpy import ndarray
from numpy.linalg import solve, qr, norm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


point = loadtxt("Ma313_Algèbre_numérique/TP3/py/ressources/TP3_partie2_points.dat")


# 1 . Régression linéaire multiple

data1 = loadtxt("Ma313_Algèbre_numérique/TP3/py/ressources/TP3_partie1_donnees1.dat")
data2 = loadtxt("Ma313_Algèbre_numérique/TP3/py/ressources/TP3_partie1_donnees2.dat")

def splitMatrix(matrix: ndarray):
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
# graph 3D

def methodQR(A: ndarray, b: ndarray):
    Q, R = qr(A) # avec Q (n, p) et R (p, p) matrice carrée
    x = solve(R, Q.T@b)
    erreur = norm(A@x -  b)
    return x, erreur

# 1 . 3 . Résolution
def resolve(matrix: ndarray):
    A, b = splitMatrix(matrix=matrix)
    x1, erreur1 = methodNormal(A, b)
    x2, erreur2 = methodQR(A, b)
    return (x1, erreur1), (x2, erreur2)

# 1 . 3 . 1 Premier Jeu

resolve(data1)

# 1 . 3 . 2 Deuxième Jeu
resolve(data2)

# 1 . 4 Graphique 3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data1[:, 0], data1[:, 1], data1[:, 2], zdir='z', c= 'red')
ax.scatter(data2[:, 0], data2[:, 1], data2[:, 2], zdir='z', c= 'blue')
# plt.show()

