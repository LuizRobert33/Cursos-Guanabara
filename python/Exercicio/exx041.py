## Gerenciador de Pagamento ##
print("-------ATACADÃO LOJAS LUIZ-------")
Valor = float(input("Digite o valor das suas compras: "))
print("""Escolha a forma de pagamento
[1] A vista no dinheiro/cheque
[2] A vista no cartão
[3] Até 2x no cartão
[4] Aparti de 3x no cartão""")
opção = int(input("Sua opção: "))
if opção == 1:
    resultado = Valor - (Valor*0.10)
    print("Sua compra foi de {} R$ e com o desconto fica de {}R$".format(Valor,resultado))
elif opção == 2:
    resultado = Valor - (Valor*0.05)
    print("Sua compra foi de {} R$ e com o desconto fica de {}R$".format(Valor,resultado))     
elif opção == 3:
    resultado = Valor/2
    print("Sua compra de {} R$ foi parcelada em 2x e ficou {}".format(Valor,resultado))  
elif opção == 4:
    parcelas = int(input("Digite suas parcelas: "))
    resultado = Valor + (Valor*0.20)
    resultadoP = resultado/parcelas
    print("Sua compra foi de {} R$ e foi parcelada em {}x e ficou em {}R$".format(Valor,parcelas,resultadoP))            