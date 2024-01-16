## Descobrir se o ano e bissexto ##
A = int(input("Que ano quer analisar? "))
if A % 4==0 and A % 100!= 0 or A % 400 == 0:
    print("O ano e BISSEXTO")
else:
    print("O ano não e BISSEXTO")    