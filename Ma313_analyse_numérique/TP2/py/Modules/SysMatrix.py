from numpy import array, ndarray, transpose

class SysMatrix:
    def __init__(self, size: int) -> None:
        self.size: int = size
        self.A: ndarray = self.create_A()
        self.b: ndarray = self.create_b()

    def create_A(self) -> ndarray:
        return array([
            [
                self.coefficient_A(i, j) for j in self.getrange()
            ]
            for i in self.getrange()
        ])
    
    def create_b(self) -> ndarray:
        return transpose(array([
            [
                self.coefficient_b(i) for i in self.getrange()
            ]   
        ]))
    
    def getrange(self) -> range:
        return range(1, self.size + 1)

    def coefficient_A(self, i: int, j: int) -> float:
        return
    
    def coefficient_b(self, i: int):
        return i / 100

class SysOneMatrix(SysMatrix):    
    def coefficient_A(self, i: int, j: int) -> float:
        return 1 / (5 + 2*i + 3*j) if i != j else 1
    
class SysTwoMatrix():
    def coefficient_A(self, i: int, j: int) -> float:
        return 1 / (5 + 4*abs(i - j))
    
class SysThreeMatrix(SysMatrix):    
    def coefficient_A(self, i: int, j: int) -> float:
        return 7 if i == j else -2 if i == j - 1 else -4 if i == j + 1  else 0