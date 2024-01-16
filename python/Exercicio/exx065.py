## Analise de dados em grupos ##
print("BORA CADASTRAR")
maioridade = 0
cadhom = 0
mulheresnovas = 0
continuar = ""
while True:
    print("--------------------------------------")
    idade = int(input("Idade: "))
    while True:
        sexo = str(input("Sexo [M/F]: ")).upper().strip()
        if sexo in "MF":
            break
    if idade > 18:
        maioridade+=1
    if sexo in "M":
        cadhom+=1
    if sexo in "F" and idade < 20:
        mulheresnovas+=1
    continuar = str(input("Quer continuar? [N/S]")).upper().strip()
    while continuar not in "NS":
        continuar = str(input("Quer continuar? [N/S]"))
    if continuar in "N":
            break

print("--------------RESULTADO--------------")
print(f"Nessa pesquisa, nós tivemos {maioridade} pessoas acima de 18 anos!")
print(f"{cadhom} homens cadastrados")
print(f"E {mulheresnovas} mulher(s) com menos de 20 anos!")

