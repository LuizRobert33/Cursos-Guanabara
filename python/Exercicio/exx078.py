## Dividindo valores em várias listas ##
Lista = []
ListaP = []
ListaI = []
while True:
    N = int(input("Digite um numero: "))
    c = str(input("Quer continuar? [S/N] ")).strip().upper()
    Lista.append(N)
    if c =="N":
       break
for i,v in enumerate(Lista):
    if v % 2 == 0:
        ListaP.append(v)
    else:
        ListaI.append(v)
print(f"Lista completa {Lista}")
print(f"Lista com numeros pares {ListaP}")
print(f"Lista com numeros impares {ListaI}")                
        