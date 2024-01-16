## Calculando a Fatorial
F = int(input("Digite seu fatorial: "))
N = F
calculo = 1
print("Calculando a fatorial de {}".format(F))
while N > 0:
     print("{} --> ".format(N), end="")
     calculo = calculo * N
     N = N - 1
print("{}".format(calculo))     
