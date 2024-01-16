## Contando Vogais em Tuplas ##
palavras = ("APRENDER","PROGRAMAR","VIVER","COMER","CAFE")
for n in palavras:
    print(f"\n Na palvra {n} temos: ", end="")
    for p in n:
        if p.upper() in "AEIOU":
            print(p, end=" ")
