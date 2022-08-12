class Carro:
    def __init__(self, marca, cor, preco):
        self.marca = marca
        self.cor = cor
        self.preco = preco

    def Aceletar(self):
        print("VRUMM!")

    def Ligar(self):
        print("Carro Ligado.")

    def Desligar(self):
        print("Carro Desligado.")


car = Carro('fiat', 'preto', '10000')
car.Ligar()
car.Aceletar()
car.Aceletar()
car.Desligar()
