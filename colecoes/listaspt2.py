#OUTRA MANEIRA DE ITERAR UMA LISTA SEM USAR FOR

import enum


listaNova = []

for numero in range(1,11):
    listaNova.append(numero)
    
print(listaNova) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#podemos fazer dessa forma

listaNova2 = list(range(1,11))

print(listaNova2) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



#percorrendo listas (iterar)

#for

lista2 = [1,2,3,4,5,6,7,8]

for elemento in lista2:
    print(elemento, end=" ") # 1 2 3 4 5 6 7 8
    
    
total = 0

for elemento in lista2:
    total = total + elemento 
    
print(total/len(lista2)) # 4.5 # media



#while

totalWhile = 0
contador = 0

while len(lista2) != 0:
    totalWhile +=  + lista2.pop()
    contador += 1
print(totalWhile/contador)  # 4.5 # media





#obtendo indices da lista usando enumerate  

#sintaxe

#for indice, item in enumerate(lista):
    #code 
    
#idice itera todos os indices da lista, e item itera todos os valores


jogos = ['it takes two','mario','sonic']

for indice, item in enumerate(jogos):
    print(item)
    print(indice)
    
    
    
#index - retorna o indice de um elemento, pode ser passado um segundo parametro para definir onde vai começar a buscar o indice
#pode ser passado 3 parametros tbm, (valor buscado, indice onde começa a buscar, indice onde finaliza a busca)

#sintaxe

#lista.index(valor dentro da lista)

games = ['mario','sonic','hercules','hades']


print(games.index("hercules")) # indice 2 # encontrou o indice informando o valor do elemento



num = [1,2,3,4,5,6,7,8,8,0,8,7]

print(num.index(7,7)) # 11  #procurando o indice do valor 7 a partir do indice 7, temos 2 numeros 7 um no indice 6 e outro no indice 11, como o segundo paramentro informou que devemos buscar o indice do 7 que está depois do indice 7, o primeiro 7 não foi "buscado" 


print(num.index(8, 9, 11)) # 10 # busca o valor 8 entre o indice 9 e 11
 
 
 
#descompactar listas

#lembrando que para descompactar uma lista em variaveis, o numero de variaveis deve ser igual ao len(lista), caso contrario retorna um erro
lista5 = ['girafa','preta',3]


animal , cor, numero = lista5
#ou seja estamos passando em ordem os valores dentro da lista 5 para as variaveis animal, cor e numero, ou seja, animal recebe o primeiro indice, cor recebe o segundo indice e numero recebe o terceiro indice, nessa ordem

print(animal) # girafa
print(cor) # preta
print(numero) # 3



#              FUNÇÕES UTEIS PARA TRABALHAR COM LISTAS


#1) sum - soma os valores da lista (int ou float)

lista6 = [1,2,3]

print(sum(lista6)) # 6

lista7 = [1,2.2,44,4.44]

print(sum(lista7)) # 51.64




# 2) max , min - pega o valor maximo e o valor minimo dentro de uma lista (int e float)

lista8 = [1,2,5,6,88,3,234]

print(max(lista8)) # 234 # maior valor dentro da lista
print(min(lista8)) # 1  # menor valor dentro da lista





# 3) round - arredonda para o numero mais proximo

listaPlana = [1.233212313212, 2.2131432532532534,112.12312431521]

print(round(listaPlana[0])) # 1 # arredondando o primeiro item da lista



# 4) obter o modulo de uma lista

 
listaPessimista = [-10,-11,-123]

print(abs(listaPessimista[0])) # 10 # pega o valor absoluto (modulo) do primeiro indice da lista

listaPositivo = []

for numero in listaPessimista:
    listaPositivo.append(abs(numero))
    
print(listaPositivo) # [10, 11, 123] # retorna os valores absolutos (modulo)


# 5) copiar uma lista

# 5.1) Deep copy - copia uma lista em outra, porem se for adicionado algo posteriormente na lista 'pai' a lista onde foi copiado não copia o valor, ou seja, DEEP COPY COPIA AS LISTAS E AS TORNAM INDEPENDENTES ENTRE SI, LOGO QUALQUER MODIFICAÇÃO EM UMA DAS LISTAS NÃO AFETA A OUTRA

lista9 = [1,2,3,4,5]

lista10 = lista9.copy()

print(lista10) # [1, 2, 3, 4, 5]

lista9.append(12)
print(lista10) # [1, 2, 3, 4, 5]
print(lista9) # [1, 2, 3, 4, 5, 12]


# 5.2) shallow copy - É UMA ATRIBUIÇÃO DE LISTAS, LOGO TUDO QUE FOR ALTERADO EM UMA DELAS AFETA A OUTRA

lista11 = [1,2,3,4,5]

lista12 = lista11 # só atribuimos a lista11 a lista12

print(lista12) # [1, 2, 3, 4, 5]

lista11.append(12)

print(lista12) # [1, 2, 3, 4, 5, 12]
print(lista11) # [1, 2, 3, 4, 5, 12]



#MATRIZES - são listas que contem listas (é nada mais nada menos que uma lista)

# cada lista interna a uma lista é uma linha da matriz


matriz = [[1,2,3], [12,123,22]] # matriz 2 x 3 (2 listas 3 items)


print(matriz[0]) # [1, 2, 3] # primeiro indice
print(matriz[1]) # [12, 123, 22] # segundo indice


print(matriz[0][0]) # 1 #primeiro indice da matriz e primeiro indice da lista 'filha'

#                ITERANDO UMA MATRIZ

for linha in matriz: # linha itera todos os valores de uma lista, nesse caso itera todas as listas dentro da matriz
    for item in linha: # item itera todos os elementos dentro de cada lista filha
        print(item , end=" ") # 1 2 3 12 123 22 # todos os itens dentro das listas filhas
        
        
#jogo da velha com matriz

matriz1 = [ ['','',''] , ['','',''] , ['','',''] ] 

print('\n')
print(matriz1[0])
print(matriz1[1])
print(matriz1[2])

# ['', '', '']
# ['', '', '']
# ['', '', '']



lp1 = int(input("digite a linha que quer jogar: ")) # 1  # linha 1
cp1 = int(input('digite a coluna quer quer jogar: ')) # 1 # coluna 1

matriz1[lp1][cp1] = 'x'

lp2 = int(input("digite a linha que quer jogar: ")) # 0 # linha 0
cp2 = int(input('digite a coluna quer quer jogar: ')) # 0 # coluna 0

matriz1[lp2][cp2] = '0'



for linha in matriz1:
    print(linha)

# ['0', '', '']
# ['', 'x', '']
# ['', '' , '']

