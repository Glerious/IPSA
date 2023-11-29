from numpy import loadtxt, ones, c_
from numpy import ndarray, array
from numpy.linalg import solve, qr, norm
from matplotlib.pyplot import figure, scatter, show, plot, legend
from mpl_toolkits.mplot3d import Axes3D
from math import pi, sin
from time import perf_counter

# 0 Fonctions de résolution de la méthode Normale et de la méthode QR

def normalEquation(A: ndarray, b:  ndarray):
    return A.T@A, A.T@b

def methodNormal(A: ndarray, b: ndarray):
    start = perf_counter()
    A_, b_ = normalEquation(A, b)
    x = solve(A_, b_)
    end = perf_counter()
    erreur = norm(A@x - b)
    return x, erreur, end - start

def methodQR(A: ndarray, b: ndarray):
    start = perf_counter()
    Q, R = qr(A) # avec Q (n, p) et R (p, p) matrice carrée
    x = solve(R, Q.T@b)
    end = perf_counter()
    erreur = norm(A@x -  b)
    return x, erreur, end - start

def resolve(A: ndarray, b: ndarray):
    x1, erreur1, time1 = methodNormal(A, b)
    x2, erreur2, time2 = methodQR(A, b)
    return (x1, erreur1, time1), (x2, erreur2, time2)

# Méthode QR plus longue (note rendu)


# 1 . Régression linéaire multiple
data1 = loadtxt("Ma313_Algèbre_numérique/TP3/py/ressources/TP3_partie1_donnees1.dat")
data2 = loadtxt("Ma313_Algèbre_numérique/TP3/py/ressources/TP3_partie1_donnees2.dat")

def splitMatrix(data: ndarray):
    return  c_[ones(data.shape[0]),data[:, :data.shape[1] - 1]] , data[:, data.shape[1] - 1:]

# 1 . 3 . Résolution
def resolve1(data: ndarray):
    A, b = splitMatrix(data)
    return resolve(A, b)

# 1 . 3 . 1 Premier Jeu
resolve1(data1)

# 1 . 3 . 2 Deuxième Jeu
resolve1(data2)

# 1 . 4 Graphique 3D
"""
fig = figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data1[:, 0], data1[:, 1], data1[:, 2], zdir='z', c= 'red')
ax.scatter(data2[:, 0], data2[:, 1], data2[:, 2], zdir='z', c= 'blue')
show()
"""

# 2 Détermination d’un cercle
point = loadtxt("Ma313_Algèbre_numérique/TP3/py/ressources/TP3_partie2_points.dat")

def cercleMatrix(data: ndarray):
    return c_[2*data, ones(data.shape[0])], data[:, 0]**2 + data[:, 1]**2

# 2 . 3 Resolution
def resolve2(data: ndarray):
    A, b = cercleMatrix(data)
    return resolve(A, b)

resolve2(point)

# 2 . 4 Graphique 3D

"""
fig = figure()
scatter(point[:, 0], point[:, 1], c= 'red')
show()
"""

# 3 Approximation d’une fonction usuelle
x = array([i/100 for i in range(round(pi/2*1000))])

def sinusMatrix(data: ndarray) -> ndarray:
    return c_[data**9, data**8, data**7, data**6, data**5, data**4, data**3, data**2, data, data**0], [sin(i) for i in data]

def resolve3(data: ndarray):
    A, b = sinusMatrix(data)
    return resolve(A, b)

resolve3(x)

"""
y1 = sinusMatrix(x)[0]@resolve3(x)[0][0]
y2 = sinusMatrix(x)[0]@resolve3(x)[1][0]
plot(x, y1, label="Polynôme normal")
plot(x, y2, label="Polynôme QR")
plot(x, [sin(i) for i in x], label="Fonction sinus")
legend()
show()
"""

# 0 Solution
# print(f"DATA1 :\nSolutions Equation normale :  \n{resolve1(data1)[0][0]}, \nSolutions QR : \n{resolve1(data1)[1][0]}")
# print(f"DATA2 :\nSolutions Equation normale : \n{resolve1(data2)[0][0]}, \nSolutions QR : \n{resolve1(data2)[1][0]}")
# print(f"POINT :\nSolutions Equation normale : \n{resolve2(point)[0][0]}, \nSolutions QR : \n{resolve2(point)[1][0]}")
print(f"SINUS :\nSolutions Equation normale : \n{resolve3(x)[0][0]}, \nSolutions QR : \n{resolve3(x)[1][0]}")

# 0 Erreur
# print(f"DATA1 :\nErreurs Equation normale : {resolve1(data1)[0][1]}, Erreurs QR : {resolve1(data1)[1][1]}")
# print(f"DATA2 :\nErreurs Equation normale : {resolve1(data2)[0][1]}, Erreurs QR : {resolve1(data2)[1][1]}")
# print(f"POINT :\nErreurs Equation normale : {resolve2(point)[0][1]}, Erreurs QR : {resolve2(point)[1][1]}")
# print(f"SINUS :\nErreurs Equation normale : {resolve3(x)[0][1]}, Erreurs QR : {resolve3(x)[1][1]}")

# 0 Temps
# print(f"DATA1 :\nTemps Equation normale : {resolve1(data1)[0][2]}, Temps QR : {resolve1(data1)[1][2]}")
# print(f"DATA2 :\nTemps Equation normale : {resolve1(data2)[0][2]}, Temps QR : {resolve1(data2)[1][2]}")
# print(f"POINT :\nTemps Equation normale : {resolve2(point)[0][2]}, Temps QR : {resolve2(point)[1][2]}")
# print(f"SINUS :\nTemps Equation normale : {resolve3(x)[0][2]}, Temps QR : {resolve3(x)[1][2]}")
