# conseguimos gerar uma lista a partir do processamento de uma coleção de dados.

#                                       sintaxe 

# [operacao ou funcao ou iteravel - for elemento in iteravel - condição(se necessario)]

#ex

#loop for simples

impares = [1,3,5,7,9,11,13,15,17,19,21]

pares = []

for numeros in impares:
    pares.append(numeros * 2) # multiplicamos todos os valores da lista de numeros impares por 2 e anexamos dentro de uma lista chamada pares
    
print(pares) # [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42]



#usando list comprehension

listaImpares = [1,3,5,7,9,11,13,15,17,19,21]

listaPares = [(num * 2) for num in listaImpares] # para cada item na lista impares

print(listaPares)  # [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42]

#passamos uma operação (num * 2) e logo depois passamos o loop iterando um iteravel (nesse caso uma lista de numeros impares)

#para cada numero em lista impares ( for num in listaImpares ), multiplica cada um desses numeros ( (num * 2) ) por 2


#podemos usar ferramentes com essas listas criadas por metodo Comprehension do mesmo jeito que listas normais

print(listaPares[3]) # 14 # acha o elemento de indice 3 
print(sum(listaPares)) # 242 # soma os valores dentro da lista
print(listaPares.index(34))  # 8 # encontrou o indice do numero 34 na lista criada por comprehension


#   lista comprehesion com estruturas condicionais

#if

listaNumeros = list(range(1,11))

pares = [num for num in listaNumeros if num % 2 == 0] 

impares = [num for num in listaNumeros if num % 2 != 0]

print(pares) # [2, 4, 6, 8, 10]

print(impares) # [1, 3, 5, 7, 9]


#outro exemplo


letras = ['a','b','c','d','e','f','g','h','i']

vogais = [letra for letra in letras if letra in 'aeiou'] # quero que me retorne letra , para letra in letras se letra estiver em 'aeiou' 

consoantes = [letra for letra in letras if not letra in 'aeiou'] # quero que me retorne letra, para letra in letras se letra não estiver em 'aeiou'


print(vogais) # ['a', 'e', 'i']

print(consoantes) # ['b', 'c', 'd', 'f', 'g', 'h']


# outro exemplo

numeros = [num for num in range(1,11) if num % 2 == 0] # quero que me retorne num para num no range de 1 a 10, ou seja nos numeros de 1 a 10, se resto da divisao de num por 2 for igual 0

#ou seja, me retorna todos os numeros pares dentro do range de 1 a 10

print(numeros) # [2, 4, 6, 8, 10]


#if e else  

#quando temos somente o if ele vai depois do for, ja quando temos if e else eles vem antes do for

listaRange = list(range(1,10))

listaRangeNova = [num if num <= 5 else num * 10 for num in listaRange] #retorna num se num for menor ou igual a 5, se nao retorna num * 10, para num in listaRange

print(listaRangeNova)  # [1, 2, 3, 4, 5, 60, 70, 80, 90]





#comprehension em matrizes


matriz = [[1,2,3],[4,5,6],[7,8,9]]

[[print(num, end=" ") for num in linha] for linha in matriz] # 1 2 3 4 5 6 7 8 9

# como as matrizes são listas dentro de listas, devemos acessar elas usando 2 loops for, um para iterar as listas dentro da lista principal e outro para acessar os valores dentro das listas filhas


matrizNova = [[num * 3 for num in linha] for linha in matriz] # para cada lista filha (linha) in matriz, e para cada numero (num) in lista filha (linha), retorne os numeros multiplicados por 3

print(matrizNova) # [[3, 6, 9], [12, 15, 18], [21, 24, 27]]  # retorna uma matriz com todos os numeros multiplicados por 3

