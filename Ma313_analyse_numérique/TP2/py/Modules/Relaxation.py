from numpy import ndarray, diag, tril

from .MethodeModel import MethodeModel

class Relaxation(MethodeModel):
    def __init__(self, A : ndarray, w : int) -> None:
        self.w : int = w
        super().__init__(A)

    def initM(self):
        return ((1 - self.w)/self.w)*diag(diag(self.A)) + tril(self.A)
    
    def spectral_ray(self):
        return abs(max(self.own_value()))