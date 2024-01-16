## Indice de massa corporal ##
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura**2)
if imc<18.5:
    print("Seu imc e: {}".format(imc))
    print("ABAIXO DO PESO")
elif imc>=18.5 and imc < 25:
    print("Seu imc e: {}".format(imc))
    print("PESO IDEAL")
elif imc>=25 and imc < 30:
    print("Seu imc e: {}".format(imc))
    print("SOBREPESO")   
elif imc>=30 and imc < 40:
    print("Seu imc e: {}".format(imc))
    print("OBESIDADE")   
elif imc>=40:
    print("Seu imc e: {}".format(imc))
    print("OBESIDADE MÓRBIDA")                  