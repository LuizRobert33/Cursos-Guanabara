## Nota com Nomes ##
dados = [ ]
media = 0
galera = [ ]
while True:
    dados.append(str(input(f'Nome: ')))
    dados.append(float(input(f'Nota 1: ')))
    dados.append(float(input(f'Nota 2: ')))
    galera.append(dados[:])
    dados.clear()
    usuario = ' '
    while usuario not in 'SN':
        usuario = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if usuario == 'N':
        break
print('No.         Nome         Média')
print('-' * 30)
for indice, pessoas in enumerate(galera):
    media = (pessoas[1] + pessoas[2]) / 2
    print(f'{indice:<7}    {pessoas[0].capitalize():^7}    {media:>7}')
print('-' * 30)
opcao = -1
while opcao != 999:
    opcao = int(input('Mostrar nota de qual aluno? [999 para interromper]: '))
    if opcao != 999:
        for indice, pessoas in enumerate(galera):
            if opcao == indice:
                print(f'As notas de {pessoas[0].capitalize()} foram {pessoas[1]} e {pessoas[2]}.')
                print('-' * 50)