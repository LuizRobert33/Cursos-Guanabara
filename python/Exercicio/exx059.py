##Sequencia de Fibonacci ##
Termos = int(input("Quantos termos você quer mostrar: "))
t1 = 0
t2 = 1
cont = 3
while cont <=Termos:
    t3 = t1 + t2
    print("{} --> ".format(t3),end="")
    t1 = t2
    t2 = t3
    cont += 1
print("FIM!")    