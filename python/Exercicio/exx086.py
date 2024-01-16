## Dicionario em Python ##
situação = dict()
lista = []
Nome = str(input("Digite o nome do(a) aluno: "))
Nota = float(input(f"Digite a media do(a) {Nome}: "))
lista.append(Nome)
lista.append(Nota)   
dados = {"Nome": Nome,"Nota": Nota}
if Nota >=7:
    situação["Situação"] = "Aprovado"
else:
    situação["Situação"] = "Reprovado"

print("Nome é igual a: " ,end="")
print(dados["Nome"])
print("Media igual a: ", end="")
print(dados["Nota"])
print(situação["Situação"])
