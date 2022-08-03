nome_aluno = "João"
nota1 = 7
nota2 = 7
media = (nota1 + nota2) / 2
faltas = 2

if(media < 7) or (faltas >= 3):
    print(nome_aluno + " reprovado!")

elif(media >= 7) or (faltas <= 2):
    print(nome_aluno + " aprovado!")
