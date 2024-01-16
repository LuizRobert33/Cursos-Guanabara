## Valores unicos em uma lista ##
numero = list()
while True:
    N = int(input("Digite um valor: "))
   
    if N not in numero:
        numero.append(N)
    else:
        print("Valor duplicado, digite outro valor")    
    C = input("Quer continuar: [S/N] ").strip().upper()
    if C =="N":
        break
ListaOrdenada = sorted(numero,reverse=True)
print(ListaOrdenada)    