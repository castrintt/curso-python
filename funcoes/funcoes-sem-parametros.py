# são blocos de codigos que irão executar uma tarefa especifica podendo ser repetida

# OBS: funções devem ser declaradas e invocadas

# tem função de diminuir o programa , facilitar o gerenciamento e organizar

# São declaradas após os comentarios iniciais e imports(se houver)

# Já estudamos algumas funções como print, input e type por exemplo

# podemos criar nossas proprias funções

# DECLARAÇÂO

# utilizamos a palavra reservada       def   para declarar uma função
# sempre começam por letras minusculas e se tiverem nomes compostos separar por letras maiúsculas 

#sintaxe : def nome da função(parametro):
            # bloco de codigo
            
# OBS : TODA FUNÇÂO TEM UM RETORNO

#Ex


x = 10

y = 20

def soma(): # criamos uam função que retorna a soma dos valores declarados em x e y
    return x + y

print(soma()) # 30 
# caso ocorra mudança dos valores de x e y e chamarmos a função de novo ela executara com base nos novos dados

x = 40

y = -20

print(soma()) # 20 # lembrando que o valor da primeira soma n é excluido, pois a chamada da função "puxa" a relação de todo codigo que está declarado acima


#outro exemplo

def chamandoFrase():
    print('ola!')
    
    
chamandoFrase() # ola!

# função acima com parametros de entrada

def chamandoFraseDeNovo(frase):
    print(frase)
    
chamandoFraseDeNovo('Olá mundo!') # Olá mundo!




 
# PODEMOS CRIAR UMA VARIAVEL DO TIPO FUNÇÃO # 


def nome():
    print('igor')
    

nomeUsuario = nome # não deve ser declarada invocando a função

print(type(nomeUsuario)) # <class 'function'>

nomeUsuario() # igor # logo como atribuimos a função nome() a variavel nomeUsuario, podemos agora invocar a variavel para chamar a função




# CLASSIFICAÇÃO FUNÇÕES

# 1) função com retorno e sem retorno:

# 1.1) retorno é utilizado para justamente retornar alguma operação, variavel de dentro da função
# para isso usamos a palavra reservada return

# OBS: se voce nao retornar nada, porem ainda sim declarando o return - a função vai retornar o tipo None

# OBS2:  assim que a função reconhece o comando return, ela finaliza automaticamente
#ex

# retornando uma operação

def somandoNumeros():
    x = 20
    y = 20
    return x + y

somandoNumeros() # 40 

def subtraindoNumeros():
    x = 20
    y = 20
    return x - y

subtraindoNumeros() # 0



# retornando variaveis

def numeros():
    x = 20
    y = 20
    soma = x + y
    return soma

numeros() # 40

def numerosSubtraidos():
    x = 20
    y = 20
    subtracao = x - y
    return subtracao

numerosSubtraidos() # 0


# podemos ter '2 retornos' dentro de uma função: no caso um print() e um retorno

#ex 

def name():
    nome = 'matheus'
    print(f'Ola {nome}')
    return nome



print(name()) # Ola matheus    # matheus (o retorno me retorna um valor que eu possa usar) (o print retorna uma mensagem no console)


# outro exemplo de função com retorno mais complexa



def cont(numero):
    x = numero
    print(x, end=", ")
    contador = 0
    while contador <= 10:
        if x != None:
            x += numero
            print(x, end=", ")
            contador += 1
    return 

print(cont(10)) # 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, None



# 2) funções recursivas e não recursivas

# recursividade aquilo que se repete indefinidademente. Em programação é uma função que retorna ela mesma (call back function do javascript)

# função não recursiva não retorna ela mesma

# ex


# 2.1) função não recursiva

def conversor():
    celsius = int(input('digite um valor em celsius: '))
    kelvin = celsius + 273
    return kelvin


print(conversor()) # defini o valor do input como 30 o retorno foi 303


# 2.2) função recursiva
# OBS LEMBRE-SE SEMPRE DE UMA CONDIÇÂO DE PARADA EM UMA FUNÇÃO RECURSIVA, CASO CONTRARIO CAIRA NUM LOOP INFINITO

def converter():
    celsius = int(input('digite um valor em celsius')) # temos um input de dados
    kelvin = celsius + 273
    sair = input('digite se deseja sair: ') # mais um input para verificar se o usuario deseja ou nao continuar
    if sair == 'sim': # se sim retorna uma string 'acabou'
        return 'Acabou'
    else: # senao ele retorna a execução da função novamente
        return converter()
        
# a função acima simula um while 

# sair = ''
# celsius = 0
# kelvin = 273

# while sair != 'nao':
#     celsius = int(input('digite o valor em celsius: '))
#     kelvin += celsius
    
    
# OBS LEMBRE-SE SEMPRE DE UMA CONDIÇÂO DE PARADA EM UMA FUNÇÃO RECURSIVA, CASO CONTRARIO CAIRA NUM LOOP INFINITO


#           VANTAGEM DE USAR RECURSIVIDADE

# 1) torna o codigo mais limpo e gera sequencia facilmente (podendo substituir um loop for ou while)

#           DESVANTAGENS DE USAR RECURSIVIDADE

# 1) a logica pode ser mais complexa
# 2) pode usar mais memoria
