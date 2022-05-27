from tkinter import *
from tkinter import messagebox

class Tela:
    def __init__(self):
        self.janela = Tk()

        self.frameCima = Frame(self.janela)
        self.frameCima.pack()

        self.frameBaixo = Frame(self.janela)
        self.frameBaixo.pack()

        self.checkvar1 = IntVar()
        self.checkvar2 = IntVar()
        self.checkvar3 = IntVar()
        self.checkvar4 = IntVar()


        self.checkvar1.set(0)
        self.checkvar2.set(0)
        self.checkvar3.set(0)
        self.checkvar4.set(0)

        self.label = Label(self.frameCima, text='Quais gêneros literários você gosta?')
        self.label.pack(anchor='w')

        self.check1 = Checkbutton(self.frameCima, text='Sci-fi', variable=self.checkvar1)
        self.check2 = Checkbutton(self.frameCima, text='Terror', variable=self.checkvar2)
        self.check3 = Checkbutton(self.frameCima, text='Aventura', variable=self.checkvar3)
        self.check4 = Checkbutton(self.frameCima, text='Suspense', variable=self.checkvar4)
        self.check1.pack(anchor='w')
        self.check2.pack(anchor='w')
        self.check3.pack(anchor='w')
        self.check4.pack(anchor='w')

        self.botao = Button(self.frameBaixo, text='Exibir escolha', command=self.exibe)
        self.botao.pack()

        mainloop()

    def exibe(self):
        self.texto = 'Você curte: \n'
        if self.checkvar1.get() == 1:
            self.texto += 'Sci-fi\n'
        if self.checkvar2.get() == 1:
            self.texto += 'Terror\n'
        if self.checkvar3.get() == 1:
            self.texto += 'Aventura\n'
        if self.checkvar4.get() == 1:
            self.texto += 'Suspense\n'
        messagebox.showinfo('Seu gosto literário: ', self.texto)

minhaTela = Tela()