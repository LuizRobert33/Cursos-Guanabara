##  Custo de viagem  ##
K = float(input("Digite a distancia da sua viagem: "))
if K>=200:
    R = K*0.45
    print("Você fez uma viagem de {:.2f} km".format(K))
    print("Voçê tera que pagar {:.2f} R$ de passagem".format(R))
else:
    R= K*0.50
    print("Você fez uma viagem de {:.2f} km".format(K))
    print("Voçê tera que pagar {:.2f} R$ de passagem".format(R))