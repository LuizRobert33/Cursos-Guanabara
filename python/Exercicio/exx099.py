## Ficha de Jogador ##
def ficha(a,b):
    print("-" * 30)
    F1 = a
    F2 = b
    if len(F1) == 0:
        F1 = "<Desconhecido>"
    return f"O jogador {F1} fez {F2} gols no campeonato"

N = input("Digite o Nome do jogador: ")
G = input("Digite o Numero de gols no Campeonato: ")

if G.strip().isdigit():
    G = int(G)
else:
    G = 0

print(ficha(N, G))


## Se a condição not isinstance(G, int) 
## for avaliada como verdadeira, significa que G não é um número inteiro. Em seguida, o valor de G é definido como 0.
## A função isdigit() é um método em Python que verifica se todos os caracteres 
# de uma string são dígitos. Ela retorna True se todos os caracteres forem dígitos e False caso contrário.