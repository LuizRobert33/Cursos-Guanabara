## aprofundamento em matriz ##
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))

print('-=' * 15)
for i in range(0,3):
    for j in range(0,3):
        print(f'[{matriz[i][j]:^5}]', end='')
    print()
print('-=' * 15)

soma_pares = 0
for i in range(0,3):
    for j in range(0,3):
        if matriz[i][j] % 2 == 0:
            soma_pares += matriz[i][j]

print(f'A soma dos valores pares é {soma_pares}')

soma_coluna3 = 0
for i in range(0,3):
    soma_coluna3 += matriz[i][2]

print(f'A soma dos valores da terceira coluna é {soma_coluna3}')

maior_valor = max(matriz[1])

print(f'O maior valor da segunda linha é {maior_valor}')
