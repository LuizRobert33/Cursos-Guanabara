## Maior e Menor peso ##
maior = 0
menor = 0
for p in range(1,6):
    peso = float(input("Digite um peso: "))
    if peso>maior:
        maior = peso
    if menor == 0 or menor > peso:
        menor = peso
print("Maior {} e menor {}".format(maior,menor))           