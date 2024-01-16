## digitando numero real e float ##
while True:
    try:
        N1 = int(input("Digite um inteiro: "))
        N2 = float(input("Digite um número real: "))
    except ValueError:
        print("\033[91mERRO DE VALOR, POR FAVOR DIGITE UM NÚMERO VÁLIDO\033[0m")
    except KeyboardInterrupt:
        print("\033[91mO USUÁRIO PREFERIU NÃO DIGITAR UM VALOR\033[0m")

    else:
        print(f"O número inteiro digitado foi {N1} e o número real digitado foi {N2}")
        break
    finally:
        print("\033[92mObrigado, volte sempre\033[0m")
