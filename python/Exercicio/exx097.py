## Função para Votar ##
from datetime import date ## pegar o ano atual ##
def votar(a):
    atual = date.today().year
    print("-"*30)
    R = atual - a
    if R>=18:
        print("\033[92mVoto Obrigatorio")
        print(f"Sua idade e {R} anos")
    elif R<18 and R>=16 or R>=65: 
        print("\033[93mVoto Opcional")
        print(f"Sua idade e {R} anos")
    else:
        print("\033[91mNão vota")
        print(f"Sua idade e {R} anos ")

       
        
    


idade = int(input("Digite o seu ano de nascimento: "))
votar(idade)