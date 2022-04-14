# comparação de listas tuplas e dicionarios

# quando usar dicionario?
# - dicionarios são interessantes quando voce possui um conjunto de informações de um mesmo objeto ou pessoa

#ex:

# funcionarios:
#     paula, 27 anos, programadora
#     gabriel , 30 anos , engenheiro


#usando listas

funcionarios = []
func1 = list(['paula',27,'programadora'])
func2 = list(['gabriel',30,'engenheiro'])
funcionarios.append(func1)
funcionarios.append(func2)
print(funcionarios) # [['paula', 27, 'programadora'], ['gabriel', 30, 'engenheiro']]

 
# usando tuplas

funcionarioPaula = 'paula',27,'programadora'
funcionarioGabriel = 'gabriel',30,'engenheiro'
funcionarios2 = funcionarioGabriel + funcionarioPaula
print(funcionarios2) # ('gabriel', 30, 'engenheiro', 'paula', 27, 'programadora')


# usando um dicionario (como voce vera no exemplo podemos usar listas contendo dicionarios)

funcionarios3 = [
    {
        'nome':'paula',
        'idade': 27,
        'ocupaçao':'programadora'
    },
    {
        'nome':'gabriel',
        'idade': 30,
        'ocupaçao':'engenheiro'
    }
]
    


print(funcionarios3) # [{'nome': 'paula', 'idade': 27, 'ocupaçao': 'programadora'}, {'nome': 'gabriel', 'idade': 30, 'ocupacao': 'engenheiro'}]


for indice,funcionarios in enumerate(funcionarios3):
    print(funcionarios3[indice]['nome']) # temos todos os nomes
    print(funcionarios3[indice]['ocupaçao'])  # temos todas as ocupações
    print(funcionarios3[indice]['idade']) # temos todas idades
    
    
    
    
    
#                               FERRAMENTAS


# 1) METODO PARA LIMPAR DICIONARIOS USANDO O COMANDO CLEAR 
#OBS : ESSE METODO APENAS LIMPA O DICIONARIO, NÂO O EXCLUI


dicionario = {
    'Programando':'ideias'
}

print(dicionario) # {'Programando': 'ideias'}
dicionario.clear() #limpamos todos os dados dentro do dicionario
print(dicionario) # {}


# 2) shallow copy x deep copy

# 2.1) deep copy - cria 2 dicionarios independentes

dicionario1 = {'programador':'igor'}
dicionario2 = dicionario1.copy()

print(dicionario2) # {'programador': 'igor'}
print(dicionario1) # {'programador': 'igor'}

dicionario1['comida favorita'] = 'pizza'

print(dicionario2) # {'programador': 'igor'}
print(dicionario1) # {'programador': 'igor', 'comida favorita': 'pizza'}


# 2.2) shallow copy - cria duas copias dependentes entre si

dicionario3 = {'programador':'igor'}
dicionario4 = dicionario3

print(dicionario3) # {'programador': 'igor'}
print(dicionario4) # {'programador': 'igor'}

dicionario3['comida favorita'] = 'feijao'

print(dicionario3) # {'programador': 'igor', 'comida favorita': 'feijao'}
print(dicionario4) # {'programador': 'igor', 'comida favorita': 'feijao'}


# 3) podemos iterar dicionarios
# ex

personagem = {
    'nome':'rick',
    'funcao':'cientista',
    'neto':'morty'
}


# 3.1) iterando somente a chave

for chave in personagem:
    print(chave, end=', ')  # nome, funcao, neto, # dessa forma só iteramos as chaves, não os valores

# 3.2) iterando os elementos das chaves


for chave in personagem:
    print(personagem[chave], end=", ") # rick, cientista, morty,
  
  
    
# 4) metodo KEYS - retorna uma LISTA com as CHAVES

dicionario4 = {
    'nome':'igor',
    'idade':23
}

print(dicionario4.keys()) # dict_keys(['nome', 'idade'])

# 5)  metodo VALUES - imprime uma lista com os elementos (valor de cada chave)

dicionario5 = {
    'nome':'beliria',
    'idade':42,
    'profissao':'venda de intercambio'
}

print(dicionario5.values()) # dict_values(['beliria', 42, 'venda de intercambio'])




# 6) metodo items()  - retorna uma LISTA de TUPLAS com cada CHAVE e VALOR do dicionario

dicionario6 = {
    'assassino':'hannibal',
    'status': 'preso',
    'vivo': True
}

print(dicionario6.items()) # dict_items([('assassino', 'hannibal'), ('status', 'preso'), ('vivo', True)])

for item in dicionario6.items(): # itera todos os indices da lista criada, dessa forma temos acesso a todas as tuplas dentro da lista
    print(item, end=', ') # ('assassino', 'hannibal'), ('status', 'preso'), ('vivo', True)
print('\n')
    
for indice, item in dicionario6.items():
    print(indice, end=', ') # assassino, status, vivo, # retorna todas 'chaves'
    print(item, end=", ") # hannibal, preso, True, # retorna todos os valores
    
    
    
# 7) metodo len - retorna a 'largura' do dicionario - levando cada (chave - valor) como 1 

dicionario7 = {
    'nome':'igor',
    'idade': 23
}

print(len(dicionario7)) # 2 ()


# 8) metodo max, min e sum - valor maximo, valor minimo e soma

# APENAS ACEITAM DADOS NUMERICOS - float, int e complexos

dicionario8 = {
    'valor1':1,
    'valor2':2,
    'valor3':3
}

#usando o metodo values acessamos somente os elementos, não as chaves, com isso nesse caso como temos somente elementos numericos, conseguimos aplicar os metodos max, min e sum

print(max(dicionario8.values()))  # 3
 
print(min(dicionario8.values()))  # 1

print(sum(dicionario8.values()))  # 6




