from math import sqrt
from matplotlib.pyplot import show, scatter, title, legend, plot

class Functions:
    def __init__(self, given : dict) -> None:
        self.givenx : tuple = tuple(given.keys())
        self.giveny : tuple = tuple(given.values())
        if not len(self.givenx).__eq__(len(self.giveny)):
            raise ValueError("legnth of list x and list y are different. Check duplicate number !")
        self.x_ : float = self.init_(self.givenx)
        self.y_ : float = self.init_(self.giveny)
        self.covxx : float = self.initcov(self.givenx)
        self.covyy : float = self.initcov(self.giveny)
        self.covxy : float = self.initcov(self.givenx, self.giveny)
        self.r : float = self.covxy / sqrt(self.covxx*self.covyy)
        self.a : float = self.covxy/self.covxx
        self.b : float = self.y_ - self.a * self.x_

    def init_(self, listof: tuple) -> float:
        return 1/len(listof) * sum(listof)
    
    def initcov(self, lista : tuple, listb : tuple = None):
        if listb is None:
            return (1/len(lista) * sum(i**2 for i in lista)) - self.init_(lista)**2
        return (1/len(lista) * sum(i*j for i, j in zip(lista, listb)))  - self.init_(lista)*self.init_(listb)
    
    def printfunc(self) -> str:
        return f"{round(self.a, 2)}x + {round(self.b, 2)}"

    def func(self, x : float):
        return self.a * x + self.b

    def antifunc(self, y : float):
        return (y - self.b) / self.a
    
    def graph(self):
        """ Affiche le graphique de la méthode de régrassion linéaire
        - Affiche le graphiques de point
        - Affiche le point G
        - Affiche la courbe de régréssion linaire ainsi que son équation    
        """
        size = (150)
        scatter(self.x_, self.y_, s=size, c="coral", label="Point G")

        x = self.givenx
        y = self.giveny
        scatter(x, y)

        x = [0, max(self.givenx)]
        y = [self.func(i) for i in x]
        plot(x, y, label=self.printfunc())
        
        legend()
        title("Rayon Spectral de la méthode de relaxation en fonctions de w")
        show()

    def adjusty(self):
        return [self.func(i) for i in self.givenx]
    
    def distancey(self):
        return [abs(i - j) for i, j in zip(self.adjusty(), self.giveny)]
    
    def residual_var(self):
        return self.covyy * self.r**2
    
    def explained_var(self):
        return self.covyy * (1 - self.r**2)