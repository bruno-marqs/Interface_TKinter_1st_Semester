from tkinter import *

class Tela:
    def __init__(self):
        self.janela = Tk()

        self.fontePadrao = ("Arial", "10")

        self.container1 = Frame(self.janela, pady=10)
        self.container1.pack()

        self.container2 = Frame(self.janela, padx=20)
        self.container2.pack()

        self.container3 = Frame(self.janela, padx=20)
        self.container3.pack()

        self.container4 = Frame(self.janela, pady=10)
        self.container4.pack()

        self.container5 = Frame(self.janela, pady=20)
        self.container5.pack()

        self.titulo = Label(self.container1,
                            text="Clique no [+] e some",
                            font=("Arial", "10", "bold"))
        self.titulo.pack()

        self.nome = Label(self.container2,
                          text="Insira aqui primeiro número:",
                          font=self.fontePadrao)
        self.nome.pack(side=LEFT)

        self.caixaEntrada1 = Entry(self.container2,
                               width=10,
                               font=self.fontePadrao)
        self.caixaEntrada1.pack(side=LEFT)

        self.somar = Label(self.container3,
                                 text="[ + ]",
                                 width=5,
                                 relief=RAISED,
                                 font=("Calibri", "8"))
        self.somar.bind("<Button-1>", self.somarEvento)
        self.somar.pack()

        self.nome = Label(self.container4,
                          text="Insira aqui segundo número:",
                          font=self.fontePadrao)
        self.nome.pack(side=LEFT)

        self.caixaEntrada2 = Entry(self.container4,
                                  width=10,
                                  font=self.fontePadrao)
        self.caixaEntrada2.pack(side=LEFT)

        self.msg = Label(self.container5,
                         text="", font=self.fontePadrao)
        self.msg.pack()

        mainloop()

    def somarEvento(self, event):
        evento = int(self.caixaEntrada1.get()) + int(self.caixaEntrada2.get())
        result = f'O resultado é {evento}'
        self.msg['text'] = result
        print(result)

minhatela = Tela()
