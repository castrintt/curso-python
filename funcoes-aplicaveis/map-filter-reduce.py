# MAP, FILTER e REDUCE

# são funções pré definidas INTEGRADAS á linguagem (javascript tbm as usa por exemplo)





# MAP - aplica um iteravel em uma função , gerando um resultado para cada elemento do iterável:

# OBS map deve ser associado a uma variavel
# essa variavel retorna um objeto do tipo map, guardado em um endereço de memoria
# map salva os valores e guarda na memoria
# para acessar os valores de map, devemos converter a variavel (que recebe o valor de map) em uma lista

# OBS 2 - COMO UM GENERATOR (comprehension de tuplas) A MAP APÓS O USO SE PERDE (ou seja, voce só o pode usar uma vez)
# sintaxe :  map(função, iteravel)

# ex


def maiorQue10(num):
    if num > 10:
        print('maior')
    else:
        print('menor ou igual')
        
maiorQue10(27) # maior
maiorQue10(8) # menor ou igual

# agora suponhamos que temos que testar todos numeros de uma lista dentro dessa função, por exemplo

lista = [1,2,3,4,5,6,7,3,22,23,1.2,35,78,12,53,10,21,11]

# usando o map para fazer isso simplismente usariamos a sintaxe:
# OBS map deve ser associado a uma variavel

resultado = map(maiorQue10, lista) # <map object at 0x000001D14F56BCA0>
# map salva os valores e guarda na memoria
# para acessar os valores de map, devemos converter a variavel (que recebe o valor de map) em uma lista

print(list(resultado)) # retorna todos os retornos de todos numeros de lista testados na função maiorQue10

# menor ou igual
# menor ou igual
# menor ou igual
# menor ou igual
# menor ou igual
# menor ou igual
# menor ou igual
# menor ou igual
# maior
# maior
# menor ou igual
# maior
# maior
# maior
# maior
# menor ou igual
# maior
# maior

print(list(resultado))  # [] retorna uma lista vazia, pois logo após o uso ele se perde


# USANDO MAP COM LAMBDA


listaNomes = ['igor','maria','raissa','bela','carol','matheus']

nomes = lambda nome: print(f'O nome da pessoa é {nome}')

conversaoNomes = map(nomes,listaNomes)

print(list(conversaoNomes))

# O nome da pessoa é igor
# O nome da pessoa é maria
# O nome da pessoa é raissa
# O nome da pessoa é bela
# O nome da pessoa é carol
# O nome da pessoa é matheus 



# usando map, com lista de tuplas e lambda


nascimento = lambda data: print(f'Data de nascimento {data[0] - data[1]}')
                #passando data de hoje, e idade
listaDeDatas = [(2022, 23),(2022,42),(2022, 17)] 

result = map(nascimento, listaDeDatas) # nesse caso o map vai passar o primeiro elemento como data, no caso uma tupla

print(list(result))

# Data de nascimento 1999
# Data de nascimento 1980
# Data de nascimento 2005




# FILTER - filtra dados originados de uma função ou coleção de dados.
# tambem temos que usar uma conversão (para lista por exemplo) para ver os dados, pois o filter filtra os dados e salva na memoria
# sintaxe: filter(função, iteravel) # mesma sintaxe do map


# exemplo

import math # importando uma biblioteca de matematica

listaNumeros = [1,4,1,3,5,6,3,2,9,7,4,6,9]

resultadoNumeros = filter(lambda num: num > math.pi, listaNumeros) # ou seja (lambda num: num > math.pi) é a função e (listaNumeros) é o iteravel, lembre-se da sintaxe : filter(função, iteravel) a unica diferença aqui é que passamos a função direto pelo parametro, ao inves de escrever ela fora

# essa função testa se os numeros são maiores que pi (3,14)

print(resultadoNumeros) # <filter object at 0x00000190FC393D60>
print(list(resultadoNumeros)) # [4, 5, 6, 9, 7, 4, 6, 9] # todos esses são maiores
print(list(resultadoNumeros)) # [] retorna agora uma lista vazia, pois como o map, só se pode usar uma vez, logo depois se perde


# a espressão lambda acima lambda num: num > math.pi, faz exatamente a mesma coisa que:

# def funcao(*args):
#     for num in args:
#         if num > math.pi:
#             return True
#         else:
#             return False




# USANDO FILTER COM MAP

numeros = [1,2,3,4,6,10,22,12,11,55,23,44]

pares = filter(lambda num: num % 2 == 0, numeros) # filtra todos os numeros pares da lista numeros

# def achaPares(*args): # lambda a cima faz exatamente a mesma coisa que essa função
#     for num in args:
#         if num % 2 == 0:
#             return True
#         else:
#             return False

#print(list(pares)) # [2, 4, 6, 10, 22, 12, 44]


paresAoQuadrado = map(lambda num: num ** 2, pares)  # retorna todos os numeros da lista pares (gerada por um filter) ao quadrado

# def quadrado(*args): # a lambda acima faz exatamente a mesma coisa que esta função
#     for num in args:
#         return num ** 2
    

#print(list(paresAoQuadrado)) # [4, 16, 36, 100, 484, 144, 1936]




# REDUCE - relaciona dados posteriores de uma coleção com resultado da relação de dados anteriores
# USE SOMENTE SE NECESSARIO
#sintaxe : reduce(função, iteravel) # mesma sintaxe de map e filter

# OBS a partir do python3 + reduce() não é mais integrada (built-in) 
# agora temos que importa-la pora usar, a partir do modulo 'functools' (import functools)

# podemos importar a biblioteca inteira ou somente o modulo do reduce

# importando ela inteira - import functools

# importando somente o modulo reduce - from functools import reduce

# ex

from functools import reduce

numers = [2,1,2,3]
                # funcao que recebe dois parametros (usa o primeiro como base e o segundo com potencia)
resultadoReduce = reduce(lambda x ,y : x ** y, numers)

print(resultadoReduce) # 64

# oque o reduce fez ali foi basicamente pegar x = 2 e y = 1, depois 2 ** 1 = 2, logo ele vai repetir esse processo, porem o valor de x agora é o resultado de x ** y anterior, entao x = 2 e o valor de y é o proximo valor na lista (ja foram usados o indice 0 e indice 1 como x e y, agora vamos usar o indice 2) que é 2, entao ele executa 2 ** 2 = 4, agora x vale 4, entao ele pega novamente o proximo elemento da lista(indice 3 [que nesse caso é o ultimo]) que é o 3, então ele pega x = 4 (resultado de x ** y anterior) e y = 3, logo 4 ** 3 = 64

# OBS UTILIZE REDUCE SOMENTE SE NECESSARIO, UTILIZAR O LOOP FOR È MAIS LEGIVEL 99% das vezes
 














# resumindo - map - mapeia uma lista (para ser usado cada item dessa lista como parametro para uma função)
# resumindo - filter - filtra todos valores de uma lista (tendo como parametro uma função)



