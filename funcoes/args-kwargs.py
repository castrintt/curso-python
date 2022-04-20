# são parametros como quaisquer outros

# não são obrigatorios  (não exigem argumentos)

# seus nomes não importam, e sim o(s) asterisco(s) . # ex *batataa , **bode

# os nomes args e kwargs são apenas por conveções

# ajudam a evitar erros e tornam suas funções mais dinamicas

# ARGS GERAM UMA TUPLA (NAO PRECISAM SER NOMEADOS) - KWARGS GERAM UM DICIONARIO  (PRECISAM SER NOMEADOS)




# ARGS

# *args -  armazena os argumentos EXTRAS em uma tupla

# pense o seguinte, voce tem uma função com 3 argumentos, mas voce passa 5, nesse caso os 3 primeiros argumentos vao ser designados aos parametros obrigatorios e os outros 2 irao para uma tupla que o *args vai gerar

# ARGS NADA MAIS NADA MENOS SÂO OS PARAMETROS (PASSADOS A MAIS) GRAVADOS EM UMA TUPLA
# PODEMOS FAZER TUDO OQUE FAZEMOS COM TUPLAS COM ESSES ARGS
# ITERAR, SOMAR, PEGAR O VALOR MAXIMO E ETC



# ex 1

def cadastro(nome,idade,*args):
    print(f'nome: {nome}')
    print(f'idade: {idade}')
    print(args) # ('carpinteiro', 'lutador', 'garçom')


cadastro('agnaldo',87, 'carpinteiro','lutador','garçom')

        #'agnaldo'  e 87 fazem parte dos 2 parametros obrigatorios (nome e idade)
        
        #o restante são armazenados em *args
        
        
#ex 2 (podemos passar tbm, para função receber somente *args)

def media(*args):
    
    print(args) # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(sum(args)/len(args)) # 5.5
    

media(1,2,3,4,5,6,7,8,9,10) # 5.5, nesse caso pegamos a media de todos os args

# ex 3 - *args com coleção de dados

notas = [8, 9.7,2.3]

def nota(nota1,nota2,*args):
    print(nota1)
    print(nota2)
    print(args)
    for items in args:
        print(items)
        print(items[1])

nota(1,2,notas)

# 1
# 2
# ([8, 9.7, 2.3],) # returna uma lista dentro como primeiro elemento de uma tupla
# [8, 9.7, 2.3] # iterando args retorna os items dentro da tupla, nesse caso um elemento(uma lista)
# 9.7 # acessando o elemento de indice 1 da lista dentro da tupla (args)





# DESCOMPACTANDO ARGS NA CHAMADA DA FUNÇÂO
# sintaxe: lista = [1,2,3,4]
# chamada_da_funcao(*lista)

# O ASTERISCO DENTRO NO ARGUMENTO (NA CHAMADA DA FUNÇÂO) INFORMA QUE DEVE HAVER UM DESCOMPACTAMENTO DA COLEÇÂO DE DADOS:  # listas, tuplas e conjuntos # antes que sejam enviados para a função



notasAlunos = [1,2,3,4,56,6,7,78,2]

def somaNotas(*args):
    print(args) # (1, 2, 3, 4, 56, 6, 7, 78, 2)
    print(sum(args)) # 159
    
somaNotas(*notasAlunos) # 159 # usando o asterisco dentro da chamada da função, estamos dizendo para o python que ele precisa desestruturar os itens da variavel passada, no caso uma lista, logo ele separa todos os items

# tanto q em print(args) dentro da função somaNotas ele retornou os items dentro de uma tupla e não uma tupla com um elemento como lista





# KWARGS

# armazena argumentos EXTRAS E NOMEADOS em um dicionario (diferente de *args, que alem de não precisar ser nomeado são armazenados dentro de uma tupla)

# LEMBRANDO QUE KWARGS USAM A SINTAXE DE 2 ASTERISCOS E ARGS UM

# PARA PASSARMOS OS KWARGS PRECISAMOS USAR A MESMA SINTAXE DE UM DICT - passando chave e valor

# ex 1

def idades(**kwargs):
    print(kwargs) # {'maria': 20, 'isadora': 20, 'igor': 23, 'isabela': 17} # retorna um dicionario
    for nome, idade in kwargs.items():
        print(f'nome: {nome} idade: {idade}')
        # nome: maria idade: 20
        # nome: isadora idade: 20
        # nome: igor idade: 23
        # nome: isabela idade: 17
        

idades(maria=20,isadora=20,igor=23,isabela=17)



# ex 2

def jogadas(nome, **kwargs):
    print(kwargs) # {'j1': 9, 'j2': 9, 'j3': 1} # {'j1': 10, 'j2': 40, 'j3': 1}
    for jogada in kwargs:
        print(jogada,end=', ') # j1, j2, j3 # j1, j2, j3
        if kwargs[jogada] == 10:
            return f'{nome} ganhou'
    print(f'{nome} Perdeu!')
    

print(jogadas('igor',j1=9,j2=9,j3=1)) # igor Perdeu! # ou seja, nenhum dos valores é igual a 10

print(jogadas('matheus',j1=10,j2=40,j3=1)) # matheus ganhou



# DESCOMPACTANDO KWARGS NA CHAMADA DA FUNÇÂO

# ex de **kwargs passando como parametro um dicionario

# DA MESMA FORMA QUE ARGS DEVEM PASSAR * (ASTERISCO) PARA PASSAR UM PARAMETRO COMO (LISTA< TUPLA OU CONJUNTO) NA CHAMADA DA FUNÇÂO, KWARGS TBM DEVEM PASSAR, POREM PASSAM 2 * (ASTERISCOS)
# sintaxe : dicionario = {'nome':'igor', 'idade':23}
# chamada_da_funcao(**dicionario)

dicionario = {'igor': 80, 'isabela': 90, 'maria': 20, 'estela': 49}

def apresentarNotas(**kwargs):
    print(kwargs) # 
    for chave, valor in kwargs.items():
        print(f'chave: {chave} // valor: {valor}')
        
        
apresentarNotas(**dicionario) # 

# {'igor': 80, 'isabela': 90, 'maria': 20, 'estela': 49} 
# chave: igor // valor: 80
# chave: isabela // valor: 90
# chave: maria // valor: 20
# chave: estela // valor: 49










# PASSANDO UM DICIONARIO COMO PARAMETRO SEM PASSAR *KWARGS

def apresenta(joao,carlos,jessica):
    print(f'joao {joao}, carlos {carlos} e jessica {jessica}')
    
notass = {
    'joao':23,
    'carlos': 24,
    'jessica': 42
}
 
apresenta(**notass) # joao 23, carlos 24 e jessica 42

# devemos passar com os 2 asteriscos tbm caso contrario recebe erro






# ORDEM DE UTILIZAÇÂO ARGS E KWARGS


# CORRETA - def função (parametros obrigatorios, *args, default, **kwargs)

#ex

def correta(nome, *args, cidade='curitiba',**kwargs):
    print(nome)
    print(args)
    print(cidade)
    print(kwargs)


telefones = ['908901283','1290381290321','12389012931']

dados = {
    'dado':True,
    'dado2': False,
    'dado3': True
}
    
correta('igor',*telefones,**dados)

# igor
# ('908901283', '1290381290321', '12389012931')
# curitiba
# {'dado': True, 'dado2': False, 'dado3': True}

# Veja que por estar na ordem correta, o python ignora o argumenta passado como default (cidade) e ja passa para a **kwarg


