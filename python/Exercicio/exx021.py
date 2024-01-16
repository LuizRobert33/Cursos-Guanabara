## Digitar um numero e dizer a parte de milhar,centena,dezena e a unidade ##
num = int(input("Digite um numero: "))
n = str(num)
print(""" Analisando o numero: {} vemos que sua
unidade e: {}
sua centena e: {}
sua dezena e: {}
sua milhar e: {} """.format(num,n[3],n[2],n[1],n[0]))