## extraindo dados de uma lista ##
Lista = []
cont = 0
while True:
    N = int(input("Digite um valor: "))
    cont += 1
    Lista.append(N)
    Lista.sort(reverse=True)
    S = str(input("Quer continuar [S/N]: ")).strip().upper()       
    if S == "N":
        break
if 5 in Lista:
        print("O valor 5 pertence a essa lista")
else:
        print("O numero 5 não esta presente")      
print(f"foram digitados {cont} valores")   
print(f"valores em orde decrescente {Lista}") 