## Cadastro do Trabalhador ##
informações = dict()
informações["Nome"] = str(input("Digite o seu Nome: "))
informações["Ano"] = int(input("Ano de Nascimento: "))
informações["Carteira"] = int(input("Carteira de Trabalho[0 caso não haja carteira]: "))
if informações["Carteira"] != 0:
    informações["Contratação"] = int(input("Ano de Contratação: "))
    informações["Salario"] = float(input("Salario: "))
    informações["aposentadoria"] = 65 - (informações["Contratação"] - informações["Ano"]) 
print("="*40)
for k,v in informações.items():
    print(f"{k} tem valor {v}")