import time

print("Transformar a string em maiúsculo.\n")
time.sleep(1)

resp = "S"

while(resp == "S"):

    converter = input("Escreva algo: ").upper()
    print(converter)

    time.sleep(1)
    resp = input("\nJogar novamente? (S / N) ").upper()
