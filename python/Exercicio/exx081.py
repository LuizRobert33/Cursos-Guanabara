## Lista com pares e impares ##
N = [[],[]]
valor = 0
for c in range (1,8):
    valor = int(input("Digite o valor: "))
    if valor % 2 == 0:
        N[0].append(valor)
    else:
        N[1].append(valor)         
N[0].sort()
N[1].sort()        
print(f"Os valores pares digitados foram: {N[0]}")
print(f"Os valores impares digitados foram: {N[1]}")