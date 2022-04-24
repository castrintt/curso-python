# 1) utilize o modulo random e suas funções para realizar os seguintes procedimentos abaixo

# a) random - obter um numero aleatorio inteiro entre 1 e 10 e armazenar em uma variavel x

# b) randint - obter x numeros aleatorios inteiros entre 0 e 100 e armazena-los em uma lista

# c) shuffle - embaralhar a lista usada no randint

# d) choice - selecionar um elemento aleatorio da lista onde foi usado shuffle

# e) loop  imprimir os numeros da lista que são maiores que o numero selecionado



# resolução fazendo importanção de forma generica

import random

x = round(random.random() * 10)

print(x)

lista = []

while len(lista) < x:
    lista.append(randint(0,100))

print(lista)

random.shuffle(lista)

escolha = random.choice(lista)

print(f'O numero escolhido foi {escolha}')

for num in lista:
    if num > escolha:
        print(num,end=", ")

# resolução usando importação especifica das funções usando alias (as)

from random import (
    random as rd,
    randint as rin,
    shuffle as shu,
    choice as ch
)

x = round(rd() * 10)

print(x)

lista = []

while len(lista) < x:
    lista.append(randint(0,100))

print(lista)

shu(lista)

print(lista)

escolha = ch(lista)
print(escolha)

for num in lista:
    if num > escolha:
        print(num, end=', ')



# resolução usando o import com * (asterisco)

from random import *

x = round(random() * 10)

print(x)

lista = []

while len(lista) < x:
    lista.append(randint(0,100))

print(lista)

shuffle(lista)

escolha = choice(lista)

print(escolha)

for num in lista:
    if num > escolha:
        print(num, end=', ')
