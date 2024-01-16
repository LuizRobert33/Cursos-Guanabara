## Dizer se a cidade começa com a palavra "Santo" ##
C = str(input("Digite o nome da cidade: ")).strip()
print(C[:5].upper() == 'SANTO')
