## Classificando Atletas ##
Idade = int(input("Digite a sua idade: "))
if Idade<= 9:
    print("Atleta classicado como: MIRIM")
elif Idade>9 and Idade<=14: 
    print("Atleta classicado como: INFANTIL")   
elif Idade>14 and Idade<=19: 
    print("Atleta classicado como: JUNIOR")
elif Idade>19 and Idade<=25: 
    print("Atleta classicado como: SENIOR")
else:
    print("Atleta classificado como: MASTER")                  