## salarios do funcionarios com aumentos de 10% e 15% ##
S = float(input("Digite o seu salario: "))
if S>1250:
    N= (S*0.10) + S
    print("Seu novo salario e de {:.2f}".format(N))
else:
    N= (S*0.15) + S    
    print("Seu novo salario e de {:.2f}".format(N))