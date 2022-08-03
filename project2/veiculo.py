rodas = 6
peso = 4000
pessoas = 2

if(rodas <= 3) and (rodas > 1):
    print("A")
elif(rodas == 4) and (pessoas <= 8) and (peso <= 3500):
    print("B")
elif(rodas >= 4) and (peso >= 3500) and (peso <= 6000):
    print("C")
elif(rodas >= 4) and (pessoas >= 8):
    print("D")
elif(rodas >= 4) and (peso >= 6000):
    print("E")
