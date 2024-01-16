## Sorteio de Nomes ##
import random
N1 = input("Digite um nome: ")
N2 = input("Digite outro nome: ")
N3 = input("Digite outro nome: ")
N4 = input("Digite mais um nome: ")
lista = [N1,N2,N3,N4]
sorteio = random.choice(lista) ## fazer sorteio de listas ##
print("O nome sorteado foi {}".format(sorteio))