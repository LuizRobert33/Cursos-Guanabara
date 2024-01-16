from Bibli import * 


def arqExiste(nome):
    try:
        a = open(nome,"rt")
        a.close
    except FileNotFoundError:
        return False
    else:
        return True    
    

def CriarArquivo(nome):
    try: 
        a = open(nome,"wt+")    
        a.close()
    except:
        print("Houve um erro na criação do arquivo")
    else:
        print(f"Arquivo {nome} Criado com sucesso")      


def LerArquivo(nome):
    try:
        a = open(nome,"rt")
    except:
        print("Erro ao ler o Arquivo")
    else:
        cabeçalho("Pessoa(s) Cadastradas")
        print(a.read())
    finally:
        a.close()    
def cadastrar(arquivo,nome="Desconhecido",idade=0):
    try:
         a = open(arquivo,"at")
    except:
        print("Houve um ERRO  abertura os dados dados")   
    else:
       try:
           a.write(f"{nome}{idade}\n")
       except:
            ("Houve um Erro de Escrever os dados") 
       else:
           print(f"Novo registro de {nome} adicionado")  
           a.close()          

