## Lista composta e análise de dados ##
dados = list()
pessoas = []
pessoasPesadas = []
pessoasLeves = []
leve = pesado = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    res = str(input('Deseja continuar [S/N}?: '))
    if res in 'Nn':
        break
for pes in pessoas :
    if leve == 0 and pesado == 0:
        leve = pesado = pes[1]
    if pes[1] > pesado:
        pesado = pes[1]
    elif pes [1] <= leve:
        leve = pes[1]
for pes in pessoas:
    if pesado == pes[1]:
        pessoasPesadas.append(pes[:][0])
    elif leve == pes [1]:
        pessoasLeves.append(pes[:][0])
print('='*30)
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi {pesado}Kg. Peso de {pessoasPesadas}')
print(f'O menor peso foi {leve}kg. Peso de {pessoasLeves}')

