## Criando um Menu de Opções ##
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
opcao = 0
while opcao !=5:
    print("""        [1] somar
        [2] multiplicar
        [3] maior
        [4] informar novos numeros
        [5] sair do programa             """)
    opcao = int(input("Qual sua opção: "))
    if opcao == 1:
        somar = n1 + n2
        print("{} + {} = {}".format(n1,n2,somar))
    elif opcao == 2:
        produto = n1*n2
        print("{} x {} = {}".format(n1,n2,produto))   
    elif opcao == 3:
         if n1>n2:
            maior = n1
         else:
            maior = n2

            print("entre {} e {} o maior e {}".format(n1,n2,maior))
    elif opcao == 4:
        print("Informe os numeros novamente")
        n1 = int(input("Digite um numero: "))
        n2 = int(input("Digite outro numero: "))


    elif opcao > 5:
         print("opção invalida, tente novamente: ")        
print("----------------------------------------------------")
           
print("FIM DO PROGRAMA!")   


 