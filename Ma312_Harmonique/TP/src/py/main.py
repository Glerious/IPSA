from numpy import ndarray, ones, array, abs, angle
from numpy.fft import fft
from matplotlib.pyplot import subplot, plot, show, title
from soundfile import read
from scipy import *

from math import cos, pi, sin, exp

# 1 . Quelques expérimentations
def fourrierTransform(func: ndarray):
    x = fft.fft(func)
    iterate = [func, abs(x), angle(x)]
    for i in range(len(iterate)):
        subplot(len(iterate), 1, i + 1)
        plot(iterate[i])
    show()

N = 128

x1: ndarray = ones(N)
x2: ndarray = array([1 if k == 0 else 0 for k in range(N)])
x3: ndarray = array([0 if k == 1 else 0 for k in range(N)])
x4: ndarray = array([cos(20 * k * pi / N) for k in range(N)])
x5: ndarray = array([1 if k < N / 2 else 0 for k in range(N)])

iterate = [x1, x2, x3, x4, x5]

# for i in iterate:
#     fourrierTransform(i)

# 2 . Transformée de Fourrier discrète d'une signal échelonné
def fourrierTransform2(func: ndarray): 
    x = fft.fft(func)
    t: ndarray = array([x * deltaT for x in range(N)])
    f: ndarray = array([x / T for x in range(N)])
    iterate = [f[:int(N/2)], t[:int(N/2)]]
    ttl = ["frequenciel", "temporel"]
    for i in range(len(iterate)):
        subplot(len(iterate), 1, i + 1)
        plot(iterate[i], x[:int(N/2)])
        title(ttl[i])
    show()

N = 1024
T = 10  # Péridode
deltaT = T / N # intervalle de temps
fe = 1 / deltaT # fréquence d'échantillonnage

t = [i * deltaT for i in range(N)]

x1: ndarray = array([2 * cos(10 * pi * x) + 7 * cos(2 * pi * x) for x in t])
x2: ndarray = array([sin(2.0 * pi * x)**2 for x in t])
x3: ndarray = array([abs(sin(pi * x)) for x in t])
x4: ndarray = array([exp(-x) for x in t])
x5: ndarray = array([sin(50*x) for x in t])
x6: ndarray = array([sin(2*pi*x)*cos(100*pi*x) for x in t])
x7: ndarray = array([sin(2*pi*x) + cos(100*pi*x) for x in t])
x8: ndarray = array([sin(2046*pi*x) for x in t])
x9: ndarray = array([sin(10*pi*(10 + x)*x) for x in t])
x10: ndarray = array([exp(-(x-4)**2) for x in t])

iterate = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]

# for i in iterate:
#     fourrierTransform2(i)

# 3 Formule de Parseval
def prouveParseval(func: ndarray):
    x = fft.fft(func)
    sum1 = sum(abs(func)**2)
    sum2 = 1 / T * sum(abs(x)**2)

    return sum1, sum2, round(1 - sum1 * 100 / sum2, 5)

# for i in iterate:
#     print(prouveParseval(i))

# 4 Compression d'un fichier audio

data, fe = read(r"Ma312_Harmonique\TP\ressources\Note_03.aif")
data_ = data[: ,0]
N = len(data)

def compress(data):
    x = abs(fft.fft(data))
    plot(x[:int(N/2)])
    show()

compress(data_)