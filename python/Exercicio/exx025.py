## leia o nome de alguem e mostre o primeiro e o ultimo nome dela ##
M = str(input("Digite o seu nome: ")).strip().split()
print(M[0])
print(M[len(M)-1])