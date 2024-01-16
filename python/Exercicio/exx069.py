## Tuplas com time de futebol ##
## Com 10 times ##
print("=-"*20)
print("TABELA DO BRASILEIRÃO")
tabela = ("Palmeiras","Flamengo","Santos","Galo","São paulo","Cruzeiro","Atletico GO","Atletico Mg","Ceara","Fortaleza")
print(tabela)
print("=-"*20)
print(f"OS 5 PRIMEIROS SÃO: {tabela[0:5]}")
print("=-"*20)
print(f"OS 4 ULTIMOS SÃO: {tabela[6:10]} ")
print("=-"*20)
print(f"TIMES EM ORDEM ALFABETICA: {sorted(tabela)} ")
print(f"O {tabela[5]} está na {tabela.index('Cruzeiro') + 1} posição")
