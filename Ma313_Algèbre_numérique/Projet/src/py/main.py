from numpy import ndarray, array, zeros, fill_diagonal, tril, linspace, sin, cos, pi, c_
from numpy.linalg import inv, eigvals, svd, solve
from matplotlib.pyplot import figure, subplot, plot, scatter, legend, title, tight_layout, xlabel, ylabel, grid, show
from scipy.interpolate import CubicSpline

from math import exp

# 1 Approximation de fonctions par des polynômes

def funcByIntervale(func, start: float, end: float, split : int) -> list:
    rectifer = (end - start) / (split - 1)
    x = [round(start + rectifer * i, 3) for i in range(split)]
    return x, [func(i) for i in x]

def normalEquation(A: ndarray, b:  ndarray):
    return A.T@A, A.T@b

def svdAplus(A: ndarray):
    u, e, v = svd(A)
    ePlusVal = array([0 if i == 0 else 1 / i for i in e])
    ePlus = array([[ePlusVal[i] if i == j  else 0 for i in range(A.shape[0])] for j in range(A.shape[1])])
    return v.T @ ePlus @ u.T

def polynomeCoefsBySplit(method: str, n: int):
    sorted: list = []
    for k in range(d):
        x, y = funcByIntervale(func, -1, 1, n)
        A = c_[[[j**i for i in range(k + 1, -1, -1)] for j in x]]
        x_: ndarray
        if method == "Normale":
            A_, b_ = normalEquation(A, y)
            x_ = solve(A_, b_)
        elif method == "SVD":
            aPlus = svdAplus(A)
            x_ = aPlus @ y
        sorted.append(x_)
    return sorted

def estimateValuePolynome(coefs: ndarray, x: float):
    return sum([j * x for j in coefs])

def error(var1: float, var2: float):
    return abs(var1 - var2)

def main(n: int):
    xs, ys = funcByIntervale(func, 0, 1, n)
    allPoly: list = polynomeCoefsBySplit(method, n)
    errors: list = []
    for x, y in zip(xs, ys):
        e = max([error(estimateValuePolynome(i, x), y) for i in allPoly])
        errors.append(e)
    return errors, ys

d = 10 # dégrés de polynôme étudiés
allN: list = [d + 1, 50, 1000] # L'ensembles des point distincts de l'intervale
method: str = "SVD" # Editable in normalEquation and svdAplus
func = exp # Editable in exp and lambda x: 1/(1+x**2)

legends = []
for i in allN:
    scatter(main(i)[1], main(i)[0])
    xlabel("Valeurs de l'intervalle de la fonction étudiée")
    ylabel("Erreur Etudiée")
    legends.append(f"Intervale par {i}")
title(f"Erreur des coefficients de polynômes de degrés 0 à {d} par {method}")
legend(legends)

# 2 . Spline Cubique

# Création de A
N = 1000

A = zeros((N, N))
fill_diagonal(A, 4)

for i in range(N-1):
    A[i, i+1] = 1
for i in range(N):
    A[i, i-1] = 1
A[0,N-1] = 0

def JACO(A):  
    M = zeros((len(A),len(A)))
    for i in range(len(A)):
        for j in range(len(A)):
            fill_diagonal(M,A[i,j])
    N = -(A -M)
    J = inv(M)@N
    sp = eigvals(J)
    conv = max(abs(sp))
    return conv

def GS(A):
    M = tril(A)
    N = -(A-M)
    J = inv(M)@N
    sp = eigvals(J)
    conv = max(abs(sp))
    return conv

a = GS(A)
b= JACO(A)
#print(a)
#print(b)
if a >b: 
    print("la méthode de Jacobi converge plus vite")
else: 
    print("la méthode GS converge le plus vite")


#Pour les deux dernière question je ne savait quelle marche suivre et par ou comencer j'ai utiliser chat gpt cependant je détaile cache qu'une des action des ligne de code
#on réecrit les fonction du 1 
def fonction_exp(x):
    return exp(x)

def fonction_rationnelle(x):
    return 1 / (1 + x**2)

#dans cette partie on tente d'aproximer les fonctions exp et 1/... on aligne plusieur polynome de deg 3 pour les aproximer. 
x_points = linspace(-10, 10, 30) #on commence à dessiner l'absice en partant de -10 a 10 avec un pas de 10 
y_exp = fonction_exp(x_points)      #on utilise les fonction faite plus haut en ordonné
y_rationnelle = fonction_rationnelle(x_points)

# Construction des splines cubique
spline_exp = CubicSpline(x_points, y_exp) #on utilise la fonction CubicSpline pour créer le spines cubique à partir de plusieur point (définit plus haut) pour ensuite créer un graf
#cette fonction permet de relier les point de manière "lisse"
spline_rationnelle = CubicSpline(x_points, y_rationnelle)

# Évaluation des splines sur un domaine étendu pour le traçage
x_eval = linspace(-10, 10, 1000)
y_spline_exp = spline_exp(x_eval)
y_spline_rationnelle = spline_rationnelle(x_eval)



#en bas le dimensionnement et l'affichage des graf
figure(figsize=(10, 6))

# Tracé de la fonction exp(x)
subplot(2, 1, 1)
plot(x_eval, fonction_exp(x_eval), label='exp(x)')
scatter(x_points, y_exp, color='red', label='Points d\'Interpolation exp(x)')
plot(x_eval, y_spline_exp, linestyle='--', label='Spline Cubique exp(x)')
legend()
title('Interpolation par Spline Cubique - exp(x)')

# Tracé de la fonction 1 / (1 + x^2)
subplot(2, 1, 2)
plot(x_eval, fonction_rationnelle(x_eval), label='1 / (1 + x^2)')
scatter(x_points, y_rationnelle, color='blue', label='Points d\'Interpolation 1 / (1 + x^2)')
plot(x_eval, y_spline_rationnelle, linestyle='--', label='Spline Cubique 1 / (1 + x^2)')
legend()
title('Interpolation par Spline Cubique - 1 / (1 + x^2)')

tight_layout()
#show()


# Définir la fonction à interpoler
def fonction_exemple_1(x):    
    return sin(x) + 0.5 * x 
def fonction_exemple_2(x):
    return cos(x) + 0.5 * x 

#comme dans la question précédante 
x_points_1 = linspace(-2*pi, 2*pi, 10)
y_points_1 = fonction_exemple_1(x_points_1)

x_points_2 = linspace(-2*pi, 2*pi, 10)
y_points_2 = fonction_exemple_2(x_points_2)

# Construire la spline cubique avec ϕ′′(a) = 0 et ϕ′′(b) = 0
spline_naturelle_1 = CubicSpline(x_points_1, y_points_1, bc_type=((2, 0), (2, 0)))
spline_naturelle_2 = CubicSpline(x_points_2, y_points_2, bc_type=((2, 0), (2, 0)))

# Évaluation de la spline sur un domaine étendu pour le traçage
x_eval_1 = linspace(-2*pi, 2*pi, 1000)
y_spline_naturelle_1 = spline_naturelle_1(x_eval_1)


x_eval_2 = linspace(-2*pi, 2*pi, 1000)
y_spline_naturelle_2 = spline_naturelle_2(x_eval_2)

# Affichage des résultats
figure(figsize=(10, 6))

# Tracé de la fonction réelle et de la spline naturelle
subplot(2,1,2)
plot(x_eval_1, fonction_exemple_1(x_eval_1), label='Fonction sin Réelle')
scatter(x_points_1, y_points_1, color='red', label='Points d\'Interpolation')
plot(x_eval_1, y_spline_naturelle_1, linestyle='--', label='Spline sin Naturelle')
legend()
title('Interpolation par Spline Naturelle')
xlabel('x')
ylabel('y')
grid(True)

subplot(2,1,2)
plot(x_eval_2, fonction_exemple_2(x_eval_2), label='Fonction cos Réelle')
scatter(x_points_2, y_points_2, color='red', label='Points d\'Interpolation')
plot(x_eval_2, y_spline_naturelle_2, linestyle='--', label='Spline cos Naturelle')
legend()
title('Interpolation par Spline Naturelle')
xlabel('x')
ylabel('y')
grid(True)


tight_layout()

show()