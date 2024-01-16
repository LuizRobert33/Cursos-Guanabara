## ler um angulo e mostrar o valor do seno, cosseno e tangente ##
import math
A = float(input("Digite um numero de um angulo: "))
R = math.radians(A) ## transformar em radiandos ##
S = math.sin(R) ## transforma radiandos em seno ##
C = math.cos(R) ## transforma radiandos em cosseno ##
T = math.tan(R) ## transforma radiandos em tangente ##

print("O seno do numero digitado e de: {:.2} o cosseno do numero digitado e de: {:.2} a tangente do numero digitado e de: {:.2}".format(S,C,T))
