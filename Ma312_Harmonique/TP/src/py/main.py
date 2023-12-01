from numpy import ndarray, fft, ones, array, abs, angle
# from numpy.fft import fft
from matplotlib.pyplot import subplot, plot, show
from soundfile import *
from scipy import *

from math import cos, pi

# 1 Quelques expérimentations
def fourrierTransform(func: ndarray):
    x = fft.fft(func)
    iterate = [func, abs(x), angle(x)]
    for i in range(len(iterate)):
        subplot(len(iterate), 1, i + 1)
        plot(iterate[i])
    show()

N = 128

# 1 . 1
# fourrierTransform(ones(N))

# 1 . 2
x2: ndarray = array([1 if k == 0 else 0 for k in range(N)])
# fourrierTransform(x2)

# 1 . 3
x3: ndarray = array([0 if k == 1 else 0 for k in range(N)])
# fourrierTransform(x3)

# 1 . 4
x4: ndarray = array([cos(20 * k * pi / N) for k in range(N)])
# fourrierTransform(x4)

# 1 . 5
x5: ndarray = array([1 if k < N / 2 else 0 for k in range(N)])
# fourrierTransform(x5)




