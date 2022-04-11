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