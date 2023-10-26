from addons.BetterTkinter import *
from addons.BetterText import *
from functions import Functions

given : dict = {2: 4, 4: 11, 8: 15, 10: 20, 24: 39, 40: 62, 52: 85}
# Question 1
new = Functions(given=given)

def exercice1():
    # Question 2
    # Question 3
    # Question 5
    # Question 6
    new.graph()
    # Question 4
    print(f"Coefficient de correlation linéarie : {new.r}")
    # Question 7
    print(f"Valeurs ajustée de y : {new.adjusty()}")
    print(f"Valeur des distances à la droite d'ajustement : {new.distancey()}")
    # Question 8
    print(f"Variable résiduelle : {new.residual_var()}")
    print(f"Variable expliquée : {new.explained_var()}")
    # Question 9
    print(f"Respectivement pour x = 9 et x = 30 : {new.func(9)} et {new.func(30)}")

if __name__.__eq__("__main__"):
    exercice1()