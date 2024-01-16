## Numeros por Extenso ##
cont = ("zero","um","dois","tres","quatro","cinco","seis","sete","oito","nove","dez","onze","doze")
while True:
    Numero = int(input("Digite um numero [entre 0 e 12]: "))
    if 0 <= Numero <= 12:
        break
    print("Tente Novamente!")
print(f"O numero que voce digitou foi {cont[Numero]}")