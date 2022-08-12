class Banco:
    def __init__(self, nome):
        self.nome = nome

    def Depositar(self, valorDepositado):
        self.valor = valorDepositado
        print(f"Eu depositei:", valorDepositado)

    def Sacar(self, valorSacado):
        self.saque = valorSacado
        print(f"Saquei:", valorSacado)

    def Saldo(self):
        resp = self.valor - self.saque
        print(f"Saldo da conta", self.nome, "é de:", resp)


contaBanco = Banco('joao')
contaBanco.Depositar(2000)
contaBanco.Sacar(90)
contaBanco.Saldo()
