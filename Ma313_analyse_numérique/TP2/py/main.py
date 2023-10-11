from numpy.linalg import solve, norm
from numpy import ndarray, dot, array, transpose
from matplotlib.pyplot import semilogy, title, show

from time import sleep

from Modules.SysMatrix import SysOneMatrix, SysTwoMatrix, SysThreeMatrix
from Modules.Jacobi import Jacobi
from Modules.GaussSeidel import GaussSeidel
from Modules.Relaxation import Relaxation


limite1 = 10e-5
limite2 = 10e-10
limite_iterate = 200

def system(func):
    def wrapper():
        def loop_limite(M: ndarray, N: ndarray, b: ndarray, limite: int, x: ndarray = transpose(array([[0, 0, 0]]))):
            loop : int = 1
            new_x = solve(M, dot(N, x) - b)
            while norm(new_x - x) > limite and loop < limite_iterate:
                x = new_x
                new_x = solve(M, dot(N, x) - b)
                loop += 1
            return loop
        
        def graph_relax(A : ndarray):
            scan = range(1, 199)

            x = [i for i in scan]
            y = [Relaxation(A, i/100).spectral_ray() for i in scan]

            semilogy(x, y)
            title("Rayon Spectral de la méthode de relaxation en fonctions de w")
            show()

        jacobi = Jacobi(func()[0])
        jacobi_limite1 = loop_limite(M=jacobi.M, N=jacobi.N, b = func()[1], limite=limite1)
        jacobi_limite2 = loop_limite(M=jacobi.M, N=jacobi.N, b = func()[1], limite=limite2)
        print(f"Méthode Jaconienne :\n > 10e-5 : {jacobi_limite1} itération. \n > 10e-10 : {jacobi_limite2} iterations.")

        gaussseidel = GaussSeidel(func()[0])
        gaussseidel_limite1 = loop_limite(M=gaussseidel.M, N=gaussseidel.N, b = func()[1], limite=limite1)
        gaussseidel_limite2 = loop_limite(M=gaussseidel.M, N=gaussseidel.N, b = func()[1], limite=limite2)
        print(f"Méthode Gaussiènne :\n > 10e-5 : {gaussseidel_limite1} itération. \n > 10e-10 : {gaussseidel_limite2} iterations.")

        graph_relax(A = func()[0])
    return wrapper

@system
def sys_one():
    matrix_size = 3

    sys_one = SysOneMatrix(matrix_size)
    return sys_one.A, sys_one.b

@system
def sys_two():
    matrix_size = 200

    sys_two = SysTwoMatrix(matrix_size)
    return sys_two.A, sys_two.b

@system
def sys_three():
    matrix_size = 200

    sys_three = SysThreeMatrix(matrix_size)
    return sys_three.A, sys_three.b


if __name__.__eq__("__main__"):
    sys_one()
    # sys_two()
    # sys_three()
    # print(test())