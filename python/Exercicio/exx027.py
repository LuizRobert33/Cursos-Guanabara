## Radar de carro ##
V = float(input("Digite a sua velocidade: "))
if V>80:
    V2 = V - 80
    M = V2*7
    print("Você está dirigindo a {:.2f} km/hr".format(V))
    print("Você excedeu o limite de velocidade que e de 80Km")
    print("Deve pagar uma multa de {:.2f}R$".format(M))
else:
    print("Você está dirigindo a {:.2f} km/hr".format(V))
    print("Você está dentro do limite de velocidade,dirija com segurança")    