from enum import Enum
import time


class Erros(Enum):
    err_um = 1
    err_dois = 2
    err_tres = 3


candidato_X = 0
candidato_Y = 0
candidato_Z = 0
branco = 0
nulo = 0
user = False

while (user == False):
    print("Vote Consciente!\n")
    time.sleep(1)

    voto = input("Digite o número do seu candidato: ")

    if (voto == "889"):
        candidato_X += 1
    elif (voto == "847"):
        candidato_Y += 1
    elif (voto == "515"):
        candidato_Z += 1
    elif (voto == "0"):
        branco += 1
    else:
        voto = Erros.err_dois

        if(voto == Erros.err_dois):
            print("seu voto contou como nulo")
            nulo += 1

    resp = input("Gostaria de finalizar a votação? (S ou N): ")
    if(resp == "S") or (resp == "s"):
        print("#################################################\n")
        print(
            f"Candidato_X: {candidato_X}\nCandidato_Y: {candidato_Y}\nCandidato_Z: {candidato_Z}\nNulos e Brancos: {nulo + branco}\n")
        if(candidato_X > candidato_Y) and (candidato_X > candidato_Z):
            print("Candidato_X ganhou!\n")
        elif(candidato_Y > candidato_X) and (candidato_Y > candidato_Z):
            print("Candidato_Y ganhou!\n")
        elif(candidato_Z > candidato_X) and (candidato_Z > candidato_Y):
            print("Candidato_Z ganhou!\n")
        break
    elif(resp == "N") or (resp == "n"):
        user = False
    else:
        resp = Erros.err_tres

        if(resp == Erros.err_tres):
            print("#################################################\n")
            print("Responta com apenas S ou N\n\n")
