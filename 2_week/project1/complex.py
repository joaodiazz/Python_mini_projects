class Complexo:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def Soma(self):
        a = self.num1
        b = self.num2
        print(a + b)

    def Subtracao(self):
        a = self.num1
        b = self.num2
        print(a - b)

    def Multiplicacao(self):
        a = self.num1
        b = self.num2
        print(a * b)

    def Divisao(self):
        a = self.num1
        b = self.num2
        print(a / b)


calc1 = Complexo(1+2j, 3+4j)
calc1.Soma()
calc1.Subtracao()
calc1.Multiplicacao()
calc1.Divisao()

print("\n")

calc2 = Complexo(-4-1j, 6-2j)
calc2.Soma()
calc2.Subtracao()
calc2.Multiplicacao()
calc2.Divisao()

print("\n")

calc3 = Complexo(+5+7j, -3+9j)
calc3.Soma()
calc3.Subtracao()
calc3.Multiplicacao()
calc3.Divisao()
