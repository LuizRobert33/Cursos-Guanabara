## Analisando valores em tuplas ##
num = (int(input("Digite um numero:")),int(input("Digite um numero:")),int(input("Digite um numero:")),int(input("Digite um numero:")))
print(f"Voce digitou os valores{num}")
print(f"O valor 9 apareceu {num.count(9)} vezes")
if 3 in num:
    print(f"o valor 3 foi digitado na posição {num.index(3)+1}")
else:
    print(f"o valor 3 não foi digitado em nenhuma posição")
print("Os valores pares digitador foram:", end="")    
for n in num:
    if n % 2==0:
        print(n, end="")     
