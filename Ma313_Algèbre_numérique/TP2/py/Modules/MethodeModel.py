from numpy import ndarray, dot, diag, tril
from numpy.linalg import inv, eigvals

class MethodeModel:
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
    
    def spectral_ray(self):
        return abs(max(self.own_value()))
    
class Jacobi(MethodeModel):
    def initM(self):
        return diag(diag(self.A))
    
class GaussSeidel(MethodeModel):
    def initM(self):
        return tril(self.A)
    
class Relaxation(MethodeModel):
    def __init__(self, A : ndarray, w : int) -> None:
        self.w : int = w
        super().__init__(A)

    def initM(self):
        return ((1 - self.w)/self.w)*diag(diag(self.A)) + tril(self.A)