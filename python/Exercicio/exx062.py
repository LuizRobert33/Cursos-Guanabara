## Soma de numeros com flag ##
Numero = 0
soma = 0
cont = 0
while Numero != 999:
    Numero = int(input("Digite um numero [digite 999 para parar]: "))
    soma = Numero + soma
    cont += 1
    if Numero == 999:
        break
print(f"você digitou {cont-1} valores e a soma entre eles e {soma-999}")    

## outra opção de solução e botar o laço de condição antes da varivel "soma'
## assim o 999 não vai ser considerador ##