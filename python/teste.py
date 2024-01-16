teste = []
teste.append("Luiz")
teste.append(19)
geral = []
geral.append(teste[:]) # Usando a sintaxe de fatiamento para criar uma cópia de teste
teste[0] = "Mary"
teste[1] = 13
geral.append(teste[:]) # Usando a sintaxe de fatiamento para criar uma cópia de teste
print(geral)
