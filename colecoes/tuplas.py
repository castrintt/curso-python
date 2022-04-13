#Tuplas

## SÃO PARECIDAS COM LISTAS

# tuplas possuem duas diferenças das listas

# 1) não é possivel remover ou adicionar elementos em uma tupla, apenas sobrescrever


# 2) sintaxe , enquanto as listas tem a sintaxe de colchetes [ ] , as tuplas tem sintaxe de parenteses ( ) obs: PARENTESES NÂO SÂO OBRIGATORIOS, MAS A SEPARAÇÂO POR VURGUÇA SIM!


#sintaxe

from re import T


tuplaExemplo = ('elemento1', 'elemento2','elemento3') # etc...

# podemos tbm separar por virgula, sem usar os parenteses ex::

tuplaExemplo2 = 'elemento1', 'elemento2', 'elemento3' # etc...


# 3) a virgula para separar elementos é OBRIGATORIA

# 4) a forma de acessar uma tupla é identica a forma de acessar uma lista

tuplaEx = 1,2,3,4,5

print(tuplaEx[0]) # 1  # acessamos o valor do primeiro elemento

for indice in range(1,3): # de 1 a 2
    print(tuplaEx[indice], end=" ") # 2 3 




#                      CARACTERISTICAS

# 1) tuplas podem ter diferentes tipos de dados tbm
tuplaExemplo3 = 'ola mundo',1,1.1,'dois'


# 2) tuplas não aceitam alteração nos valores

# 2.1) podemos criar listas dentro de uma tupla , e listas aceitam alterações

tuplaList = ([1,2,3], [1,2,3,4,5], [1,3,4,5,6,7,8])

# e listas são mutaveis, então podemos acessar algum valor dentro de uma das listas e alterar eles
#ex

tuplaList[0][0] = 0 # alteramos o primeiro valor da lista indice ( 0 ) no caso a primeira lista.


print(tuplaList) # ([0, 2, 3], [1, 2, 3, 4, 5], [1, 3, 4, 5, 6, 7, 8])


# 3) ao inves de usar o comando list(parametro para criar uma lista) para criar uma lista, com tuplas usamos o comando tuple(parametro para criar uma tupla)

#obs: para criar varios elementos dentro de uma tupla usando tuple(parametro), devemos identar por meio de um array (lista)

#ex

tupla7 = tuple(range(1,11)) # criamos uma tupla de numeros do 1 ao 10

print(tupla7) # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) 

tupla8 = tuple([1,2,3,4,'igor',True, 5j, 3.22]) # podemos criar uma tupla com diferentes tipos de dados tbm, lembrando de sempre identar dentro de uma lista 

print(tupla8) # (1,2,3,4,'igor',True, 5j, 3.22)



# 4) podemos criar tuplas filhas de tuplas tbm

#ex

tupla9 = tuple([(1,2,3), 1,2,3,4,(8,9,0)])

print(tupla9) # ((1, 2, 3), 1, 2, 3, 4, (8, 9, 0))


# 4.1) acessamos essas tuplas filhas da mesma forma q listas filhas

#ex

tupla10 = tuple([(1,2,3),(4,5,6),(7,8,9),1,2,3])

print(tupla10) # ((1, 2, 3), (4, 5, 6), (7, 8, 9),1,2,3)


print(tupla10[0][-1]) # 3 # acessamos o ultimo elemento da tupla primeira tupla fillha




#                   FERRAMENTAS QUE PODEMOS USAR EM TUPLAS (LEMBRANDO QUE ALGUMAS DELAS SÃO IDENTICAS AS FERRAMENTAS DE LISTAS, TIRANDO SOMENTE REMOÇÃO E ADIÇÃO DE ELEMENTOS)


# 1) CONCATENAR TUPLAS

tupla11 = tuple([1,2,3,4]) # tupla de 1 a 4

tupla12 = tuple(range(5,11)) # tupla de 5 a 10

print(tupla11) # (1, 2, 3, 4)

print(tupla12) # (5, 6, 7, 8, 9, 10)


tupla13 = tupla11 + tupla12 

print(tupla13) # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)



# 1.1) podemos fazer dessa forma tbm

tupla11 = tupla11 + tupla12 

print(tupla11) # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) 

#nesse caso a tupla11 foi apagada e outra tupla11 foi feita em seu lugar


# 2) VERIFICAR SE UM VALOR ESTA DENTRO DA TUPLA
 
 
tupla14 = 1,2,3,4,5

print(4 in tupla14) # True # o valor 4 esta na tupla14


# 3) OBTER A QUANTIDADE DE VEZES QUE UM ELEMENTO SE REPETE NUMA TUPLA


tupla15 = 1,1,1,1,1,1,1,2,3,4,5,6,3,2,3

print(tupla15.count(1)) # 7 # numero 1 se repete 7 vezes na tupla15


# 4) slicing (inverter a ordem) 
# # lembrando que a sintaxe completa é assim: [indice inicial:indice final:pulando de tantas em tantas casas]


tupla16 = 1,2,3,4,5

print(tupla16[::-1]) # (5, 4, 3, 2, 1)



# 5) iterar tuplas

#a iteração se da da mesma forma que a lista

# 5.1) for

tupla17 = tuple(range(1,11))

for elemento in tupla17:
    print(elemento, end=" ") # 1 2 3 4 5 6 7 8 9 10

print(sum(tupla17)/len(tupla17)) # 5.5 # media dos elementos



# 5.2) while 

tupla18 = tuple(range(1,21))

contador = 0 

while contador <= 19:
    print(tupla18[contador], end=" ") # 1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 
    contador += 1


print(sum(tupla18)/len(tupla18)) # 10.5 # media



# 6) obtendo indice de um elemento de uma tupla


tupla19 = ['igor','matheus','dolan','lodinho']


print(tupla19.index('dolan')) # 2 # indice da string 'dolan'



tupla20 = ['amarelo','vermelho','preto','azul','marrom']


for indice, cores in enumerate(tupla20):
    print(f'{indice} - {cores}', end="/ ") #  0 - amarelo/ 1 - vermelho/ 2 - preto/ 3 - azul/ 4 - marrom/


tupla21 = ['amarelo','azul','verde','preto','amarelo','rosa','verde','preto']

print(tupla21.index('amarelo')) # 0

print(tupla21.index('verde',3)) # 6 # procura o indice de 'verde' a partir do indice 3

print(tupla21.index('verde',3,7)) # 6 # procura o indice de 'verde' a partir do indice 3 até o indice 7


# 7) DESCOMPACTANDO TUPLAS

#SEMPRE SEPARE AS DESCOMPACTAÇÕES POR VIRGULA.

#OBS: PARA NAO RETORNAR ERRO, A QUANTIDADE DE ELEMENTOS QUE ESTAO SEPARADOS POR VIRGULA NA ESQUERDA TEM QUE SER IDENTICO AOS DA DIREITA (NOMENCLATURA / VALOR)

esporte, frutas,cores = ('futebol','surf'),('mamao','banana'),('preto','amarelo')

print(esporte) # ('futebol', 'surf')

print(frutas) # ('mamao', 'banana')

print(cores) # ('preto', 'amarelo')


#é identico para listas

esp, frut, cors = ['futebol','surf'],['mamao','banana'],['preto','amarelo']

print(esp) # ['futebol', 'surf']

print(frut) # ['mamao', 'banana']

print(cors) # ['preto', 'amarelo']


# mesma coisa para variaveis simples

nume, letraa, booleanoo = 1, 'a',True

print(nume) # 1

print(letraa) # a

print(booleanoo) # True


# 7.1) podemos fazer assim para tuplas e listas tbm

#os indices da tupla vao ser direcionados como valor para as variaveis, logo o len(tupla22) devera ser identico a quantidade de declarações

tupla22 = (('igor','matheus'),30000,('la casa de papel','o ultimo soldado'))


amigos, dinheiro, filmes = tupla22


print(amigos) # ('igor', 'matheus')

print(dinheiro) # 30000

print(filmes) # ('la casa de papel', 'o ultimo soldado')



#             FUNÇÔES ÚTEIS PARA TRABALHAR COM TUPLAS (E LISTAS TBM)

# 1) SOMA (SOMENTE PARA INTEIROS E FLUTUANTES)

tupla23 = 1,2,3,4,5


print(sum(tupla23)) # 15 # soma os valores das tuplas


# 2) MAX E MIN (SOMENTE PARA INTEIROS E FLUTUANTES)


tupla24 = 1,4,34534,234,123,123,234,1222,1,3,4,5,6,7,8


print(max(tupla24)) # 34534 # pega o maior valor dentro da tupla

print(min(tupla24)) # 1 # pega o menor valor dentro da tupla


# 3) LEN (PARA QUALQUER TIPO DE DADO)

tupla25 = 1,21,324,5,6,57,55,2,3,3223343,233


print(len(tupla25)) # 11 # quantos elementos tem dentro da tupla (largura da tupla)


# 4) COPIAR UMA TUPLA 
# OBS: (A SINTAXE È IDENTICA A SHALLOW COPY, MAS AS TUPLAS SÂO SEMPRE INDEPENDENTES)


tupla26 = 2,4,5566,123

tupla27 = tupla26


print(tupla26) # (2, 4, 5566, 123)

print(tupla27) # (2, 4, 5566, 123) 
#ambas são iguais,mas nenhuma delas depende da outra









#                     QUANDO USAR UMA TUPLA?


	# QUANDO NÃO FOR NECESSARIO TER MODIFICAÇÕES NOS DADOS




#            EXEMPLOS DE ALGUMAS FORMAS DE DECLARAR TUPLAS

 
# 1)  #entre parenteses, separados por virgula

tupla1 = (1,2,3,4,5) 
print(type(tupla1)) # <class 'tuple'>

# 2)  # sem parenteses separados por virgula

tupla2 = 1,2,3,4,5  
print(type(tupla2)) # <class 'tuple'>

# 3) # declaramos um unico valor imutavel dentro do parenteses e separado por virgula (o simples fato de separar esse dado por virgula ja o torna imutavel)


tupla3 = (1,)  
print(type(tupla3)) # <class 'tuple'>


# 4) # declaramos um unico valor imutavel sem parenteses e separado por virgula, dessa forma temos um unico dado imutavel 

tupla4 = 1, 
print(type(tupla4)) # <class 'tuple'>

#todas são tuplas!



#                                OBS:


#LEMBRANDO AS TUPLAS DEVEM SER SEPARADAS POR VIRGULAS, INDEPENDENTE DE HAVER SOMENTE 1 VALOR

tupla5 = 1,

tupla6 = 1

print(type(tupla5)) # <class 'tuple'>

print(type(tupla6)) # <class 'int'>




#                vantagem de se usar uma tupla

# 1) dados são mais seguros, já que você não pode adicionar ou remover dados.


# 2) processamento de tuplas são mais rapidas do que listas


# 3) em tuplas não existe o shallow copy ( que são as copias onde as 'listas' se tornam dependentes, sempre que ocorrer uma mudança em uma ocorrerá na outra) , as tuplas são sempre independentes.


