from datetime import date

user = False
data = date.today()
thisYear = data.year
useName = input("Digite seu nome completo: ")
while(user == False):
    try:
        bornUse = int(input("Em que ano você nasceu? "))
        if(bornUse >= 1922):
            user = True
            age = thisYear - bornUse
            print("\n")
            print(useName, "tem ou completará", age, "anos de idade.")
        else:
            print("\nDigite um ano entre 1922 e 2021")
    except:
        print("datos invalidos")
