from numpy import ndarray, diag, dot, array, transpose
from numpy.linalg import inv, eigvals, solve

class Jacobi():
    def __init__(self, A: ndarray) -> None:
        self.A : ndarray = A
        self.M : ndarray = self.initM()
        self.N : ndarray = self.initN()
        self.J : ndarray = self.initJ()

    def initM(self):
        return diag(diag(self.A))
    
    def initN(self):
        return self.M - self.A
    
    def initJ(self):
        return dot(inv(self.M), self.N)
    
    def own_value(self):
        return abs(eigvals(self.J))


    