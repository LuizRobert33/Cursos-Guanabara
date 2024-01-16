## crie um programa que leia o nome completo de uma pessoa e mostre:
## nome com todas as letras maisculas
## nome com todas as letras minusculas
## quantas letras tem o primeiro nome
## quantas letras tem o nome sem considerar os espaços   ##
N = (input("Digite o seu nome: "))
letra = len(N) - N.count(" ")
print(N.upper())
print(N.lower())
print(len(N.split()[0]))
print(letra)
