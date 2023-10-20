from random import choice

# Caractères

lettre = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chiffre = "1234567890"

# Action

sideline = "sideline"
development = "development"
empty = "empty"
entry = "entry"


def BetterText(cmd):
    if cmd == sideline:
        return ">---------------------<"
    elif cmd == development:
        return "( En Développement ... )"
    elif cmd == entry:
        return " Indiquez une saisie : "
    elif cmd == empty:
        return "Element vide"


def Codeelement():
    mdp = ""
    caractere = lettre + lettre.lower() + chiffre
    for _ in range(8):
        mdp += choice(caractere)
    return mdp
