## Maior e Menor valor em tupla ##
import random
maior = 0
sorteio = (random.randint(1,11),random.randint(1,11),random.randint(1,11),random.randint(1,11),random.randint(1,11))
print(f"os valores sorteados foram {sorteio}")
print(f"o maior valor sorteado foi {max(sorteio)}")
print(f"o menor valor sorteado foi {min(sorteio)}")