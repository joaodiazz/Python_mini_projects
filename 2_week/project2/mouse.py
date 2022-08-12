class Mouse:
    def __init__(self, modelo, cor, conectado):
        self.modelo = modelo
        self.cor = cor
        self.conectado = conectado

    def Clicar(self):
        if(self.conectado == True):
            print("Click!")
        else:
            print("Conecte o Mouse.")

    def Conectado(self):
        self.conectado = True
        return "Mouse conectado."

    def Desconectado(self):
        self.conectado = False
        return 'Mouse desconectado.'

    def Info(self):
        if(self.conectado == False):
            print(self.modelo, self.cor, self.Desconectado())
        else:
            print(self.modelo, self.cor, self.Conectado())


mouse1 = Mouse("ZX3000", "Preto", True)
mouse1.Clicar()
mouse1.Info()
mouse1.Desconectado()
mouse1.Clicar()
mouse1.Info()
