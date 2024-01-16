## Sorteando e Somando Valores ##
import random
Numeros = list()
def sorteio(lista):
  for c in range(0,5):
   lista.append(random.randint(1,10))    


def SomaPar(lista):
  soma = 0
  for valor in lista:
        if valor %2 ==0:
            soma += valor
  return soma         






sorteio(Numeros)
print(Numeros)
soma_pares=SomaPar(Numeros)
print(f"Somando os valores pares de {Numeros}, temos {soma_pares}")