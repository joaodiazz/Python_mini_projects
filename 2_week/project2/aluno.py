class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = int(nota1)
        self.nota2 = int(nota2)

    def Media(self):
        media = (self.nota1 + self.nota2) / 2
        print(media)

    def Aprovado(self):
        media = (self.nota1 + self.nota2) / 2
        if(media >= 7):
            return "Aprovado"
        else:
            return "Reprovado"

    def Info(self):
        print(self.nome, self.Aprovado())


aluno = Aluno("Joao", 9, 8)
aluno.Media()
aluno.Info()
