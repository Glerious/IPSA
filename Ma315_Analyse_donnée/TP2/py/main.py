import pandas as pd
from matplotlib.pyplot import scatter, show, title
from functions import Functions
from numpy import array, ndarray, ones
from numpy.linalg import solve, norm


#import de donnée
data = pd.read_csv("Au311_Analyse_donnée/TP2/ressources/alcanes.csv", sep=";", encoding="latin1" , engine='python')

# détermination des colonnes de lectures
pe = data.iloc[:,2]
na = data.iloc[:,3]
h = data.iloc[:,4]
x1 = data.iloc[:,5]

givens : list = [(h, pe), (x1, pe), (na, pe)]

def studies(given = list):
    for i in given:
        given : dict = dict(zip(i[0], i[1]))
        correlation = Functions(given=given)
        correlation.graph()
        print(correlation.r)

A : ndarray = array([list(na), list(h), list(x1), ones(len(pe))])
b : ndarray = array(list(pe))
x : ndarray = solve(A@A.T, A@b)
min_x = norm(A.T@x - b)
ratio = min_x / norm(b)

print(min_x, ratio)

