# Nested functions == Funções dentro de funções
# a) Criar uma variavel do tipo função:
# Basta criar uma variavel que recebe uma função
# ex

def aniversariante(lista_nomes):
    for nome in lista_nomes:
        print(f'feliz aniversario {nome}')


aniversariante(['luca','vitoria'])


aniversario = aniversariante # não utilizar a sintaxe --> aniversario = aniversariante() pois assim vc esta chamando a função e nesse caso queremos simplismente fazer com que a variavel a receba, sem invoca-la

print(type(aniversario)) #<class 'function'>
# simples assim, agora a variavel aniversario é do tipo função 
# quando queremos criar variavel com tipo string, basta declarar uma string como dado da variavel, para interios, float e booelean é do mesmo jeito
# pois entao, só fizemos a mesma coisa porem com funções

# Para chamarmos agora a função basta declarar aniversario
#ex

# chamando a função armazenada em uma variavel

aniversario(['igor','isabela'])  # e pronto, simples

# feliz aniversario igor
# feliz aniversario isabela


# b) passando funções como parametros/argumentos

# ex

from random import randint as rd

def num_aleatorio():
    return rd(1,6)


def pessoa(funcao, nome):
    resultado = funcao()
    if resultado < 4:
        return str(resultado) + ' Finish ' + nome
    else:
        return str(resultado) + ' Vitoria perfeita ' + nome

print(pessoa(num_aleatorio,'maira')) # dessa forma passamos uma função como parametro
# lembrando que quando passamos a função (num_aleatorio) como parametro NÃO USAMOS A CHAMADA DELA função() e SIM  SOMENTE USAMOS SEU NOME --> função
# como segue no exemplo acima  print(pessoa(num_aleatorio,'maira')) # note que não houve a invocação da função num_aleatorio e sim só a sua chamada!
# não queremos passar a execução da função e sim somente passar seu nome

# POREM NÃO TOME COMO REGRA, pois sempre depende do programa, podemos sim fazer a chamada da função direto como parametro (no caso acima não)

# VEREMOS AGORA UM CASO ONDE USAREMOS A INVOCAÇÃO DA FUNÇÃO PARA EXECUÇÃO DE OUTRA

from random import choice as ch

def escolha():
    return ch(range(1,80))

def pessoa(funcao):
    if funcao < 18:
        print('Não pode entrar')
    elif funcao >= 18:
        print('pode entrar')

pessoa(escolha()) # nesse caso chamei a execução da funçao escolha, pois nela existe o retorno de uma escolha de um numero entre 1 e 80




# c) RETORNANDO A FUNÇÃO COMO PARAMETRO

# ex1

from random import randint as rand

def pessoa(nome):
    def num_aleatorio():
        return rand(1,6) # esse é o retorno da função num_aleatorio
    return f'{nome} Tirou {num_aleatorio()}'
    
print(pessoa('igor')) # igor Tirou 6 # um exemplo

# nesse caso queremos a execução da função num_aleatorio como parametro para o retorno da função pessoa

# LEMBRANDO QUE COMO A FUNÇÃO NUM_ALEATORIO() ESTA DENTRO DA FUNÇÃO PESSOA() NÃO PODEMOS CHAMAR A EXECUÇÃO DELA FORA

# ou seja --> executar num_aleatorio() retornaria um erro, ja que ela depende da execução de pessoa()


# ex 2 

from random import randint as rand

def pessoa():
    def num_aleatorio():
        return rand(1,6) 
    return num_aleatorio
    
print(pessoa()) # nesse caso ele simplismente vai me retornar a função em si # é basicamente o mesmo resultado de declarar uma função como dado de uma variavel
# porem dessa forma só retornamos a função em si, para executar ela devemos fazer com q ela seja atribuida a uma variavel
# dessa forma

definicao = pessoa() # devemos chamar ela pois ela esta retornando outra função, para assim depois invocarmos a variavel definicao como função
# como segue abaixo
print(definicao()) # 6 # retorna um valor, pois atribuimos a chamada de uma função a variavel, e essa chamada esta retornando outra função



# d) Parametros de funções externas, são reconhecidos dentro de funções internas

# ex

def pessoa(nome,idade):
    def drink(nome):
            return f'Vamos levar o drink a sua mesa senhor(a) {nome}'
    if idade > 18:
        print('Olá {nome} você esta liberado!')
        return drink(nome)
    else:
        print('Você não pode entrar')


variavel = pessoa

print(variavel('igor',23))  #o parametro nome foi passado como parametro para função drink
# Olá {nome} você esta liberado!
# Vamos levar o drink a sua mesa senhor(a) igor

# ex2

from random import randint as rd

def pessoa(nome):
    def num_aleatorio():
        return f'{nome} Tirou {rd(1,6)}' # passamos o nome (parametro da função pessoa() dentro da execução da função num_aleatorio())
    return num_aleatorio

funcao = pessoa('igor')

print(funcao()) # igor Tirou 4