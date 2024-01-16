def LeiaInt(msg):
    while True:
        try:
            N = int(input(msg))           
        except (ValueError,TypeError):
            print("\033[91mERRO DE VALOR, POR FAVOR DIGITE UM NÚMERO VÁLIDO\033[0m")
            continue
        except (KeyboardInterrupt):
            print("\033[91mERRO DE VALOR, POR FAVOR DIGITE UM NÚMERO VÁLIDO\033[0m")
            return 0
        else:
           return N



def linha(tam = 42):
    return "-"*tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f"{c} - {item}")
        c += 1
    print(linha())
    opc = LeiaInt("Sua opção: ")
    return opc