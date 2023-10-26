from addons.BetterTkinter import *
from addons.BetterText import *
from functions import Functions

given : dict = {2: 4, 4: 11, 8: 15, 10: 20, 24: 39, 40: 62, 52: 85}
# Question 1
new = Functions(given=given)


if __name__.__eq__("__main__"):
    # Question 2
    new.graph()
    # Question 3
    new.graph(True)
    # Question 4
    print(f"Coefficient de correlation linéarie : {new.r}")
    # Question 5
    


    
