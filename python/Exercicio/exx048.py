## Progressão Aritmetica ##
print("===================================")
print("OS 10 PRIMEIROS TERMOS DE UMA P.A")
print("===================================")
Termo1 = int(input("Digite o primeiro termo: "))
Razao = int(input("Digite a razão: "))
decimoTerm = Termo1 + (10 - 1) * Razao
for c in range(Termo1,decimoTerm + Razao ,Razao):
    print(c)


    

