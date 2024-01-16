## computador pensa em um numero de 0 a 5 e tente adivinhar qual numero ##
import random
import time ## biblioteca para coisas relacionadas a tempo ##
N = int(input("Digite um numero entre 0 e 5: "))
sorteio = random.randint(0,5)
print("PROCESSANDO.......")
time.sleep(2) ## tempo em segudos ate aparecer o resultado ##
if sorteio == N:
    print("O numero pensado foi {} e seu palpite está correto".format(sorteio))
else:
    print("O numero pensado foi {} e seu palpite está errado".format(sorteio))    