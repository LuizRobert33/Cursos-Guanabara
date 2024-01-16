## Grupo da maioridade ##
n = 1
contMaior = 0
contMenor = 0
for AnoNascimento in range(1,8):
    AnoNascimento =int(input("Digite o ano que a {} pessoa nasceu: ".format(n)))
    n = n + 1
    idade = 2023 - AnoNascimento 
    if idade>=18:
        contMaior = contMaior + 1
    else:
        contMenor = contMenor + 1
print("Ao todo tivemos {} pessoas maiores de idade".format(contMaior))      
print("Ao todo tivemos {} pessoas menores de idade de idade".format(contMenor))          
