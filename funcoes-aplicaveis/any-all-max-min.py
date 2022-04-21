#  são funções já integradas no python

# todas tem a sintaxe parecida

# all(iteravel)  min(iteravel)  max(iteravel)  any(iteravel)



# ANY = retorna um booleano (retorna true se qualquer elemento do iteravel for True ) === nesse caso se houver elementos dentro do iteravel e nenhum deles for uma (lista, tupla , dicionario ou conjunto vazio) ou ter um valor false , VAI SEMPRE RETORNAR TRUE

#OBS EXISTINDO PELO MENOS 1 VALOR True A FUNÇÃO ANY VAI RETORNAR True

# elementos falsos = iteraveis vazios, 0 e False

# Iteravel vazio retorna false

# ex

listaAny = [1,2,3,4,5,56]

print(any(listaAny)) # True

listaVazia = [] # lista vazia (não possui nenhum elemento) [1,2,3,4,'ola', True ...]
tuplaVazia = () # tupla vaiza (não possui nenhum elemento) (1,2,3,4,'ola', True ...)
dicionarioVazio = {} # dicionario vazio (não possui chave nem valor) {"chave": valor, "chave2": valor2 ...}
conjuntoVazio = {} # conjunto vazio (não possui dados) {dado1, dado2, dado3...}

print(any(listaVazia)) # False
print(any(tuplaVazia)) # False
print(any(dicionarioVazio)) # False
print(any(conjuntoVazio)) # False


listaDados = [0,True] # True
listaDados2 = [0, False] # False
 
print(any(listaDados))
print(any(listaDados2))


numeros = [1,2,3,4,5,6]

generator = (num % 5 == 0 for num in numeros) #  gerando um generator testando se o resto da divisao do numero por 5 é igual a 0 no caso da lista 1,2,3,4,5 somente o 5 vai retornar True

for item in generator:
    print(item, end=', ') # False, False, False, False, True, False, False

print(any(generator)) # True # como existe pelo menos 1 valor True any vai retornar True






# all - parecido com any, porem ele só retornar True se todos os elementos do iteravel forem True
# OBS UM ITERAVEL VAZIO RETORNA TRUE
# ex:


listaAll = [True,True,True,True,True,False]

print(all(listaAll)) # False # retorna false porque o ultimo elemento da listaAll é False


listaAllNova = [True,True,True,True,True]

print(all(listaAllNova)) # True # retorna true pois todos elementos da lista são True


lisVazio = []
tupVazio = ()
dicVazio = {}
conjuntoVazio = {}

print(all(lisVazio)) # True
print(all(tupVazio)) # True
print(all(dicVazio)) # True
print(all(conjuntoVazio))  # True
# todos retornam true pois são iteraveis vazios


numPares = [2,4,6,8,10]

print(all(num % 2 == 0 for num in numPares)) # True # retorna True pois o generator (num % 2 == 0 for num in numPares) # retorna uma tupla de valores verdadeiros, ja  que todos os valores da lista numPares é par



# diferença entre all e any

# any só é true se e somente se pelo menos 1 elemento for True (dentro do iteravel) X all só é true se e somente se todos os elementos forem true (dentro do iteravel)




# MAX 

# retorna o maior valor de um iteravel, ou dos elementos passados como argumentos (somente valores numericos)

#ex

listaMaiores = [32,45153,213.23123,33423,55151,562345,12352357,12341,2341]

print(max(listaMaiores)) # 12352357 # o maior valor da listaMaiores é 12352357

dicionarioMaiores = {
    'azul':10,
    'preto':23,
    'castanho':42
}

print(max(dicionarioMaiores.values())) # 42 #  de todos os valores do dicionario (lembrando que dicionarios são compostos por chave -> valor) o 42 é o maior

def valores(*args):
    print(max(args)) # vamos usar como argumentos os elementos da listaMaiores
    
valores(32,45153,213.23123,33423,55151,562345,12352357,12341,2341) # 12352357



# MIN 

# retorna o menor valor de um iteravel, ou dos elementos passados como argumentos (somente valores numericos)

# ex

listaMenor = [1,2,3,4,5,56,1.2,0.4,0.2,-1,-23]

print(min(listaMenor)) # -23 # retorna o menor elemento dentro de listaMenor que no caso é o elemento de valor negativo (-23)


dicionarioMenor = {
    'lapis': 23,
    'cadernos':4,
    'canetas': 2
}

print(min(dicionarioMenor.values())) # 2 # retorna o menor valor dentre os values do dicionarioMenor



# max e min juntos


listaCompleta = [123,414,112,3,223,235,8,45,34623,12]

print(max(listaCompleta)) # 34623 # maior valor
print(min(listaCompleta)) # 3 # menor valor


# analisando tamanho de uma string com max e min usando lambda

alunos = ['pedro','lucas','isadora','camila','samuel']

print(max(alunos, key=lambda aluno: len(aluno))) # retorna a string com maior length # isadora

print(min(alunos, key=lambda aluno: len(aluno))) # retorna a string com menor length # pedro