import geometry

N1 = float(input("Digite um numero: "))
N2 = float(input("Digite outro numero: "))
print(f"a area do rentangulo e {geometry.retangulo(N1,N2)}")
print(f"a area do circulo e {geometry.circulo(N1)}")
print(f"a area do triangulo e {geometry.triangulo(N1,N2)}")