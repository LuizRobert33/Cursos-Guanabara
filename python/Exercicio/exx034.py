## Aprovando Emprestimo  ##
ValorCasa = float(input("Digite o valor da casa: "))
Salario = float(input("Digite o seu salario: "))
Prestação = int(input("Digite em quantos anos vai parcelar: "))
## a prestação não pode exceder 30% do salario do usuario ##
Emprest= ValorCasa/(Prestação*12)
SalarioNot = Salario*0.30

if Emprest>SalarioNot:
    print("o valor da casa e de {:.2f} em prestações de {:.2f} durantes {} anos então o Emprestimo foi Negado".format(ValorCasa,Emprest,Prestação))
else:
    print("o valor da casa e de {:.2f} em prestações de {:.2f} durantes {} anos então o Emprestimo foi Liberado".format(ValorCasa,Emprest,Prestação))   
