#exemplos de declaração de listas

lista = [] #lista vazia

lista1 = [1,2,3,4,5] #lista de numeros

lista2 = [True, False,True] #lista de booleanos

lista3 = ['tatu','girafa','elefante'] #lista de strings

lista4 = ['string',True, 1.2,1] #lista com varios tipos de dados





#              podemos tbm receber uma lista dentro de outra
#ex

lis = ['string', True,[1,2,3,4,5,6],'Outra string']
#como acessamos essa lista dentro de uma lista? e como acessamos um elemento dessa lista dentro de uma lista?

#1) acessando a lista

print(lis[2]) #[1, 2, 3, 4, 5, 6]

#2) acessando um elemento dela

print(lis[2][0]) #1 #primeiro valor (indice 0) da lista






#              criando uma lista a partir de variaveis

cor = 'preta'
temMao = True
numero = 2

listaDeElementos = [cor,temMao,numero]
print(listaDeElementos) #['preta', True, 2]





#       usando o comando list() - ele converte uma string em uma lista

#ex

lista5 = list('silvio santos 1898')

print(lista5,end=" ") #['s', 'i', 'l', 'v', 'i', 'o', ' ', 's', 'a', 'n', 't', 'o', 's', ' ', '1', '8', '9', '8'] 





#                  podemos concatenar varias listas em uma só, usando spread    operator * , dessa forma:
#ex

listaCores = ['azul','vermelho','preto']

listaNumeros = [1,2,3,4,5]

listaSpread = [*listaCores, *listaNumeros]

print(listaSpread) # ['azul', 'vermelho', 'preto', 1, 2, 3, 4, 5]



#                       FERRAMENTAS

# 1) append - adicona um elemento por vez na lista
#obs - adiciona o objeto que passamos

listaNumerica = [1,2,3]
listaNumerica.append(4)

print(listaNumerica) # [1, 2, 3, 4]

listaNumerica.append([1,2,3,4,5]) #adicionando uma lista 

print(listaNumerica) # [1, 2, 3, 4, [1, 2, 3, 4, 5]]



# 2) extend - adiciona multiplos elementos em uma lista, só aceita iteraveis, só recebe um argumentoq que é uma lista (iteravel)
#sintaxe

#lista.extend([valores para adicionar aqui])

#ex

listaNomes = ['igor','matheus']

listaNomes.extend(['maria','isabela','marcela']) # ['igor', 'matheus', 'maria', 'isabela', 'marcela']

print(listaNomes)


listaCompras = ['detergente','amendoin','pasta de dente']

listaCompras.extend(['panela de pressão','coca-cola','aspirador de pó'])

print(listaCompras) #['detergente', 'amendoin', 'pasta de dente', 'panela de pressão', 'coca-cola', 'aspirador de pó'] 



# 3) inserte - adiciona um valor em um determinado indice da lista, recebe dois argumentos: lista.insert(indice, item a ser adicionado)
#obs: não substitui o valor, só o posiciona a direita

#ex


roupas = ['blusa','boné']

roupas.insert(1, 'calça')

print(roupas) #['blusa', 'calça', 'boné'] #adiciona no indice 1 a string calça



listaRoupas = [['calça verao', 'blusa verao'],['calça outono', 'blusa outono']]

listaRoupas.insert(1,['calça inverno', 'blusa inverno'])

print(listaRoupas) # [['calça verao', 'blusa verao'], ['calça inverno', 'blusa inverno'], ['calça outono', 'blusa outono']] 



# 4) concatenar listas


listaParaJuntar1 = [1,2,3,4]

listaParaJuntar2 = ['a','b','c']


listasJuntas = listaParaJuntar1 + listaParaJuntar2 

print(listasJuntas) # [1, 2, 3, 4, 'a', 'b', 'c'] 

#seria a mesma coisa que usar a seguinte sintaxe

listaParaJuntar1.extend(listaParaJuntar2)

print(listaParaJuntar1) # [1, 2, 3, 4, 'a', 'b', 'c']




#5) converter strings em listas - usando o split - cria uma lista separando uma string por seus espaços em branco (' ') (padrao)
#ex


hey = 'ola bom dia!'

print(hey.split()) # ['ola', 'bom', 'dia!']

fraseModerna = 'hoje é um novo dia de um novo tempo, que começou'

print(fraseModerna.split()) #['hoje', 'é', 'um', 'novo', 'dia', 'de', 'um', 'novo', 'tempo,', 'que', 'começou'] 

#                 podemos passar o parametro de separação pelo split

print(fraseModerna.split(',')) # ['hoje é um novo dia de um novo tempo', ' que começou']




# 6) converter listas em strings usando join - cria uma string juntando os elementos de uma lista
#sintaxe

# 'parametro separador'.join(lista para ser convertida)

#ex

lista10 = ['silvio','santos','vem','ai']
 
print(' '.join(lista10)) # silvio santos vem ai #nesse caso estamos substituindo cada separador da lista (,) no caso a virgula, por espaços

#podemos fazer assim tbm

lista11 = ['1','2','3','4','5','6']

print('*'.join(lista11)) #1*2*3*4*5*6  #substituimos todas as virgulas por *





# 7) contar elementos numa lista usando len()
#sintaxe

# len(lista)

#ex


lista12 = [1,2,3,4,5,6,7,8,123123,123]

print(len(lista12)) # 10 #lista12 tem 10 elementos



# 8) verificar se um determinado elemento esta na lista

if 5 in lista12:
    print('o elemento 5 esta na lista lista12') #o elemento 5 esta na lista lista12
   
   
    
    
# 9) podemos fazer dessa forma tbm

print(5 in lista12) # True




# 10) podemos saber a quantidade de vezes que o valor se repete em uma lista usando count


lista13 = [1,2,3,4,5,1,1,1,7,8,9,1]

print(lista13.count(1)) # 5 # OU SEJA, O NUMERO 1 SE REPETE 5 VEZES NA LISTA

listaAlunos = ['igor','matheus','giorno giovanna','dio brando','jotaro','igor']

print(listaAlunos.count('igor')) # 2 # a string igor se repete 2 vezes na listaAlunos




# 11) podemos ordenar uma lista usando o metodo sort() retorna none caso voce atribua o valor a uma variavel


listaMaluca = [5,3,2,4,1]

print(listaMaluca)

listaMaluca.sort()

print(listaMaluca) # [1, 2, 3, 4, 5]


listaMalucaStrings = ['h','y','f','a','j','b']

listaMalucaStrings.sort()

print(listaMalucaStrings) # ['a', 'b', 'f', 'h', 'j', 'y'] #coloca em ordem alfabetica



# 12) inverter uma lista usando reverse 


lista14 = [1,2,3,4,5]

print(lista14) # [1, 2, 3, 4, 5]

lista14.reverse()

print(lista14) # [5, 4, 3, 2, 1] inverteu a ordem dos indices

#                  podemos inverter a ordem de uma lista usando o slicing tbm [::-1]
# sua sintaxe é          lista[ inicio : fim : passo ]
lista15 = [1,2,3,4,5,6,7]

print(lista15) # [1,2,3,4,5,6,7]

print(lista15[::-1]) # [7, 6, 5, 4, 3, 2, 1]

print(lista15[0:4:2]) # [1, 3] # ou seja, ir do indice 0 ao indice 4 pulando de 2 em 2


# 13) acessar elementos na lista

lista16 = [1,2,3,4,5,6]

print(lista16[5]) # 6 acessando o indice 5 que nesse caso é o ultimo item

print(lista16[-1]) # 6 , -1 acessa o ultimo elemento da lista

#                    usando for para acessar indices

lista17 = [1,2,3,4,5,6]

for item in range(0,4): # do indice 0 ao 3
    print(f'indice: {item}  valor: {lista17[item]}', end=", ") 
    # indice: 0  valor: 1, indice: 1  valor: 2, indice: 2  valor: 3, indice: 3  valor: 4,   
    
    
# 14) substituir um elemento de uma lista (praticamente da mesma forma que acessamos)

lista18 = [1,2,3]

print(lista18) # [1, 2, 3]

lista18[1] = 14 # saubstituindo o valor do indice 1 por 14

print(lista18) # [1, 14, 3]



# 15) remover elementos de uma lista usando pop() - remove e retorna o ultimo elemeneto de uma lista (o pop retorna o valor que foi retirado, ou seja, se voce salvar o pop em uma variavel ela guarda o valor returado)

# podemos passar parametros para ele tbm

lista19 = [1,2,3,4,5]

print(lista19) # [1, 2, 3, 4, 5]

lista19.pop()

print(lista19.pop()) # 5 - o pop retorna o valor que foi retirado, ou seja, se voce salvar o pop em uma variavel ela guarda o valor returado

print(lista19) # [1, 2, 3, 4] # foi retirado o ultimo indice com valor de 5


#passando parametros

lista20 = [1,2,3,4,5]

print(lista20) # [1, 2, 3, 4, 5]

lista20.pop(0)

print(lista20.pop(0))  # 1 , guardou o valor 1 retirado
 
print(lista20) # [2, 3, 4, 5]  #como passamos o parametro (0) no pop (pop(0)) ele retirou o elemento de indice 0





#16) repetir elementos de uma lista

lista21 = [1,2,3]

lista22 = lista21 * 5

print(lista22) # [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3] # repetiu os valores da lista21 5 vezes
 
 
 
 
 # 17) limpar uma lista usando clear - limpa os elementos da lista
 
 
lista23 = [True,1,213,24,5,1254,25,'igor','matheus',False]
 
print(lista23) # [True, 1, 213, 24, 5, 1254, 25, 'igor', 'matheus', False]

lista23.clear()

print(lista23) # [] # lista esta zerada agora
