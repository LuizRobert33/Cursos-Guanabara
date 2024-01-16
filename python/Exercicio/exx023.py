## Diga se o nome da pessoa tem "silva" no nome ##
N = str(input("Digite o seu nome: ")).strip()
print(N[:6].upper() == "SILVA")