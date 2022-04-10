#loop for

#se repete varias vezes

#utilizamos o loop para repetir diversas vezes a mesma tarefa

#temos o for e while, nessa seção iremos ver o for

#for -- significa (para)

#sintaxe

for item in sequencia:
    
#para cada item dentro de uma sequencia faça:

		#processo


#A SEQUENCIA DEVE SER SEMPRE ITERAVEL

#ITERAR - conjunto de dados que podem ser dismembradps ou percorridos

#exemplos de dados 

#1) strings - pode ser desmembrado por caracteres

#'filmes' - 'f' , 'i' , 'l' , 'm' , 'e' e 's'

#podemos usar indice para acessar as posições

#ex

 name = 'igor'

print(name[1]) # g

print(name[-3]) # g
#podemos acessar dessas 2 formas
# i g o r
# 0 1 2 3
# -4 -3 -2 -1

#2) listas, tuplas , dicionarios e sets(conjuntos)

#lista = [1,2,3,4] #varios tipos de dados

#3) range():

#função que cria um intervalo de numeros escolhidos pelo usuario

#sintaxe

#range(numero que deseja começar, numero que deseja finalizar + 1)

numeros = range(1,11) # sequencia de numeros de 1 a 10
for numero in numeros:
     print(numero, end=" ") #1 2 3 4 5 6 7 8 9 10

#brincando um pouco com range e slice

numeros = range(1,11)

num = numeros[0:5]

print(num) #range(1, 6)

for item in num:
    print(item) #1 2 3 4 5   


#por padrao o print tem essa sintaxe por debaixo dos panos

#print(oque quer printar, end="\n")

#ou seja a cada print pula uma linha

#3.1) temos outra forma de fazer a sintaxe do range()

#ex

num = range(10) #por default o python pega o 0 como inicial

for item in num:
		print(item, end=" ") #0 1 2 3 4 5 6 7 8 9

#3.2) outra forma de escrever o range() é com um terceiro parametro
#que simula quantos passos quer dar

#ex

num = range(0,21,2)  # cria uma lista do 0 ao 20 que "pula" de 2 em 2

for item in num:
    print(item, end=" ") #0 2 4 6 8 10 12 14 16 18 20

#concluindo range() com exemplo das 3 formas de escrever

#ex 1

numeros = range(0,11) # lista de 0 a 10

for item in numeros: 
    print(item, end=" ") #0 1 2 3 4 5 6 7 8 9 10 
     

#ex2

numeros2 = range(11) # lista de 0 a 10, default ja é o 0

for item in numeros2:
    print(item, end=" ") #0 1 2 3 4 5 6 7 8 9 10 
    
    
#ex3

numeros3 = range(0,11,2) # lista de 0 a 10 que vai de 2 em 2

for item in numeros3:
    print(item, end=" ") #0 2 4 6 8 10

#complemento

numeros4 = range(10,0,-2) #lista de 10 a 0 que pula de 2 em 2 começando do final da lista

for item in numeros4:
    print(item, end=" ") #10 8 6 4 2


#4) podemos colocar condicionais dentro do loop

num = range(2,20)# lista de 2 a 19

for item in num: 
    if item % 2 == 0: # quero todos os numeros dentro da lista que são pares
        print(item,end=" ") #2 4 6 8 10 12 14 16 18

#ex mais complexo

fruta = 'abacate'

numeros = range(1,4) #lista d e 1 a 3
for letra in fruta: #itera todos as letras de abacate
    if letra == 'a': # para todas as letras 'a' da palavra iterada faça
        for num in numeros: #iteramos 3 numeros 1, 2, 3 (loop de 3 passagens)
            print('achei a letra a')
            
            #imprime 3 vezes (range(1,4)) achei a letra a para cada 'a' encontrado no loop, ou seja, imprime 9 vezes, pois 'abacate' tem 3 letras 'a'

#5) para sair de um loop podemos usar a palavra reservada break

#ex

alfabeto = 'abcdefghijklmnopkrstuvxwyz'

for letra in alfabeto: # passa por todas letras na string
    print(letra , end=" ")
    if letra == 'k':  
        break # saimos do loop
    
    # a b c d e f g h i j k

#6) prosseguir o loop utilizamos a palavra continue(prosseguir)

#ex

alfabeto = 'abcdefghijklmnopkrstuvxwyz'

for letra in alfabeto: # passa por todas letras na string
    print(letra , end=" ")
    if letra == 'k':  
        continue #continua o loop
    
    #a b c d e f g h i j k l m n o p k r s t u v x w y z

#7) metodo enumerate

#função que adiciona um contador a cada elemento dentro da sequencia

#ex

heroi = 'batman'

for valor in enumerate(heroi):
    print(valor, end=" ") #(0, 'b') (1, 'a') (2, 't') (3, 'm') (4, 'a') (5, 'n')
    
# pode ser feito passando dois parametros no for tbm

nome = 'igor'

for letra, indice in enumerate(nome):
    print(f' {letra} , {indice}', end=" ") # 0 , i   1 , g    2 , o    3 , r
    
    
    
numer = range(0,11)

for num,indice in enumerate(numer):
    print(f'{num} - {indice}', end=" ") #  0 - 0   1 - 1   2 - 2   3 - 3   4 - 4  5 - 5  6 - 6   7 - 7   8 - 8   9 - 9   10 - 10 
    