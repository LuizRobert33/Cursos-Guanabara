## media do alunos  ##
Num1 = float(input("Digite sua primeira nota: "))
Num2 = float(input("Digite sua segunda nota: "))
Media = (Num1+Num2)/2
if Media<5:
    print("Sua media foi {:.2f} é você está reprovado".format(Media))
elif Media>5 and Media<6.9:
    print("sua media foi {:.2f} é você está de recuperação".format(Media))
else:
    print("Sua media foi {:.2f} é você está aprovado".format(Media))         