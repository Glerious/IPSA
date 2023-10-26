from math import sqrt
from matplotlib.pyplot import show, plot, title

class Functions:
    def __init__(self, given : dict) -> None:
        self.givenx : tuple = self.initx(given)
        self.giveny : tuple = self.inity(given)
        if not len(self.givenx).__eq__(len(self.giveny)):
            raise ValueError("legnth of list x and list y are different. Check duplicate number !")
        self.x_ : float = self.init_(self.givenx)
        self.y_ : float = self.init_(self.giveny)
        self.covxx : float = self.initcov(self.givenx)
        self.covyy : float = self.initcov(self.giveny)
        self.covxy : float = self.initcov(self.givenx, self.giveny)
        self.r : float = self.r()
        self.a : float = self.inita()
        self.b : float = self.initb()

    def initx(self, given : dict) -> tuple:
        return tuple(given.keys())
    
    def inity(self, given : dict) -> tuple:
        return tuple(given.values())

    def init_(self, listof: tuple) -> float:
        return 1/len(listof) * sum(listof)
    
    def initcov(self, lista : tuple, listb : tuple = None):
        if listb is None:
            return (1/len(lista) * sum(i**2 for i in lista)) - self.init_(lista)**2
        return (1/len(lista) * sum(i*j for i, j in zip(lista, listb)))  - self.init_(lista)*self.init_(listb)
    
    def r(self) -> float:
        return self.covxy / sqrt(self.covxx*self.covyy)
    
    def inita(self):
        return (self.covxy/self.covxx)
    
    def initb(self):
        return self.y_ - self.a * self.x_
    
    def printfunc(self) -> str:
        return f"{round(self.a, 2)}x + {round(self.b, 2)}"

    def func(self, x : float):
        return self.a * x + self.b

    def antifunc(self, y : float):
        return (y - self.b) / self.a
    
    def graph(self):
        x = self.initx()
        y = self.inity()

        plot(x, y)
        title("Rayon Spectral de la méthode de relaxation en fonctions de w")
        show()