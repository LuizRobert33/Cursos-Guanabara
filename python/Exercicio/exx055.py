## jogo de adivinhação ##
import random
palpites = 0
computador = random.randint(0,10)
print("JOGO DE ADIVINHAÇÃO! SEJA BEM-VINDO, VAMOS COMEÇAR?")
print("ACABEI DE PENSAR EM UM NUMERO ENTRE 1 E 10 TENTE ADIVINHAR......")
acertou = False
while not acertou:
    jogador = int(input("Qual o seu palpite? "))
    palpites = palpites + 1
    if jogador == computador:
        acertou = True
    elif jogador < computador:
        print("Mais.... tente novamente: ")
    elif jogador > computador:
        print("Menos... tente novamente: ")
print("Você acertou em {} tentativas.PARABENS!".format(palpites))               