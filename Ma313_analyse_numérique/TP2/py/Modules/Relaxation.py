from numpy import ndarray, diag, dot, tril
from numpy.linalg import inv, eigvals

class Relaxation():
    def __init__(self, A : ndarray, w : int) -> None:
        self.w : int = w
        self.A : ndarray = A
        self.M : ndarray = self.initM()
        self.N : ndarray = self.initN()
        self.R : ndarray = self.initR()

    def initM(self):
        return ((1 - self.w)/self.w)*diag(diag(self.A)) + tril(self.A)
    
    def initN(self):
        return self.M - self.A
    
    def initR(self):
        return dot(inv(self.M), self.N)
    
    def own_value(self):
        return abs(eigvals(self.R))
    
    def spectral_ray(self):
        return abs(max(self.own_value()))