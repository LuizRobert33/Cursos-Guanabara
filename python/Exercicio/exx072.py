## Lista de preços com Tupla ##
listagem = ("Lapis",1.75,"Caneta",2.30,"Caderon",10.0)
print("-----"*10)
print( f'{"LISTAGEM DE PREÇO":^40}' )
print("-----"*10)
for pos in range(0, len(listagem)):
   if pos %2 ==0:         
     print(f"{listagem[pos]:.<30}" ,end="")
   else:
      print(f"R${listagem[pos]:>7.2f}")  
