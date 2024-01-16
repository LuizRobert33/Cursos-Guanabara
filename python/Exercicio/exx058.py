## Os 10 primeiros termos de um P.A v2 ##
Ptermo = int(input("Digite o primeiro termo: "))
Prazão = int(input("Digite a razão: "))
cont = 1
while cont <= 10:
    print("{} --> ".format(Ptermo), end="")
    Ptermo = Ptermo + Prazão
    cont += 1
print("FIM!")    