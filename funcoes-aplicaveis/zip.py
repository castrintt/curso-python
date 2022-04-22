# zip - retorna um objeto zip, com elementos dos iteraveis passados como parametros.

# passamos no minimo 2 iteraveis (porem podemos passar quantos quisermos[contanto que seja maior que 2])

# OBS PODE SER USADO SOMENTE UMA VEZ, (ele guarda na memoria o valor do zip e após usado se perde o valor)

# retorna uma lista de tuplas 

# pode receber qualquer tipo de iteravel (lista,tupla,dicionario,conjunto)

# o tamanho do menor iteravel predomina

#ex

alunos = ['bianca','vitor','arial']

notas = 14,15,20

juntarTudo = zip(alunos, notas)

print(list(juntarTudo)) # [('bianca', 14), ('vitor', 15), ('arial', 20)] # retorna uma lista de tuplas

print(dict(juntarTudo)) # {'bianca': 14, 'vitor': 15, 'arial': 20} # transforma em chave valor

print(tuple(juntarTudo)) # (('bianca', 14), ('vitor', 15), ('arial', 20)) # transfoma tudo em uma tupla com tuplas



# ex 2

nome = ['matheus','igor','ribas','romulo']

idade = 24,23,23,22

valores = dict(zip(nome, idade))

print(valores) # {'matheus': 24, 'igor': 23, 'ribas': 23, 'romulo': 22} # dicionario com chave e valor

print(list(zip(nome,idade))) # [('matheus', 24), ('igor', 23), ('ribas', 23), ('romulo', 22)] lista de tuplas

print(tuple(zip(nome, idade))) # (('matheus', 24), ('igor', 23), ('ribas', 23), ('romulo', 22)) # tupla de tuplas

print(set(zip(nome,idade))) # {('igor', 23), ('ribas', 23), ('romulo', 22), ('matheus', 24)} # conjunto de tuplas


# ex 3 # podemos 'zipar' quantos iteraveis quisermos (e eles podem ser de qualquer tipo)

nomes = ['igor','matheus']

idades = 23,24

cidades = {'são paulo','uba'}

estados = {
    1:'Sp',
    2:'Mg'
}

# JUNTANDO TODOS OS VALORES (nomes, idades, cidades, estados) usando zip \/

# transformando em lista
print(list(zip(nomes,idades,cidades,estados))) # [('igor', 23, 'são paulo', 1), ('matheus', 24, 'uba', 2)] # lista de tuplas

#transformando em dicionario # não podemos transforma em dicionario caso passarmos mais de 2 parametros no zip(no caso mais de dois iteraveis) porque o dict funciona como chave -> valor (são 2 dados)
#print(dict(zip(nomes,idades,cidades,estados))) # ValueError: dictionary update sequence element #0 has length 4; 2 is required

#transformando em tupla
print(tuple(zip(nomes,idades,cidades,estados))) # (('igor', 23, 'são paulo', 1), ('matheus', 24, 'uba', 2)) # tupla de tuplas

#transformando em conjunto
print(set(zip(nomes,idades,cidades,estados))) # {('igor', 23, 'uba', 1), ('matheus', 24, 'são paulo', 2)}  # conjunto de tuplas




# ex 4 O MENOR PREDOMINA - significa que quando juntarmos os iteraveis usando o zip, oq predomina é o iteravel com menor len(), segue o exemplo abaixo

lista1 = ['isabela','valdinei','carlos','sami','celma']

lista2 = [1,2,3]

print(list(zip(lista1,lista2))) # [('isabela', 1), ('valdinei', 2), ('carlos', 3)]

# retornou uma lista com 3 tuplas somente MESMO QUE A LISTA1 TENHA 5 ELEMENTOS O ZIP SE ORIENTA PELO QUE TEM MENOS QUE NO CASO È A LISTA2 (com 3 elementos)
# por isso ele só retorna 3 tuplas usando os 3 primeiros elementos da lista1 e ignorando os 2 ultimos (a mais)



# ex 5 usando * (para descompactar) QUANDO PASSAMOS O * ANTES DE UM ITERAVEL ELE DESCOMPACTA O ITERAVEL (AULAS ANTERIORES), isso serve pra qualquer iteravel a não ser dicionarios

lugares = [('rs','sao paulo'),('pr','vitoria'),('am','sao luis')] # lista de tuplas

print(list(zip(*lugares))) # [('rs', 'pr', 'am'), ('sao paulo', 'vitoria', 'sao luis')] # criou uma lista de tuplas, sendo que a primeira tupla é composta por todos os valores [0] da tupla inicial, e a segunda tupla é composta por todos os valores [1] ta tupla incial

# lugares -> ('rs','sao paulo'),('pr','vitoria'),('am','sao luis')
# zip -> (rs,pr,am)  (sao paulo, vitoria, sao luiz)