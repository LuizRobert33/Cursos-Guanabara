## Maior e Menor valores da lista ##
posiçãoM = 0
Max =0
Min = 0
cont = 0
Lista = []
while True:
    cont += 1
    V = int(input("Numeros: "))
    Lista.append(V)
    Max = max(Lista)
    Min = min(Lista)
    if cont ==5:
        break

print(f"os numeros digitado para lista foram: {Lista}")    
print(f"O maior numero da lista e: {Max}")
print(f"O menor numero da lista e: {Min}")  

for i, v in enumerate(Lista):
        if v == Max:
            print(f" O Maior Valor está na posição(s) {i}...")
            
for i, v in enumerate(Lista):
        if v == Min:
            print(f" O Menor Valor está na posição(s) {i}...", end="")
            
