from addons.BetterTkinter import *
from addons.BetterText import *

if __name__.__eq__("__main__"):
    interface = Interface("AU311 - Calculator", "green", "900x300")

    interface.add(Volet(interface.get()), "window1", )
    interface.show()