from tkinter import *


class Gui():
    def __init__(self, root):
        self.__root = root
        self.__start = False
        self.renderStartButton()
        # self.renderResetButton()
        self.renderRestitutionEntry()
        self.renderVelAEntry()
        self.renderVelBEntry()
        self.renderMassAEntry()
        self.renderMassBEntry()
        self.renderResWall()
        root.mainloop()

    def onStartButton(self):
        self.__start = True
        # (vel, mass)
        self.__A = (int(self.__velAEntry.get()),
                    int(self.__massAEntry.get()))
        self.__B = (int(self.__velBEntry.get()),
                    int(self.__massBEntry.get()))
        self.__e = float(self.__restitutionEntry.get())
        self.__we = float(self.__WeEntry.get())
        self.__root.destroy()

    def renderStartButton(self):
        startButton = Button(self.__root, text="Start",
                             command=lambda: self.onStartButton())
        startButton.grid(row=0, column=1)

    def onResetButton(self):  # TODO: implement
        pass

    def renderResetButton(self):
        resetButton = Button(self.__root, text="RESET",
                             bg="red", command=lambda: self.onResetButton())
        resetButton.grid(row=2, column=0)  # TODO: change pos

    def renderRestitutionEntry(self):
        self.__restitutionEntry = Entry(self.__root)
        self.__restitutionEntry.insert(-1, "e")
        self.__restitutionEntry.grid(row=1, column=0)

    def renderVelAEntry(self):
        self.__velAEntry = Entry(self.__root)
        self.__velAEntry.insert(-1, "Va")
        self.__velAEntry.grid(row=1, column=1)

    def renderVelBEntry(self):
        self.__velBEntry = Entry(self.__root)
        self.__velBEntry.insert(-1, "Vb")
        self.__velBEntry.grid(row=1, column=2)

    def renderMassAEntry(self):
        self.__massAEntry = Entry(self.__root)
        self.__massAEntry.insert(-1, "Ma")
        self.__massAEntry.grid(row=2, column=1)

    def renderMassBEntry(self):
        self.__massBEntry = Entry(self.__root)
        self.__massBEntry.insert(-1, "Mb")
        self.__massBEntry.grid(row=2, column=2)

    def renderResWall(self):
        self.__WeEntry = Entry(self.__root)
        self.__WeEntry.insert(-1, "e with wall")
        self.__WeEntry.grid(row=2, column=0)

    def getStart(self):
        return self.__start

    def getA(self):
        return self.__A

    def getB(self):
        return self.__B

    def getRestituition(self):
        return self.__e

    def getResWall(self):
        return self.__we
