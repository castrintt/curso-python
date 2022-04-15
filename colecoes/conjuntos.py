# Caracteristicas de conjuntos:

# 1) não são ordenados.

# 2) não aceitam elementos repetidos

# 3) são representados por chaves {} , POREM NÂO SÂO REPRESENTADOS POR CHAVE -> VALOR




#  QUAL A VANTAGEM DE USAR CONJUNTOS ??

# 1) apresentam formas otimizadas de realizar funções especificas que só ele possui





#  Quando utilizar ?

# 1) - São utilizados quando você não precisa se preocupar com ordenação e repetição de elementos.



# COMO DECLARAR

# 1) declararando a variavel, ela recebe uma chave com dados separados por virgula

# sintaxe --  conjunto = { dado1, dado2, dado3 ... } 

conjunto = {1,2,3,4,5,6}

print(type(conjunto)) # <class 'set'>

# 1.1) lembrando que conjuntos não aceitam valores repetidos
# ex

conjunto1 = {1,2,3,4,5,5,5,5,5,5,5}

print(conjunto1) # {1, 2, 3, 4, 5} # não ira retornar um erro, mas qualquer valor repetido é ignorado (para ficar mais facil de visualizar é só entender que qualquer dado que no conjunto.count(dado) > 1 ele não vai se repetir)




# 2) usando a função set()
# sintaxe ---  conkunto = set(iteravel) ( tem que ser um iteravel, no caso uma lista, tupla ou dict )
#ex


# lista
lista = list(range(1,20))

conjunto2 = set(lista)

print(conjunto2) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}


#tupla
tupla = tuple(range(1, 20))

conjunto3 = set(tupla)

print(conjunto3) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}


#dicionario
dicionario = dict(nome='igor',idade=23,profissao='programador')

conjunto4 = set(dicionario.keys())

print(conjunto4)  # {'profissao', 'idade', 'nome'} # itera e salva as chaves

conjunto5 = set(dicionario.values())

print(conjunto5) # {'igor', 'programador', 23} # itera e salva os valores

conjunto6 = set(dicionario.items())

print(conjunto6) # {('idade', 23), ('profissao', 'programador'), ('nome', 'igor')}  # transforma chave -> valor em uma tupla , itera e salva.

conj = set([1,2,3,4,5,6])
print(conj) # {1, 2, 3, 4, 5, 6}




#  CONJUNTOS TBM SÂO ITERAVEIS

#ex

conjunto7 = {1,2,3,4,5,6,7}

for num in conjunto7:
    print(num, end=", ") # 1, 2, 3, 4, 5, 6, 7
    
    
    
#         FERRAMENTAS

# 1) adicionar elementos dentro de um conjunto  - usando o comando add()
# conjunto.add(elemento a ser adicionado)

# ex

esportes = {'futebol','volei','natação'}

print(esportes)

esportes.add('Futvolei') # {'volei', 'natação', 'futebol'}

print(esportes) # {'volei', 'Futvolei', 'natação', 'futebol'}


# 2) remover elementos do conjunto


# 2.1) forma mais comum - usando remove() 
# conjunto.remove(elemento que quero retirar)

#OBS: o metodo remove não retorna o elemento retirado, como o metodo pop.() em listas faz


conjunto8 = {1,3,5,7,9,11}

print(conjunto8) # {1, 3, 5, 7, 9, 11}

conjunto8.remove(7) # removemos o elemento 7 dentro de conjunto 8

print(conjunto8) # {1, 3, 5, 9, 11}



conjunto9 = {'igor',True,23}

print(conjunto9) # {True, 'igor', 23}

conjunto9.remove(True)

print(conjunto9) # {'igor', 23}


# 2.2) metodo discard() - faz exatamente a mesma coisa que o remove
# conjunto.discard(elemento que quer remover)

conjunto10 = {'igor','matheus','ribas'}

print(conjunto10) # {'matheus', 'igor', 'ribas'}

conjunto10.discard('matheus')

print(conjunto10)  # {'igor', 'ribas'}



# 2.3) metodo pop - remove o elemento porem retorna o elemento retirado
# conjunto.pop() - nesse caso não necessida de argumento, ele irá remover um valor arbitrario ( ja que sets não possuem ordenação )
conjunto11 = {1,2,3,4,5,6,7}

conjunto11.pop() 

print(conjunto11) # {2, 3, 4, 5, 6, 7}

conjunto11.pop()

print(conjunto11) # {3, 4, 5, 6, 7}




conjuntoNomes = {'igor','matheus','ribas'}

elementoRetirado = conjuntoNomes.pop()

print(elementoRetirado) # igor
print(conjuntoNomes) # {'ribas', 'matheus'}



# 2.4) usando metodo clear() -- porem nesse caso voce limpa o conjunto, e não o exclui, ou seja retorna um conjunto vazio
# conjunto.clear()


conjunto12 = {1,23,4,5,6,67,7}

print(conjunto12) # {1, 67, 4, 5, 6, 7, 23}

conjunto12.clear()

print(conjunto12) # set() - # retorna um set vazio (conjunto vazio)




# 3) possui o metodo len() que é a 'largura' do conjunto
# len(conjunto)

conjunto13 = {1,2,3,4,5,6,7}

print(len(conjunto13)) # 7 # possui 7 elementos dentro do conjunto 13



# 4) intersecção de conjuntos ( basicamente mostra os valores que se repetem em 2 ou mais conjuntos ) --  intersection()
#conjunto1.intersection(conjunto2)


conjunto14 = {1,2,3,4,5,6}

conjunto15 = {1,2,6,7,8,9,90}

print(conjunto14.intersection(conjunto15))# {1, 2, 6}  # retorna os valores que se repetem nos 2



# 5) unir conjuntos -  comando union()
# conjunto 3 = conjunto1.union(conjunto2)

conjunto16 = {1,2,3}

conjunto17 = {4,5,6}

conjunto18 = conjunto16.union(conjunto17)

print(conjunto18) # {1, 2, 3, 4, 5, 6} # uniu os dois conjuntos


# 5.1) pode ser feito assim tbm


conjunto19 = {1,2,3}

print(conjunto19) # {1, 2, 3}

conjunto20 = {4,5,6}

conjunto19 = conjunto19.union(conjunto20)

print(conjunto19) # {1, 2, 3, 4, 5, 6}





# 6) diferença entre conjuntos ( mostra oque não se repete ) - metodo difference()
# conjunto3 = conjunto1.difference(conjunto2) ( basicamente isso -- conjunto1 - conjunto2 )


conjunto21 = {1,2,3,4,5,6,7,8,9,10}

conjunto22 = {2,4,7,9}

conjunto23 = conjunto21.difference(conjunto22)

print(conjunto23) # {1, 3, 5, 6, 8, 10} # retorna os valores que não se repetem (nesse caso que estão em conjunto21 e não estao no conjutno22)




# 7) deep copy e shallow copy

# 7.1) deep copy - criam 2 conjuntos independentes

conjunto24 = {1,2,3,4}

conjunto25 = conjunto24.copy()

print(conjunto25) # {1, 2, 3, 4}

conjunto24.add(5)

print(conjunto24) #  {1, 2, 3, 4, 5}
print(conjunto25) # {1, 2, 3, 4}



# 7.2) shallow copy - cria 2 conjuntos dependentes


conjunto26 = {1,2,3,4}

conjunto27 = conjunto26 

print(conjunto27) # {1, 2, 3, 4}

conjunto26.add(5)

print(conjunto26) # {1, 2, 3, 4, 5}
print(conjunto27) # {1, 2, 3, 4, 5}



# 8) max min e sum -- ( SOMENTE PARA VALORES NUMERICOS )


conjunto28 = {1,2,3}

print(max(conjunto28)) # 3 # maior valor

print(min(conjunto28)) # 1 # menor valor

print(sum(conjunto28)) # 6 # soma dos valores