## Função Contador ##
from time import sleep
def contador(a,b,c):
    print(f"Contagem de {a} ate {b} pulando de {c} em {c}:")

    if(b>a):
        cont = a
        while cont <= b:
            print(f"{cont} ", end=" ")
            cont += c
        print("FIM")     
    else:
        cont = a
        while cont >= b:
            print(f"{cont} ", end=" ")
            cont -= c
        print("FIM")    
        
        


contador(1,10,1)
contador(0,20,2)
contador(30,5,2)    
