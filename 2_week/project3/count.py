import time

print("Contador de caracteres.\n")
time.sleep(1)


resp = "s"

while(resp == "s"):

    carac = input("Escreva algo: ")
    print(f"o que você escreveu tem", len(carac), "caracteres.")

    time.sleep(1)
    resp = input("\nJogar novamente? (S / N) ").lower()
