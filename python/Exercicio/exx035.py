##  Conversão para Base numerica  ##
N = int(input("Digite um numero: "))
print(""" Escolha uma base de conversão
[1] Converte para BINARIO 
[2] Converte para OCTAL
[3] Converte para HEXADECIMAL""")
opção = int(input("Sua opção: "))
if opção == 1:
    print("o numero {} convertido em binario é {}".format(N,bin(N)[2:]))
elif opção == 2:
    print("o numero {} em octal é {}".format(N,oct(N)[2:]))
elif opção ==3:
    print("o numero {} em hexadecimal é {}".format(N,hex(N)[2:]))    
else:
    print("OPÇÂO INVALIDA TENTE NOVAMENTE")    
