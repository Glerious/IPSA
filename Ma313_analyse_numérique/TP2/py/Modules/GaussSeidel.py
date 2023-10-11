from numpy import ndarray, tril, dot
from numpy.linalg import inv, eigvals

class GaussSeidel():
    def __init__(self, A : ndarray) -> None:
        self.A : ndarray = A
        self.M : ndarray = self.initM()
        self.N : ndarray = self.initN()
        self.G : ndarray = self.initG()

    def initM(self):
        return tril(self.A)
    
    def initN(self):
        return self.M - self.A
    
    def initG(self):
        return dot(inv(self.M), self.N)
    
    def own_value(self):
        return abs(eigvals(self.J))
    
    