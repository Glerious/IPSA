from addons.BetterTkinter import *
from addons.BetterText import *
from functions import Functions

fenetre = Interface("fenetre", "yellow", "300x300")
fenetre.add(Volet(fenetre.get()), "volet_tableau")
fenetre.add(Volet(fenetre.get(), bg="blue"), "volet_fonction")

volet_tableau: Volet = fenetre.to("volet_tableau")
volet_tableau.add(Text(volet_tableau.get(), "Entrer les données"))
volet_fonction: Volet = fenetre.to("volet_fonction")


if __name__ == "__main__":
    # volet_tableau.addelement()
    # fenetre.show()
    given : dict = {2: 4, 4: 11, 8: 15, 10: 20, 24: 39, 40: 62, 52: 85}
    new = Functions()
