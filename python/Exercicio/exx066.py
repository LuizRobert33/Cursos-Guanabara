## Estatísticas em produtos ##
c=sp=0
n = str(input('Produto: '))
p = float(input('Preço: R$ '))
n2 = n
p2 = p
sp += p
if p >= 1000: c += 1
e = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
while e != 's' and e != 'n':
   e = str(input('Por favor escolha S, para sim ou N, para não: ')).strip().lower()[0]
while True:
   n = str(input('Produto: '))
   p = float(input('Preço: R$ '))
   sp += p
   if p >= 1000: c += 1
   if p < p2:
      p2 = p
      n2 = n
   e = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
   while e != 's' and e != 'n':
      e = str(input('Por favor escolha S, para sim ou N, para não: ')).strip().lower()[0]
   if e == "n": break
print(f"Foi gasto um total de \033[1;33mR$ {sp:.2f}\033[m. Dentre eles, \033[1;33m{c}\033[m custaram mais de \033[1;33mR$1000\033[m, sendo que o menor deles foi o(a) "
      f"\033[1;33m{n2}\033[m, com o custo de \033[1;33mR$ {p2:.2f}\033[m")