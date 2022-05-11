# 1 ) manipulando somente a hora --> manipulamos somente a hora se usarmos a classe time dentro do datetime (nesse caso temos acesso a hora, minuto e segundo)

import datetime

jogo = datetime.time(16,0,0)

print(jogo) # 16:00:00

print(type(jogo)) # <class 'datetime.time'>


# 2 ) formatar data e hora -->> strftime() --> assim temos o formato string da nossa data

# para formatar uma data devemos passar como parametro para o strftime como ele deve formatar %d (day), %m(month) e %y(year) em forma de string --> '%d , %m , %y'

import datetime

dataAtual = datetime.datetime.now()

print(dataAtual) # 2022-05-11 11:39:28.465603

dataAtualBrasil = dataAtual.strftime('%d/%m/%y') # dessa forma o python formata os parametros de uma data da forma que quisermos! (usando sempre %d para dia, %m para mes e %y para ano)

print(dataAtualBrasil) # 11/05/22

# ou inves de passarmos o mes como numero podemos usar o %b 

dataAtualBrasil = dataAtual.strftime('%d/%b/%y') 

print(dataAtualBrasil) # 11/May/22 



# 2.1 ) Tabela para formatos do strftime() --> http://docs.python.org/3/library/datetime.html#modulo-datetime



# 3 ) dias da semana usando --> weekday()

# no python o primeiro dia é segunda-feira e começa com indice --> 0 e o ultimo dia é domingo que termina no indica 6

# 0 - segunda-feira -> .... -> 6 - domingo

import datetime


horaAtual = datetime.datetime.now()

print(horaAtual.weekday())  # 2 (mostra no indice qual dia da semana estamos) --> nesse caso estamos no indice 2 , tenha em mente a lista ['segunda','terça','quarta','quinta','sexta','sabado','domingo'] --> o indice 2 é quarta!



# 4 ) tempo de execução --> para isso não usamos o modulo datetime, nós usamos o timeit

import timeit

# vamos criar uma lista e ver quanto tempo o programa demorar para rodar 

numQuadrado = str([num ** 2 for num in range(10000)]) # quero todos os numeros de 0 a  10000 com exceção do 10000, ao quadrado e depois transformados em string( devemos transformar em string pois é uma exigencia de parametro para o timeit )

print(timeit.timeit(numQuadrado, number=100)) # o parametro number define quantas vezes se repete o processo

# 0.0046121000004859525 esse foi o tempo de execução da maquina
