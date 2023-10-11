from numpy import tril

from .MethodeModel import MethodeModel

class GaussSeidel(MethodeModel):
    def initM(self):
        return tril(self.A)