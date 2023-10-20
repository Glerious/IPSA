from tkinter import *

class BetterTkinter():
    def __init__(self):
        self.main = object()
        self.compaund = {}

    def get(self):
        return self.main

    def add(self, object: object, name: str = ""):
        if name == "":
            id: int = 0
            while "element" + str(id) in self.compaund.keys():
                id += 1
            name = "element" + str(id)
        self.compaund[name] = object

    def to(self, name: str):
        compaund = self.compaund[name]
        if isinstance(compaund, BetterTkinter):
            return compaund

    def getcompaund(self):
        return self.compaund


class Interface(BetterTkinter):
    def __init__(self, name: str, bg: str, size: str):
        super().__init__()
        self.main = Tk()
        self.setinfo(name, bg, size)

    def setinfo(self, name: str, bg: str, size: str):
        _ = self.main
        _.title(name)
        _.configure(bg=bg)
        _.geometry(size)

    def show(self):
        self.main.mainloop()


class Volet(BetterTkinter):
    def __init__(self, interface, orient=HORIZONTAL, bg: str = "white"):
        super().__init__()
        self.main = PanedWindow(interface, orient=orient, bg=bg)
        self.main.pack(side=TOP, expand=Y, fill=BOTH)

    def addelement(self):
        for i in self.compaund:
            if isinstance(i, BetterTkinter) or isinstance(i, Text) or isinstance(i, Press):
                self.main.add(i.main)


class Box(BetterTkinter):
    def __init__(self, interface, bg: str = "white"):
        super().__init__()
        self.main = Frame(interface, bg=bg)
        self.main.pack()


class Text():
    def __init__(self, interface, text: str, bg: str = "white"):
        self.main = Label(interface, text=text, bg=bg)
        self.main.pack()


class Press():
    def __init__(self, interface, text: str, cmd, bg: str = "white"):
        self.main = Button(interface, text=text, command=cmd, bg=bg)
        self.main.pack()

class Enter():
    def __init__(self, interface, value: str = "Enter something...", bg: str = "white", width: int = 30):
        self.variable = StringVar(value=value)
        self.main = Entry(interface, textvariable=self.variable, bg=bg, width=width)
        self.main.pack()

