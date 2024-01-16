## tratando varios valores ##
Numero = 0
Soma = 0
SomaT = 0
cont = 0
while Numero != 999:
    Numero = int(input("Digite um numero: [digite 999 para parar]: "))
    cont += 1
    Soma = Numero + Soma
SomaT = Soma - 999        
print("foram digitados {} numeros soma de todos os numeros digitados e: {}".format(cont - 1,SomaT))