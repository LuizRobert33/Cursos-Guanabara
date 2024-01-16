## Analisador Completo ##
Tidade = 0
contIdade = 0
maior = 0
NomeMaisvelho = ""
print("=============================")
print("ANALISADOR COMPLETO")
print("=============================")
for c in range(1,5):
    Nome = str(input("Digite o nome da pessoa: "))
    idade = int(input("Digite a idade da pessoa: "))
    sexo = str(input("Sexo [M/F]: ")).upper()
    Tidade = Tidade + idade
    MediaIdade = Tidade/4
    if sexo == "F" and idade <= 20:
        contIdade = contIdade + 1
    if sexo == "M" and idade>0:
        maior = idade
        NomeMaisvelho = Nome
print("A media de idade do grupo e {}".format(MediaIdade))
print("o Nome do Homem mais velho e {}".format(NomeMaisvelho))
print("e tem {} mulheres com menos de 20 anos".format(contIdade))        

        
