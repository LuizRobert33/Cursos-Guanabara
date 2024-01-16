## sorteio da mega cena ##
import random

num_jogos = int(input("Quantos jogos deseja gerar:? "))

jogos = []
for i in range(num_jogos):
    jogo = []
    while len(jogo) < 6:
        num = random.randint(1, 60)
        if num not in jogo:
            jogo.append(num)
    jogo.sort()
    jogos.append(jogo)

print("\nPalpites gerados:")
for i, jogo in enumerate(jogos):
    print(f"Jogo {i+1}: {jogo}")
