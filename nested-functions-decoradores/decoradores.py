# Decoradores - são funções que você utiliza para decorar, enfeitar, complementar suas outras funções
# OBS - para utilizar a função declaradora devemos declara-la antes de usar o declarador

# Lembrando que dentro da função declaradora devemos usar como parametro a função que queremos decorar!
# OBS - A FUNÇÃO MAIS EXTERNA DA DECORADORA RECEBE A FUNCAO E A INTERNA RECEBE OS PARAMETROS (VIA ARGS)
# como declarar
# sintaxe : @nome_da_funcao_decoradora
        #   def função_a_ser_Decorada()

# ex sem utilizar decorador

def pessoa():
    print('Arthur')

def motivacao(funcao): # usando a função que queremos decorar como parametro
    def decorando():
        funcao()
        print('Continue em frente')
        print('Você é o melhor!')
    return decorando # sem retornar a execução da função interna

motivo = motivacao(pessoa)

motivo()
# Arthur
# Continue em frente
# Você é o melhor!

# ou 


def pessoa():
    print('Arthur')

def motivacao(funcao):
    def decorando():
        funcao()
        print('Continue em frente')
        print('Você é o melhor!')
    return decorando() # retornando a execução da função interna

motivacao(pessoa)
# Arthur
# Continue em frente
# Você é o melhor!



# USANDO DECORADORES com o proprio decorador



def motivacao(funcao):
    def decorando():
        funcao()
        print('Continue em frente')
        print('Você é o melhor!')
    return decorando 
# devemos chamar a função decoradora logo abaixo da sua declaração

@motivacao #decorando  # dessa forma, devemos simplismente chamar a função pessoa() que o seu decorador é executado
def pessoa():
    print('Arthur')


pessoa() # utilizando o decorador basta eu invocar a execução da função que foi decorada que ja estara funcionando

# Arthur
# Continue em frente
# Você é o melhor!


                # OQUE FOI FEITO ALI EM CIMA É BASICAMENTE ISSO AQUI:


def motivacao():
    def decorando():
        print('Continue em frente')
        print('Você é o melhor!')
    return decorando # retornando o nome da função e nao sua execução


def pessoa():
    print('Arthur')
    motivacao() # executando ela

pessoa()

# Arthur
# Continue em frente
# Você é o melhor!


                                # OU assim

def motivacao():
    def decorando():
        print('Continue em frente')
        print('Você é o melhor!')
    return decorando() # retornando a execução


def pessoa():
    print('Arthur')
    motivar = motivacao
    motivar()

pessoa()

# Arthur
# Continue em frente
# Você é o melhor!




#                   Ou assim

def motivacao():
    print('Continue em frente')
    print('Você é o melhor!')

def pessoa():
    print('Arthur')
    motivacao()

pessoa()

# Arthur
# Continue em frente
# Você é o melhor!



# QUAL A VANTAGEM DE USAR DECORADORES

# - usando decoradores você tem o trabalho de criar a função decoradora apenas uma vez, e basta chamar com o arroba (@)

# - Melhor visualização no codigo

# - São muito comuns em frameworks web(desenvolvimento de sites) Flask e bottle





# PASSANDO PARAMETROS NOS DECORADORES

def calculadora(funcao):
    def decorando(x,y,op):
        print(f'Operador {op}')
        return funcao(x,y,op)
    return decorando

@calculadora
def soma(num1,num2,op):
    return num1 + num2

print(soma(20,20,2)) 
# Operador 2 # passamos um parametro chamando a função soma que foi utilizado dentro da função decoradora
# 40 

# PARA FICAR MELHOR A VISUALIZAÇÃO ACONTECEU BASICAMENTE ISSO

# def calculadora(soma(20,20,2)):
#     def decorando(20,20,2):
#         print(f'Operador {2}')
#         return soma(20,20,2)
#     return decorando



# Melhorando  o exemplo
# OBS - SE O NUMERO DE PARAMETROS DE ENTRADA FOR DIFERENTE????? OQUE FARIAMOS?
# Basta usar como parametro *args ou **kwargs, caso os parametros sejam diferentes conseguiremos usar a mesma função decoradora ainda!
# ex


def calculadora(funcao):
    def decorando(*args):
        if len(args) == 2:
            print(f'Estamos fazendo uma soma')
            return funcao(*args)
        else:
            print(f'Estamos fazendo uma multiplicação')
            return funcao(*args)
    return decorando

@calculadora
def soma(num1,num2):
    return num1 + num2

@calculadora
def mult(num1,num2,num3): 
    return num1 * num2 * num3


print(soma(20,20))
print(mult(12,14,10))

# Estamos fazendo uma soma
# 40
# Estamos fazendo uma multiplicação
# 1680






# DICAS EXTRA: COMO FORÇAR PARAMETROS COM DECORADORES
# suponhamos que no codigo acima nós quisessemos passar como obrigatorio o primeiro parametro da soma e da multiplicação como 10
# como fariamos isso?
# basta colocarmos uma condição ou uma tratativa de erro caso o numero não seja 10
# veja abaixo


def calculadora(funcao):
    def decorando(*args):
        if args[0] == 10:
            if len(args) == 2:
                print(f'Estamos fazendo uma soma')
                return funcao(*args)
            else:
                print(f'Estamos fazendo uma multiplicação')
                return funcao(*args)
        else:
            return f'O primeiro valor deve ser 10'
    return decorando


@calculadora
def soma(num1,num2):
    return num1 + num2

@calculadora
def mult(num1,num2,num3): 
    return num1 * num2 * num3


print(soma(20,20))
print(mult(12,14,10))

# O primeiro valor deve ser 10
# O primeiro valor deve ser 10

print(soma(10,20))
print(mult(10,14,10))

# Estamos fazendo uma soma
# 30
# Estamos fazendo uma multiplicação
# 1400



