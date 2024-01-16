def contador(T):
    palavras = T.split()
    return len(palavras)

def vogais(T):
    vogais = 'aeiouAEIOU'
    return sum(T.count(vogal) for vogal in vogais)
def inverter(T):
    return T[::-1]
