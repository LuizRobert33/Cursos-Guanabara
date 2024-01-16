## Segmentos que formam um triangulo  ##
## a regra para forma uma triangulo e que a soma de 2 lados
## Não pode ser menos que o terceiro lado ##

s1 = float(input("Digite o primeiro seguimento: "))
s2 = float(input("Digite o segundo seguimento: "))
s3 = float(input("Digite o terceiro seguimento: "))
if (s1+s2) > s3 and (s1+s3) > s2 and (s2+s3) > s1:
    print("Podem formar um triângulo.")
else:
    print("Não podem formar um triângulo.")