from addons.BetterTkinter import *
from addons.BetterText import *

fenetre = Interface("fenetre", "yellow", "300x300")
fenetre.add(Volet(fenetre.get(), bg="blue"), "volet01h")

volet01h: Volet = fenetre.to("volet01h")

volet01h.add(Text(volet01h.get(), "Je ne sais pas", bg="yellow"))
volet01h.add(Text(volet01h.get(), "En vrai oui", bg="red"))
volet01h.add(Enter(volet01h.get(), "Entre de la merde..."))

if __name__ == "__main__":
    volet01h.addelement()
    fenetre.show()