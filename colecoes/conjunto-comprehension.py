# é a mesma logica de list comprehension, generators, dict comprehensions

# - relembrando set comprehension

# 1) - não possuem ordenação
# 2) - nao possuem elementos repetidos
# 3) - são declaradas por chaves

# logo

# conjunto = {iterado ou função ou operacao ----  for }

#set comprenhesion simples

conjunto = {num for num in range(1,11)} # retorna os numeros em um range de 1 a 10

print(conjunto) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


frase = 'o rato roeu a roupa do rei de roma'

conjuntoFrase = {letra for letra in frase}

print(conjuntoFrase) # {'p', 'o', 'u', 'r', 'e', ' ', 't', 'i', 'a', 'd', 'm'}


# set comprehension condicional if

conjunto2 = {num for num in range(1,11) if num <= 5} # retorna os numeros menores ou iguais a 5 no range de 1 a 10

print(conjunto2) # {1, 2, 3, 4, 5}


# set comprehension condicional if e else

conjunto3 = {num if num <= 5 else num * 10 for num in range(1,11)} # retorna os numeros num range de 1 a 10 se os numeros forem menores ou iguais a 5, senao retorna numero multiplicado por 10

print(conjunto3) # {1, 2, 3, 4, 5, 70, 100, 80, 90, 60}




# DESAFIO

# 1) - Faça usando comprehension de conjuntos imprimir os multiplos de 3 , porem os não multiplos devem ser impressos com a mensagem print('Desconhecido': {numero})


# usando set comprehension

mult = {numero if numero % 3 == 0 else print(f'Desconhecido: {numero}') for numero in range(1,31)}

mult.remove(None)
print(mult)


# outra forma sem usar set comprehension

prim = set(range(1,31))
res = {''}

print(prim)

for numero in prim:
    if numero % 3 == 0:
        res.add(numero)
    else:
        print(f'Desconhecido: {numero}',end=", " )

res.remove('')
print(res)