##   calcular  a area do triangulo retangulo   ##
import math
C1 = int(input("Digite o valor do cateto adjacente: "))
C2 = int(input("Digite o valor do cateto oposto: "))
H = (C1**2) + (C2**2)
H2 = math.sqrt(H) ## tirar raiz quadrada ##
print("A hipotenusa do triangulo e de: {:.2f}".format(H2))
