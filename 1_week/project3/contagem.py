import time

print("Iniciando contagem regressiva")
time.sleep(1)

for i in range(10, 0, -1):
    resp = i
    print(resp)
    time.sleep(1)

print("BOOM!!")
