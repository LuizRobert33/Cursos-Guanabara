## Função que descobre o Maior e Menor ##
from time import sleep
def valores(*num):
    cont = 0
    maior = 0
    print("Analisando Valores passados:")
    print("*"*30)
    for valor in num:
        print(f" {valor}",end="", flush=True)
        sleep(0.4)
        cont +=1
    if cont == 0:
        maior = valor
    else:
        if valor > maior:
            maior = valor     

    print(f"\nForam informados {cont} valores")
    print(f"O Maior valor e {valor}")          


valores(2,5,7,8,9)
valores(5,20,17)
valores(2,5)
valores(0)



