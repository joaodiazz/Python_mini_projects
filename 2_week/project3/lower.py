import time

print("Transformar a string em minúscula.\n")
time.sleep(1)

resp = "s"

while(resp == "s"):

    converter = input("Escreva algo: ").lower()
    print(converter)

    time.sleep(1)
    resp = input("\nJogar novamente? (S / N) ").lower()
