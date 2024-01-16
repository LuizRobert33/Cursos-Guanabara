## Validando entradas em Python ##
def entrada(a):
    print("-" * 30)
    while True:
        F1 = a
        if len(F1) == 0 or not F1.isdigit():
            print("\033[91mERRO! Digite um número inteiro válido\033[0m")
            a = input("Digite um número válido: ")
        else:
            print(f"\033[92mVocê digitou o número {F1}\033[0m")
            return int(F1)


N = input("Digite um número: ")
print(f"\033[92mVocê acabou de digitar {N}\033[0m")
entrada(N)


