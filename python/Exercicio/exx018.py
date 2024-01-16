##  sortear o aluno e sua ordem na apresentação   ##
import random
N1 = input("Digite um nome: ")
N2 = input("Digite outro nome: ")
N3 = input("Digite outro nome: ")
N4 = input("Digite mais um nome: ")
lista = [N1,N2,N3,N4]
random.shuffle(lista)## para embaralhar os nomes da lista ##
print(lista)

