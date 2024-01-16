import converter

F = float(input("Digite a temperatura Celsius: "))
Q = float(input("Digite sua distancia em Km: "))
H = int(input("Digite alguma hora: "))

print(f"A temperatura em fahrenheit de {F} graus celsisus e: {converter.farehrenhait(F):.2f}")
print(f"A distancia em milhas de {Q} km e de : {converter.milhas(Q):.2f}")
print(f"os segundos em {H} hrs são : {converter.horas(H)}")