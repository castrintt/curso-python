# - Modulos são arquivos python que podem ser importados para o  arquivo principal, geralmente contendo funções

# TODOS OS MODULOS PODEM SER ENCONTRADOS AQUI  ------>>>> https://docs.python.org/3/py-modindex.html

# - modulo random : possui funções retornam valores aleatorios.

# METODOS DE IMPORTACAO

# 1) importação do modulo todo 

# sintax: import random

# Desse modo, TODO o modulo é importando, ou seja, todas as classes, funções e atributos ficarão disponiveis na memoria

import random


# Função random - retorna um numero real entre 0 e 1

# para usar uma função de algum modulo a sintaxe é a seguinte
# sintaxe: nome_do_modulo.funcao_a_ser_executada()
# ex
       #nome modulo.função
print( random.random() ) 



# 2) importação expecifica

# LEMBRANDO QUE DESSA FORMA, NÃO PRECISAMOS DECLARAR O NOME DO MODULO QUE EXPORTAMOS NA CHAMADA, OU SEJA
# ao inves de chamar dessa forma: modulo.funcao() /// podemos simplismente chamar a função direto funcao()

# sintax : from nome_do_modulo import Funçao_a_ser_importada

# função randint retorna um numero inteiro aleatorio entre os valores dos parametros

# ex

from random import randint

print(randint(1, 50))  # retorna um numero aleatorio num range de 1 a 50


# função uniform - retorna um numero real aleatorio entre os valores dos parametros
# ex

from random import uniform

print(uniform(1, 50))  # retorna um nuemro real aleatorio num range de 1 a 50


# função choice - retorna um valor aleatorio de um iteravel
# ex

from random import choice

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(random.choice(lista))  # retorna um valor aleatorio dentro da lista


# outro exemplo

premios = ['jogo da vida', 'playstation', 'manete de videogame']

escolhido = choice(premios)

print(f'Mario ganhou {escolhido}')  # Mario ganhou playstation # nesse caso o item sorteado foi o item de indice 1


# função shuffle - retorna um iteravel com os elementos embaralhados
# ex

from random import shuffle

listaDeNumeros = [1, 2, 3, 4, 5]

shuffle(listaDeNumeros)

print(listaDeNumeros)  # [5, 2, 4, 3, 1] # embaralhou os items do iteravel



# TODOS OS MODULOS PODEM SER ENCONTRADOS AQUI  ------>>>> https://docs.python.org/3/py-modindex.html



# modulo statistics

import statistics

numeros = [2, 4, 6, 8, 10]

media = statistics.mean(numeros)  # metodo mean do modulo statistics pega a media dos valores declarados(podendo ser ou não um iteravel)

print(media) # 6





# 3) terceiro modo de importação - utilizando o (as): - apelida um modulo ou uma função

#ex  import random as rd  (nesse caso sempre vamos chamar as funções do random usando rd.funcao() )

import random as rd

lis = [1, 2, 3, 4]
rd.shuffle(lis)

print(lis)  # [1, 3, 4, 2] funciona exatamente da mesma forma




# outro exemplo  from random import shuffle as sh (nesse caso como a importação foi de forma especifica eu posso simplismente usar a seguinte sintaxe para chamar a função shuffle --  sh(iteravel)  )


from random import shuffle as sh

li = [1, 3, 4, 5, 6]

sh(li)

print(li)  # [1, 6, 3, 4, 5] funciona exatamente da mesma forma




# 4 ) utilizando * :  importamos todas as funções do modulo

#sintaxe :  from random import *

# nesse caso nós não precisamos especificar que é o modulo random, somente usar as suas funções

# dessa forma não precisamos declarar o modulo da mesma forma que a importação especifica faz

# ex

from random import *

h = [1, 2, 3, 4, 5]

shuffle(h)

print(h)  # [5, 4, 1, 2, 3] # funciona exatamente da mesma forma




# 5) importando multiplas funções de um modulo

# basta usar a virgula para separar
# sintaxe: from random import shuffle, choice, uniform

from random import suffle, choice, uniform # dessa forma importamos somente as 3 funções do modulo random


# 5.1) outra forma de declarar importações multiplas (mais usado)

# sintaxe :  from modulo import ( funcoes )

#ex 

from random import (
    shuffle,
    randint,
    choice
)
