import time


def calc():
    n1 = int(input("Primeiro número da operação: "))
    n2 = int(input("Segundo número da operação: "))
    time.sleep(1)
    print("\nEscolha uma das operações ou digite 0 para sair.\n1: Soma\n2: Subtração\n3: Multiplicação\n4: Divisão\n0: Sair")
    resp = int(input("\nSua escolha: "))

    if(resp == 1):
        print("\nVocê escolheu Soma!")
        print("a Soma de", n1, "e", n2, "é igual a:", (n1 + n2), "\n")
        time.sleep(1)
        return calc()
    elif(resp == 2):
        print("\nVocê escolheu Subtração!")
        print("a Subtração de", n1, "e", n2, "é igual a:", (n1 - n2), "\n")
        time.sleep(1)
        return calc()
    elif(resp == 3):
        print("\nVocê escolheu Multiplicação!")
        print("a Multiplicação de", n1, "e", n2, "é igual a:", (n1 * n2), "\n")
        time.sleep(1)
        return calc()
    elif(resp == 4):
        print("\nVocê escolheu Divisão!")
        print("a Divisão de", n1, "e", n2, "é igual a:", (n1 / n2), "\n")
        time.sleep(1)
        return calc()
    elif(resp >= 5):
        print("Esta opção não existe!")
        print("Tente novamente.")
        time.sleep(1)
        return calc()
    else:
        return print("Até a proxima!")


print(calc())
