## Alistamento militar ##
AnoNasc= int(input("Digite seu ano de nascimento: "))
idade = 2023 - AnoNasc
alistamento = 18 - idade
Anoalistamento = 2023 + alistamento

if idade<18:
    print("Você tem {} anos e falta {} anos para o seu alistamento que sera em {}".format(idade,alistamento,Anoalistamento))
elif idade>=18:
    print("Você tem {} anos e precisa se alistar IMEDIATAMENTE".format(idade))