## Analisando e Gerando Dicionarios ##
def Notas(*num, sit=False):
    """
    Parametro de comentario
    """
    d = dict()
    print("-" * 30)
    d["total"] = len(num)
    d["Maior"] = max(num)
    d["Menor"] = min(num)
    d["Media"] = sum(num) / len(num)
    
    if sit:
        if d["Media"] >= 7:
            d["Situação"] = "Boa"
        elif d["Media"] >= 5:
            d["Situação"] = "Razoavel"    
        else:
            d["Situação"] = "Ruim"

    return d


resp = Notas(10, 9.5, 3.5, sit=True)
print(resp)
help(Notas)