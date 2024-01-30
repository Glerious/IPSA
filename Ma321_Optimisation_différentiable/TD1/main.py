from matplotlib.pyplot import *
from numpy import linspace
from math import exp


intervale = list(linspace(-5, 5, 1000))

f1 = lambda x : abs(x)
f2 = lambda x : exp(x)
f3 = lambda x : 2*x**2 + x + 1
f4 = lambda x : 4*x + 1

iterate = [f1, f2, f3, f4]
for i in range(len(iterate)):
    subplot(len(iterate), 1, 1 + i)
    plot([iterate[i](x) for x in intervale])
show()