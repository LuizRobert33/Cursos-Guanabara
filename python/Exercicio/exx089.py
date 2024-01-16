## Cadastro de Jogador de Futebol ##
Gols = list()
dados = dict()
dados["Nome"] = str(input("Digite o Nome do Jogador: "))
dados["Partidas"] = int(input("Digite o Numero de Partidas: "))

for c in range(1, dados["Partidas"] + 1):
    Gols.append(int(input(f"Quantos gols {dados['Nome']} marcou na partida {c}: ")))

dados["Gols"] = Gols[:]    
dados["total"] = sum(Gols)
print("*****" * 15)    
print(dados)
print("*****" * 15)    
for k, v in dados.items():
    print(f"{k} tem valor de {v}")
print("*****" * 15)    
print(f"O jogador {(dados['Nome'])} jogou {(dados['Partidas'])}")
for i,v in enumerate(dados["Gols"]):
    print(f" na partida {i}, fez {v} gols")
print(f"O total de gols foi de {(dados['total'])}")    

