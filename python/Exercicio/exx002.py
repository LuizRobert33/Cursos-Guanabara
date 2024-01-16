## Dissecando Uma Variavel ##

V = input("Digite algo: ")
print("O tipo primitivo desse valor e:" ,type(V))
print("E somente espaço?: ",V.isspace())
print("E numerico?: ",V.isnumeric())
print("E alfabetico?:",V.isalpha())