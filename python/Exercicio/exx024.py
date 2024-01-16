## digitar uma frase e mostrar: 
## quantas vezes a letra A aparece
## em que posição ela aparece a primeira vez
## em que posição ela aparece a ultima vez ##
F = str(input("Digite uma frase: ")).upper().strip()
print(F.count('A'))
print(F.find('A')+1)
print(F.rfind('A')+1)
