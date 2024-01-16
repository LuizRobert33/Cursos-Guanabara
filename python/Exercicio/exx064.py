## jogo par ou impar ##
from random import randint
from time import sleep

print('-=-' * 20)
print('VAMOS JOGAR JOKEN PO!')
print('-=-' * 20)

cout = 0

while True:
    num = int(input('Digite um Valor: '))
    npc = randint(1, 10)
    escolha = str(input('Par ou Impar? [P/I] ').upper().strip())
    print('-' * 40)
    sleep(0.5)
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('POOOO!')
    if (num + npc) % 2 == 1:
        print(f'Você jogou {num} e o computador {npc}. Total de {num + npc} DEU IMPAR')
    elif (num + npc) % 2 == 0:
        print(f'Você jogou {num} e o computador {npc}. Total de {num + npc} DEU PAR')
    print('-' * 20)
    if escolha == 'P' and (num + npc) % 2 == 0 or escolha == 'PAR' and (num + npc) % 2 == 0:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        cout += 1
    elif escolha == 'I' and (num + npc) % 2 == 1 or escolha == 'IMPAR' and (num + npc) % 2 == 1:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        cout += 1
    elif escolha not in ('P,I,PAR,IMPAR'):
        print('ERRO, tente novamente...')
    else:
        break
    print('-=-' * 20)
print(f'GAME OVER! Você venceu {cout} vezes.')