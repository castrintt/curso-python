# 1) criar uma lista e uma tupla com diversos valores, separar os valores maximos e minimos de cada uma em um conjunto. Por fim, verificar se os valores separados são verdadeiros ou falsos, utilizando o any e all


# minha resolução

lista = list([1,23,23423,1234,321212,23523,1132,2112,232,12313145])

tupla = tuple([123,12423,325123123,23423423,23234,4352153,231432,232,21122,223])

conjunto = set([max(lista), min(lista),max(tupla), min(tupla) ])

print(conjunto) # {123, 12313145, 325123123, 1}

print(any(conjunto)) # True
print(all(conjunto)) # True




# resolução professor

lista = [23,1,12,7.64]

tupla = 0,True,0.54,0,54,True

conjunto = {max(lista), min(lista),max(tupla), min(tupla)}

print(conjunto)

print(any(conjunto))
print(all(conjunto))