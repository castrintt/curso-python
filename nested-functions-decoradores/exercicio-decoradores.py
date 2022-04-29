# 1) Faça uma função que calcule a diferença entre dois numeros
#  decore-a com outra função adicionando as Mensagens:
# - incio do programa
# - decorando a função.
#  Após isso faça com que o decorador permita que apenas seja calculada a diferença POSITIVA entre os dois numeros, independente da ordem de entrada. Imprima o resultado.

# resolução

def decorator(func):
    def verifica(a,b): 
        if func(a,b) < 0:
            a, b = b , a
            return a - b
        else:
            return a - b
    return verifica 

# função que faz a diferença entre dois numeros
@decorator
def dif(a,b):
    return a - b

print(dif(2,10))



# é a mesma coisa que fazer o seguinte:


def decorator(funcao):  # esse decorator vai retornar a função abaixo
    def verifica(a,b):
        if funcao(a,b) < 0:
            print('--------Inicio do programa------------')
            print('--------Decorando a função------------')
            a, b = b, a
            return funcao(a,b)
        else:
            print('--------Inicio do programa------------')
            print('--------Decorando a função------------')
            return funcao(a,b)

    return verifica # retornando apenas o nome da função

def dif(a, b):
    return a - b

resultado  = decorator(dif) # para que a execução de verifica(a,b) seja feita precisamos chamar ela la

# chamando a execução
print(resultado(10,2))



# RESOLUÇÃO PROFESSOR

def completa(funcao):
    def decora(x,y):
        print('--------Inicio do programa------------')
        print('--------Decorando a função------------')
        if x > y:
            funcao(x,y)
        else:
            funcao(y, x)
    return decora

@completa
def diminui(a,b):
    print(f'O resultado desejado é {a - b}')


diminui(7,1)
diminui(1,7)
