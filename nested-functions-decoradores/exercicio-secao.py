# # 1) decorar o exercicio da aula de Nested Functions e executar as três funções.
# # - na função que executa a string maiuscula use um decorador para imprimir: 'Estou gritando'
# # - na função que soma dois numeros decore com 'o maior entre os dois é: {maior}'
# # - na função que soma um numero com outro aleatorio decore com 'somando com o aleatorio'
# # -faça o tratamento com Wraps no programa

# # resolução 1

from random import randint as rd
from functools import wraps 


def maior(funcao):
    @wraps(funcao)
    def decorador(*args):
        if args[0] == 'soma':
            print(f'O maior valor é {max([ args[1], args[2] ])}')
            return funcao(*args)
        elif args[0] == 'upper_str':
            print('Estou gritando!')
            return funcao(*args)
        elif args[0] == 'soma_aleatoria':
            print('Somando com o aleatorio!')
            return funcao(*args)   
    return decorador


@maior
def funcao_externa(*args):
    if args[0] == 'upper_str':
        def upper_str():
            try:
                print(args[1].upper())
            except AttributeError:
                print('Não tem como aplicar upper() em variaveis que não sejam do tipo string')
        return upper_str
    elif args[0] == 'soma':
        def soma():
            try:
                print(f'{args[1] + args[2]}')
            except TypeError:
                print('Deve-se conter apenas numeros!')
        return soma
    elif args[0] == 'soma_aleatoria':
        def soma_aleatoria():
            numeroAleatorio = rd(0,15)
            print(f'A soma entre {args[1]} e {numeroAleatorio} é {sum([args[1], numeroAleatorio])}')
        return soma_aleatoria
    else:
        def erro():
            print('Nenhum funcao chamada')
        return erro

resultado = funcao_externa('soma_aleatoria',10)
resultado()




# resolução professor



from random import randint
from functools import wraps

def decorando(funcao):
    @wraps(funcao)
    def interna(*args):
        if args[0] == 'upper_str':
            print('Estou gritando')
            return funcao(*args)
        elif args[0] == 'soma':
            if args[1] > args[2]:
                print(f'O maior numero é : {args[1]}')
            else:
                print(f'O maior numero é : {args[2]}')
        elif args[0] == 'soma_aleatoria':
            print('somando com o aleatorio')
        return funcao(*args)
    return interna


@decorando
def funcao_externa(*args):
    if args[0] == 'upper_str':
        def upper_str():
            try:
                print(args[1].upper())
            except AttributeError:
                print('Não tem como aplicar upper() em variaveis que não sejam do tipo string')
        return upper_str
    elif args[0] == 'soma':
        def soma():
            try:
                print(f'{args[1] + args[2]}')
            except TypeError:
                print('Deve-se conter apenas numeros!')
        return soma
    elif args[0] == 'soma_aleatoria':
        def soma_aleatoria():
            numeroAleatorio = randint(0,15)
            print(f'A soma entre {args[1]} e {numeroAleatorio} é {sum([args[1], numeroAleatorio])}')
        return soma_aleatoria
    else:
        def erro():
            print('Nenhum funcao chamada')
        return erro
resultado = funcao_externa('upper_str','meu deus do ceu')
resultado()


resultado = funcao_externa('soma',12,12)
resultado()


resultado = funcao_externa('soma_aleatoria',12)
resultado()