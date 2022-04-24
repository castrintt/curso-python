# Geradores são ITERADORES basicamente objetos que podem ser percorridos como listas porem eles não armazenam dados na memoria

# lembra-se que a função next() retorna dados de um iterador? geradores são iteradores, logo podemos usar o next tbm

# - só podemos iterar ( loops/ funções ) apenas uma vez, depois ele se perde.(pois não são armazenados na memoria)

# Funções que geram geradores são chamadas de funções geradoras

# Funções NORMAIS tem a palavra reservada return (quando o programa reconhece o return ele para a função) funções GERADORAS são diferentes, ao inves de usar a palavra reservada return usamos yield, yield basicamente retorna um elemento por vez

# PARA RETORNAR O CONTEUDO EM UMA FUNÇÂO GERADORA USA-SE A PALAVRA YIELD (funções geradoras retornam um elemento por vez)

# OBS FUNÇÕES GERADORAS SÂO MAIS RAPIDAS, POIS NÃO ARMAZEMAN DADOS NA MEMORIA E SÓ PODEM SER USADOS UMA UNICA VEZ 

# OBS CASO USEM UM LOOP FOR, CUIDADO PARA NÃO CAIR EM UM LOOP INFINITO (OU SEJA, SEMPRE COLOQUEM UM CONTADOR OU UMA OPÇÂO DE PARADA COMO CONDIÇÃO)

# EX


def geradora():
    while True:
        palavra = input('Fale: ')
        yield palavra # indicando para o programa que quando terminarmos o loop (iterarmos todos os elementos de palavra ele vai parar o programa)

print(geradora())   # <generator object geradora at 0x7ffb8d0fcb30> # retorna um objeto gerador
# lembra-se que a função next() retorna dados de um iterador? geradores são iteradores, logo podemos usar o next tbm

print(next(geradora()))
# Fale: igor # digitei igor no input, logo em seguida o yield me retornou o igor e parou a função
# igor

# ESSA FUNÇÃO VAI SEMPRE EXECUTAR QUANDO CHAMARMOS O METODO NEXT
#a cada chamada dessa função ela faz exatamente a mesma coisa que a anterior, pede para o usuario digitar algo, e logo em seguida retorna oque ele escreveu e termina a função

#ELE IRÁ GERAR LOOPS DE ACORDO COM A QUANTIDADE DE NEXT()
print(next(geradora()))
print(next(geradora())) 
print(next(geradora()))



# EX 2 (podemos salvar os valores de yield em um iterador) # (vamos usar tbm try, except e else para tratar eventuais erros, a titulo de exercicio)


def numero():
    cadeia = 0
    while cadeia < 5:
        try:
            numero = int(input('Digite um numero: '))
        except:
            print('Erro')
        else:
            cadeia += 1
            yield numero

lista = list(numero())

print(lista) # [10, 20, 30, 40, 50]
#podemos manipular geradores e transforma-los no que quisermos (lista,tupla e set)
            

#TESTE DE VELOCIDADE - (vamos importar uma biblioteca chamada time, simplismente para medir o tempo de processamento de um gerador e uma função)

import time #importando toda biblioteca


#list comprehension (listas)
tinicio_lista = time.time()
print(sum([valor ** 2 for valor in range(100000000)])) # list comprehension
tfinal_lista = time.time() - tinicio_lista



#generator comprehension (tuplas)

tinicio_gen = time.time()
print(sum((num ** 2 for num in range(100000000)))) # tupla comprehesion ou generator
tfinal_gen = time.time() - tinicio_gen


print(f'Lista demorou {tfinal_lista}') # Lista demorou 27.301981687545776
print(f'Generator demorou {tfinal_gen}') # Generator demorou 22.068155527114868
# # vimos que a list comprehension demorou 5 segundos a mais (arredondando) que um generator


# TESTE DE MEMORIA
# - para executar esse exemplo iremos utilizar a geração de 100000 numeros da sequencia de fibonacci
# - a soma dos 2 antecessores de um numero sempre são iguais a ele
# ex 1 , 1, 2, 3, 5, 8 ... para encontrar o 8 somamos os 2 antecessores 5 e 3

#1) lista

def fibo(max):
    sequencia = []
    x,y = 0 , 1 # x = 0 e y = 1
    while len(sequencia) < max:
        sequencia.append(y)
        x, y = y , x + y # x começa a valer y e y começa a valer x + y
    return sequencia

for item in fibo(100000):
    print(item)
# aumento de 6 % de uso de memoria




# 2) generator
def fibonacci(max):
    x,y = 0 , 1 # x = 0 e y = 1
    contador = 0
    while contador < max:
        x, y = y , x + y # x começa a valer y e y começa a valer x + y
        yield x
        contador +=1
    
for x in fibonacci(100000):
    print(x)
# aumento de 1% somente no pico





# DIFERENÇA ENTRE RETURN E YIELD



# Return envia um valor especificado de volta para seu chamador, enquanto Yield pode produzir uma sequência de valores. Devemos usar o Yield quando queremos iterar em uma sequência, mas não queremos armazenar a sequência inteira na memória.

# O Yield é usado em geradores Python. Uma função geradora é definida como uma função normal, mas sempre que precisa gerar um valor, ela o faz com a palavra-chave Yield em vez de return. Se o corpo de um def contiver yield, a função se tornará automaticamente uma função geradora.



# Ele retorna um valor mantendo o estado de onde parou. Quando executa de novo ele continua de onde parou. Ele controla o estado de um enumerador entre execuções da função.


#OU SEJA O YIELD MANTEM O ESTADO, ELE EXECUTA APARTIR DE ONDE PAROU, NO CASO DO RETURN, ELE COMEÇARIA A EXECUÇÃO TODA DE NOVO


# vai pegando uma semente cada vez. Mas é com interrupções. O yield é um return, ele encerra a execução, ele interrompe. Mas o saco de sementes continua lá do jeito que você deixou. Não começa um saco novo toda vez que chamar, como ocorreria no return.