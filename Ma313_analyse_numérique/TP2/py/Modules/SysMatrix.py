from numpy import array, ndarray, transpose

class SysOneMatrix:
    def __init__(self, size: int) -> None:
        self.size: int = size
        self.A: ndarray = self.create_A()
        self.b: ndarray = self.create_b()

    def create_A(self) -> ndarray:
        return array([
            [
                self.coefficient_A(i, j) if i != j else 1 for j in self.getrange()
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
        return 1 / (5 + 2*i + 3*j)
    
    def coefficient_b(self, i: int):
        return i / 100
    
class SysTwoMatrix():
    def __init__(self, size : int) -> None:
        self.size = size
        self.A = self.create_A()
        self.b = self.create_b()

    def create_A(self):
        return array([
            [
                self.coefficient_A(i, j) for j in self.getrange()
            ]
            for i in self.getrange()
        ])

    def create_b(self):
        return transpose(array([
            [
                self.coefficient_b(i) for i in self.getrange()
            ]
            
        ]))
    
    def getrange(self) -> range:
        return range(1, self.size + 1)
    
    def coefficient_A(self, i: int, j: int) -> float:
        return 1 / (5 + 4*abs(i - j))
    
    def coefficient_b(self, i: int):
        return i / 100
    
class SysThreeMatrix:
    def __init__(self, size : int) -> None:
        self.size = size
        self.A = self.create_A()
        self.b = self.create_b()

    def create_A(self):
        return array([
            [
                7 if i == j else -2 if i == j - 1 else -4 if i == j + 1  else 0 for j in self.getrange()
            ]
            for i in self.getrange()
        ])

    def create_b(self):
        return transpose(array([
            [
                self.coefficient_b(i) for i in self.getrange()
            ]
            
        ]))
    
    def getrange(self) -> range:
        return range(1, self.size + 1)
    
    def coefficient_b(self, i: int):
        return i / 100