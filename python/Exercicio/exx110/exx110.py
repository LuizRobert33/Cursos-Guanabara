## Criando Sistema ##
from Arquivo import *
from Bibli import *
from time import sleep

arquivo = "Nomes.txt"  ## O arquivo Nome.txt foi criado fora das pastas ##

if not arqExiste(arquivo):
    CriarArquivo(arquivo)


while True:
    resposta = menu([ "Cadastra Pessoa", "Ver Pessoas","Sair do Sistema"])
    if resposta == 1:
     cabeçalho("Novo Cadastro")
     Nome = str(input("Digite o nome da pessoa: "))
     idade = LeiaInt("Idade: ")
     cadastrar(arquivo,Nome,idade)
    elif resposta == 2:
       LerArquivo(arquivo) 
    elif resposta == 3:
        print("\033[92mObrigado Volte Sempre\033[0m") 
        break
    else:
        print("\033[91mErro, digite opção valida\033[0m")   
    sleep(1.2)       
