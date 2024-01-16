## descborir qual maior e qual o menor numero digitado ##
N1 = int(input("Digite um numero: "))
N2 = int(input("Digite outro numero: "))
N3 = int(input("Digite outro numero: "))
if N1>N2 and N1>N3:
    maior = N1
if N2>N1 and N2>N3:
    maior = N2
if N3>N1 and N3>N2:
    maior = N3
if N2<N1 and N2<N3:
    menor = N2  
if N1<N2 and N1<N3:
    menor = N1
if N3<N2 and N3<N1:
    menor = N3
print("o maior numero digitado é {}".format(maior))
print("o menor numero digitado é {}".format(menor))   
                            
