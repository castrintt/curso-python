
# Sorted - ordena de forma crescente os valores

# Sorted: semelhante ao sort. Porém, sort é usado apenas em listas e sorted é usado em qualquer iteravel (lista, tupla, dicionarios e conjuntos)

#OBS - CONJUNTOS NÂO SÂO ORDENADOS, PORTANTO SORTED E NEM REVERSED FUNCIONAM 

#SORTED ORDENA OS VALORES

# OBS INDEPENDENTE DO ITERAVEL O SORTED VAI RETORNAR UMA LISTA COM A ORDENÇÃO DOS VALORES


#ex

tupla = 24,5,4,12,34,3,121

print(sorted(tupla)) # [3, 4, 5, 12, 24, 34, 121] # ordenado em crescente

lista = [1,2,5,4,67,34,322,3,4,12,23,4,354]

print(sorted(lista)) # [1, 2, 3, 4, 4, 4, 5, 12, 23, 34, 67, 322, 354]

dicionario = {
    'valor1':1,
    'valor3:':34,
    'valor2':22,
    'valor4':11
}

print(sorted(dicionario)) # ['valor1', 'valor2:', 'valor3', 'valor4'] # ordena as chaves
print(sorted(dicionario.keys())) # ['valor1', 'valor2', 'valor3:', 'valor4']  # tbm ordena as chaves

print(sorted(dicionario.values())) # [1, 11, 22, 34] # ordena os valores


# CASO A ORDENAÇÃO SEJA FEITA EM UM DICIONARIO UTILIZANDO O METODO ITEMS() O SORTED ORDENA OS VALORES POREM COLOCA ELES DENTRO DE UMA LISTA, SEPARANDO CHAVE E VALOR POR TUPLAS
# Ex
print(sorted(dicionario.items())) # [('valor1', 1), ('valor2', 22), ('valor3:', 34), ('valor4', 11)] # ordena chaves e valores



# PODEMOS INVERTER O SORTED (TORNA-LO UM ORDENADOR QUE ORDENA DE FORMA DECRESCENTE)
# BASTA PASSARMOS O PARAMETRO REVERSE COMO 'True'
# POR DEFAULT O REVERSE VEM COMO FALSE
#ex

print(sorted(tupla, reverse=True)) # [121, 34, 24, 12, 5, 4, 3]
print(sorted(lista, reverse=True)) # [354, 322, 67, 34, 23, 12, 5, 4, 4, 4, 3, 2, 1]








# REVERSED - inverte a ordem dos valores, porem sem ordena-los

# Reversed é parecido com reverse, porem reverse só é utilizado em listas, reversed pode ser usado em qualquer iteravel

#OBS - CONJUNTOS NÂO SÂO ORDENADOS, PORTANTO SORTED E NEM REVERSED FUNCIONAM 

# PARA ACESSAR REVERSED DEVEMOS COLOCA-LO EM UMA LISTA (OU SEJA, PRECISAMOS LISTA-LOS)
# LEMBRANDO QUE REVERSED SEMPRE RETORNA UMA LISTA
# ex

listaUm = [1,3,6,2,4,5,8,7,9,10]

novaLista = reversed(listaUm)

print(list(novaLista)) # [10, 9, 7, 8, 5, 4, 2, 6, 3, 1]  #  inverteu os valores, sem ordena-los


tuplaUm = 1,2,3,4,5,6,7,8

novaTupla = reversed(tuplaUm)

print(list(novaTupla)) # [8, 7, 6, 5, 4, 3, 2, 1]

dicionarioUm = {
    'valor1':1,
    'valor2':2,
    'valor3':3
}

novoDic1 = reversed(dicionarioUm)
print(list(novoDic1)) # ['valor3', 'valor2', 'valor1'] # inverte só as chaves

novoDic2 = reversed(dicionarioUm.keys())
print(list(novoDic2)) # ['valor3', 'valor2', 'valor1'] # inverte só as chaves tbm

novoDic3 = reversed(dicionarioUm.values())
print(list(novoDic3)) # [3, 2, 1]  # inverteu as chaves

novoDic4 = reversed(dicionarioUm.items())
print(list(novoDic4)) # [('valor3', 3), ('valor2', 2), ('valor1', 1)] # inverte as chaves e valores, porem retorna uma lista de tuplas (as tuplas estão separadas por chave e valor)