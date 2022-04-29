# wraps e forçando dados / delimitando dados

# 1 ) Forçando dados em decoradores
# Primeira função do conjunto dos decoradores tem como parametro os tipos de dados  a serem recebidos usando a sintaxe de *args
# Segunda função do conjunto dos decoradores tem como parametro a função que vai ser responsavel por enviar o tipo de dado
# Terceira função do conjunto dos decoradores tem como parametro *args que vão ser usados para representar os dados enviados como parametro da função
# como args são tuplas, devemos transforma-los em uma lista

# sintaxe 

# def tipo_dado(*tipos):

#     def recebe_funcao(funcao):

#         def converte_dado(*args): 

#             lista = [] # transformando os *args da função em lista (de tupla para ---> lista)
#             lista.append(tipos[indice](args[indice]))
#             return funcao(*lista) # retorna o dado convertido que está armazenado dentro da lista (usando descompactando), usamos o sinal * antes de uma lista, ou tupla, para descompactar todos os dados dela (comumente usando junto a *args e **kwargs)

#         return converte_dado # retornando a proxima função na hierarquia

#     return recebe_funcao # retornando a proxima função na hierarquia



# @tipo_dado(str,int,float,bool,complex) # chamado a função tipo_dado(usada como decorador) # nós passamos os *tipos(como argumentos) para receber todos os parametros que quisermos colocar, nesse caso estou chamando todos os tipos de dados
# def funcao_a_ser_usada_como_base(*parametros):

#     return parametros # depois de ela passar pela função decoradora o tipo de dado vai ser convertido

# funcao_a_ser_usada_como_base(12312,'12','14','1',123) # seguindo a logica, o primeiro dado vai ser convertido em string, o segundo em inteiro, terceiro em float, quarto em boolean e quinto(ultimo) em complexo



# ex    



def tipo(*tipos): # mesma coisa que args #(recebendo os tipos complex, float)
    def decorando(funcao):
        def convertendo_dados(*args):
            altera_tipo = []
            altera_tipo.append(tipos[0](args[0])) #alterando o primeiro valor para complexo
            altera_tipo.append(tipos[1](args[1]))
            return funcao(*altera_tipo)
        return convertendo_dados
    return decorando



@tipo(complex,float)
def imprimindo(a,b):
    print(f'Numero complexo: {a} , numero Flutuante: {b}')



imprimindo('2',2)


# ex 2

def alterando(*tipos):
    def decorando(funcao):
        def alterando_tipo(*args):
            tipo_alterado = []
            tipo_alterado.append(tipos[0](args[0]))
            tipo_alterado.append(tipos[0](args[1]))
            return funcao(*tipo_alterado)
        return alterando_tipo
    return decorando



@alterando(float)
def soma(a,b):
    print(f'Primeiro numero: {a} segundo numero: {b}')
    return a + b


print(soma('20',23)) 
# Primeiro numero: 20.0 segundo numero: 23.0
# 43.0


# ex 3 forçando string


def muda_texto(*tipo):
    def recebe_funcao(funcao):
        def altera_dado(*args):
            lista = []
            lista.append(tipo[0](args[0]))
            return funcao(*lista)
        return altera_dado
    return recebe_funcao


@muda_texto(str)
def texto(text):
    print(f'O texto é {text}')
    print(f'O tipo do texto é {type(text)}')
    return text


texto(128912389123)
 # O texto é 128912389123
#  O tipo do texto é <class 'str'> # convertemos um inteiro para string

texto(True) 
# O texto é True
# O tipo do texto é <class 'str'> #convertemos um boolean para string


# ex 4 convertendo para boolean


def muda_bool(*tipo):
    def recebe_funcao(funcao):
        def converte_dado(*args):
            lista = []
            lista.append(tipo[0](args[0]))
            return funcao(*lista)
        return converte_dado
    return recebe_funcao




@muda_bool(bool)
def verdadeiro_ou_falso(dado):
    print(f'O tipo do dado é {type(dado)}')
    print(f'{dado}')
    return dado
    
verdadeiro_ou_falso('lalalala')
# O tipo do dado é <class 'bool'> # convertemos uma string para boolean
# True

verdadeiro_ou_falso(123123123123)
# O tipo do dado é <class 'bool'> # convertendo inteiro para boolean
# True


verdadeiro_ou_falso(123.123123)
# O tipo do dado é <class 'bool'>  # convertendo float para boolean
# True 

verdadeiro_ou_falso(2j + 2)
# O tipo do dado é <class 'bool'> #convertendo complexo para boolean
# True




# 2 ) USANDO WRAPS - copia os metadados da função antes de ser decoarada. portanto utilizar um decorador não tira a identidade da sua função

# - Oque são metadados - são dados sobre outros dados
# um decorator é um metadado ---> é um dado que sera manipulado em cima de outro dado (função decorada)

# ex, explicando o problema - Nós ja vimos o dunder name (__name__), ele retorna o nome da função a ser usada
# enquanto o dunder doc (__doc__) retorna a documentação da função

# OQUE ACONTECEU NO CODIGO ABAIXO??? --> # PERCEBEMOS QUE AO IMPRIMIR A DOCUMENTAÇÃO DE CONT_ALUNOS_APROVADOS , ELE RECONHECE COMO A FUNÇÃO DECORADORA, ISSO É UM PROBLEMA, POIS CASO VOCÊ TENHA UM PROGRAMA E QUERIA CONSULTAR A DOCUMENTAÇÃO DAS FUNÇÕES PROFISSIONALMENTE PODE OCORRER CONFLITOS POIS SEUS METADADOS ESTÃO SOBREPOSTOS
# MAS COMO RESOLVEMOS ISSO?? -->> usando WRAPS



def aprovados(funcao):
    """
    função que retorna uma losta com os alunos aprovados
    """
    def decorador(*args,**kwargs):
        """
        Função que decora e faz os testes de notas
        """

        aprove = []
        print(f'{aprovados.__name__}') # retorna o nome da função aprovados
        print(f'{aprovados.__doc__}') # retorna a documentação da função aprovados
        # retorno dos prints abaixo \/ \/
                                # aprovados

                                # função que retorna uma losta com os alunos aprovados

        for chave,valor in kwargs.items():
            if valor > 6:
                aprove.append(chave)       
        print(aprove)     
        return funcao(*aprove)
    return decorador

@aprovados # usando decorador aprovados eu tenho como saber quem são os alunos aprovados, sem gerar uma logica dentro da função principal
def cont_alunos_aprovados(*args,**kwargs):
    """
    função que apresenta a quantidade de alunos aprovados

    """
    print(cont_alunos_aprovados.__name__)
    print(cont_alunos_aprovados.__doc__)
                        # retorno dos prints abaixo \/\/
                                                    # decorador

                                                    #     Função que decora e faz os testes de notas
    print(len(args))
    
cont_alunos_aprovados(leticia=4,joao=12,maria=23)

# ['joao', 'maria']
# 2

# OQUE ACONTECEU NO CODIGO ACIMA??? --> # PERCEBEMOS QUE AO IMPRIMIR A DOCUMENTAÇÃO DE CONT_ALUNOS_APROVADOS , ELE RECONHECE COMO A FUNÇÃO DECORADORA, ISSO É UM PROBLEMA, POIS CASO VOCÊ TENHA UM PROGRAMA E QUERIA CONSULTAR A DOCUMENTAÇÃO DAS FUNÇÕES PROFISSIONALMENTE PODE OCORRER CONFLITOS POIS SEUS METADADOS ESTÃO SOBREPOSTOS
# MAS COMO RESOLVEMOS ISSO?? -->> usando WRAP

#                                   # SOLUÇÃO

# importamos o wraps de functools
# sintaxe: from functools import wraps

# PARA CORRIGIR O PROBLEMA, BASTA CHAMAR O WRAPS (COM A MESMA SINTAXE DE UMA FUNÇÃO DECORADORA) ANTES DA FUNÇÃO DECORADORA
# Nós BASICAMENTE DECORAMOS UMA FUNÇÃO DECORADORA!
# Utilizando o mesmo exemplo

from functools import wraps

def aprovados(funcao):
    """
    função que retorna uma losta com os alunos aprovados
    """
    @wraps(funcao) # PRONTO ----->>> CHAMAMOS O WRAPS -->> dessa forma a documentação e nome da nossa função principal vai ser preservado
    def decorador(*args,**kwargs):
        """
        Função que decora e faz os testes de notas
        """

        aprove = []
        print(f'{aprovados.__name__}') # retorna o nome da função aprovados
        print(f'{aprovados.__doc__}') # retorna a documentação da função aprovados
        # retorno dos prints abaixo \/ \/
                                # aprovados

                                # função que retorna uma losta com os alunos aprovados

        for chave,valor in kwargs.items():
            if valor > 6:
                aprove.append(chave)       
        print(aprove)     
        return funcao(*aprove)
    return decorador

@aprovados # usando decorador aprovados eu tenho como saber quem são os alunos aprovados, sem gerar uma logica dentro da função principal
def cont_alunos_aprovados(*args,**kwargs):
    """
    função que apresenta a quantidade de alunos aprovados

    """
    print(cont_alunos_aprovados.__name__)
    print(cont_alunos_aprovados.__doc__)
                        # retorno dos prints abaixo \/\/
                                                    # decorador

                                                    #     Função que decora e faz os testes de notas
    print(len(args))
    
cont_alunos_aprovados(leticia=4,joao=12,maria=23)