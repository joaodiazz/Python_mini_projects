def calc(num1, num2, operacao):
    if(operacao == 1):
        return num1 + num2
    elif(operacao == 2):
        return num1 - num2
    elif(operacao == 3):
        return num1 * num2
    elif(operacao == 4):
        return num1 / num2
    else:
        return 0


print(calc(8, 2, 3))
