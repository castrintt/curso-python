# tuple comprehension


#Gerar um objeto generator a partir do processamento de uma coleção de dados.

#sintaxe : a sintaxe é a mesma do list comprehension , porem ao inves de colchetes, temos os parenteses QUE SÂO OBRIGATORIOS

#o objeto generator é perdido após sua iteração

#generatorsEx  = (operação / função ou elemento ----- for elemento in iteravel)


#ex

gene1 = (numero for numero in range(1,11)) # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


#usando condicionais

#if

lista1 = list(range(1,11))

maiores = (num for num in lista1 if num <= 5) # (1, 2, 3, 4, 5)


#else

lista2 = list(range(1,11))

nums = (num if num <= 5 else num * 10 for num in lista2) # (1, 2, 3, 4, 5, 60, 70, 80, 90, 100) # para num in lista retorne num se num <= 5 senão num * 10


#ex 2 

nomes = 'Pedro', 'Tiara', 'Lucas','Gustavo'

tuplaNomes = (nome * 2 if len(nome) == 5 else nome for nome in nomes) # (PedroPedro, TiaraTiara, LucasLucas, Gustavo)
#para nome in nomes faça , nome * 2 se len(nome) == 5, senao imprima o nome

# seria a mesma coisa que fazer o seguinte

listaNomes = []

for nome in nomes:
    if len(nome) == 5:
        listaNomes.append(nome * 2)
    else:
        listaNomes.append(nome)
        
print(listaNomes) # ['PedroPedro', 'TiaraTiara', 'LucasLucas', 'Gustavo']

tuplaNomes = tuple(listaNomes) # (PedroPedro, TiaraTiara, LucasLucas, Gustavo)




# MOSTRANDO QUE UM OBJETO GENERATOR SE PERDE DEPOIS DE UM USO


frutas = 'maçã','banana','mamao'

tuplaFrutas = (fruta * 2 if len(fruta) == 3 else fruta for fruta in frutas)

listaFrutas = list(tuplaFrutas)

print(listaFrutas) # ['maçã', 'banana', 'mamao']

listaFrutas2 = list(tuplaFrutas)
 
print(listaFrutas2) # []

# ou sejam logo após ser usado uma vez, ela se perde, por isso o retorno de print(listaFrutas2) é uma lista vazia