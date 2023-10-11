from numpy import ndarray, dot
from numpy.linalg import inv, eigvals

class MethodeModel():
    def __init__(self, A: ndarray) -> None:
        self.A : ndarray = A
        self.M : ndarray = self.initM()
        self.N : ndarray = self.initN()

    def initM(self):
        return
    
    def initN(self):
        return self.M - self.A
    
    def initMatrixMethod(self):
        return dot(inv(self.M), self.N)
    
    def own_value(self):
        return abs(eigvals(self.initMatrixMethod()))