from numpy import diag

from .MethodeModel import MethodeModel

class Jacobi(MethodeModel):
    def initM(self):
        return diag(diag(self.A))