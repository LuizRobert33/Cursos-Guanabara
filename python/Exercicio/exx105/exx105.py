import string_operations
string = str(input("Digite uma frase: "))
print(f"total de palavras {string_operations.contador(string)}")
print(f"total de vogais {string_operations.vogais(string)}")
print(f"palavra invertida {string_operations.inverter(string)}")