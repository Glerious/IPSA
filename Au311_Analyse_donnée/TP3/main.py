from numpy import random, linspace
from matplotlib.pyplot import show, hist, legend, plot
from scipy.stats import poisson, norm, t

# Exercice 1

# 2
# loi1 = {21:0, 18:1, 7:2, 3:3, 1:4}

def esperance(loi: dict, size : int):
    return sum([i*j for i,j in loi.items()]) / size

def variance(loi: dict, size : int):
    loiCarree = dict((i, j**2) for i, j in loi.items())
    return esperance(loiCarree, size) - esperance(loi, size)

# print("Espérance : " , esperance(loi1, 50))
# print("Variance : " , variance(loi1, 50))

# 3 . 1

def poissonPmf(esperance : int, elements : list | range) -> list:
    return [poisson.pmf(i, esperance) for i in elements]

# print("Pour 0 à 4 accidents : " , poissonPmf(
#       esperance(loi1, 50),
#       range(0, 5)
# ))

# 3 . 2

# print(poisson.cdf(
#     3, esperance(loi1, 50)
# ))

# 4

# scatter([0, 1, 2, 3, 4], poissonPmf(esperance(loi1, 50), range(0, 5)))
# title("Probabilité du nombre d'apparition d'un accident")
# show()

# Exercice 2

# print("Pourcentage de confiture NON pur sucre : ", round(2 - norm.cdf(520, 465, 30) - norm.cdf(420, 465, 30), 4) * 100, "%")

# Exercice 3


X = linspace(-3, 3)



Y = random.standard_t(10, 10000)
hist(Y, bins=X, density=True, label="Expérience Lois de Student", color="Cyan")
Y = t.pdf(X, df=10)
plot(X, Y, color="Red", label="Densité loi Student")
Y = norm.pdf(X, 0, 1)
plot(X, Y, color="Green", label="Loi Normale")
legend()
show()












      
      









