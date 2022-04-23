 # try, except , else e finally

 # são palavras reservadas

# todas são declaradas como blocos (ou seja, precisa ser indentado)

# DIFERENTE DO RAISE O TRY EXCEPT NÃO PARA A EXECUÇÃO DO PROGRAMA

# declaração 

# try: (tente fazer isso) # deu certo? faça o else # deu errado? passa para o except
#     #processo

# except:(se ocorrer um erro durante a tentativa, tente isso) # deu certo? finaliza # deu errado? passa para o else
#     #processo

# else: (senão faça isso) # deu certo ? finaliza # deu errado? passa para o finally
#     #processo

# finally: (finalmente, tente isso) 
#     #processo

# OBS: else e finally são opcionais, ja o try e except são obrigatorios

# OBS2: o bloco else só é executado caso o try funcione

# OBS3: o bloco finally SEMPRE É EXECUTADO

# OBS4: o EXCEPT PODE RECEBER UM PARAMETRO

# OBS5: PODEMOS PASSAR QUANTOS EXCEPTS FOREM NECESSARIOS (somente se passar a especificação do erro como parametro, se tratar o erro de forma generica [somente declarando o except] voce não pode usar mais de 1 except)


# ex
# TRATANDO COM O TRY EXCEPT

#calculadora

from typing import Type


def soma(x,y):
    op = x + y
    return op

def sub(x,y):
    op = x - y
    return op

def mult(x,y):
    op = x * y
    return op

def div(x,y):
    op = x / y
    return op

try:
    operacao = int(input('Escolha a operação de acordo com o numero: \n1- soma\n2- subtracao\n3- divisao\n4- multiplicacao\n '))
except:
    print('Algo deu errado!')

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))


if operacao == 1:
    print(f'Resultado: {soma(num1,num2)}')
elif operacao == 2:
    print(f'Resultado: {sub(num1,num2)}')
elif operacao == 3:
    print(f'Resultado: {div(num1,num2)}')
elif operacao == 4:
    print(f'Resultado: {mult(num1,num2)}')

# dessa forma a execução do programa não para caso digitarmos qualquer valor que não seja numerico para respoder ao input da variavel operacao, ele retornar no console "algo deu errado", porem não para a execução



# VAMOS TRATAR DE FORMA ESPECIFICA (PASSANDO O TIPO DO ERRO COMO PARAMETRO DO EXCEPT) / MAIS INDICADA (passando parametros para o except) para tratar os erros



def soma(x,y):
    op = x + y
    return op

def sub(x,y):
    op = x - y
    return op

def mult(x,y):
    op = x * y
    return op

def div(x,y):
    op = x / y
    return op

try:
    operacao = int(input('Escolha a operação de acordo com o numero: \n1- soma\n2- subtracao\n3- divisao\n4- multiplicacao\n '))
except ValueError: # passando o parametro de ValueError # só é executado se o try não for atendido
    print('Algo deu errado!')

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))


if operacao == 1:
    print(f'Resultado: {soma(num1,num2)}')
elif operacao == 2:
    print(f'Resultado: {sub(num1,num2)}')
elif operacao == 3:
    print(f'Resultado: {div(num1,num2)}')
elif operacao == 4:
    print(f'Resultado: {mult(num1,num2)}')





# TRATAMENTO DE TRY EXCEPT E ELSE


def soma(x,y):
    op = x + y
    return op

def sub(x,y):
    op = x - y
    return op

def mult(x,y):
    op = x * y
    return op

def div(x,y):
    op = x / y
    return op

try:
    operacao = int(input('Escolha a operação de acordo com o numero: \n1- soma\n2- subtracao\n3- divisao\n4- multiplicacao\n '))
except ValueError: # passando o parametro de ValueError # só é executado se o try não for atendido
    print('Algo deu errado!')
else: #é executado somente se o try for atendido 
    num1 = int(input('Digite o primeiro numero: '))
    num2 = int(input('Digite o segundo numero: '))


    if operacao == 1:
        print(f'Resultado: {soma(num1,num2)}')
    elif operacao == 2:
        print(f'Resultado: {sub(num1,num2)}')
    elif operacao == 3:
        print(f'Resultado: {div(num1,num2)}')
    elif operacao == 4:
        print(f'Resultado: {mult(num1,num2)}')
# ou seja, o programa só entra no else, CASO O TRY SEJA ATENDIDO, SE NÂO FOR ATENDIDO ELE RESOLVE O EXCEPT (RETORNANDO UM ERRRO)




# USANDO TRY, EXCEPT, ELSE e FINALLY

# FINALLY È MUITO UTILIZADO PARA FINALIZAR PROCESSOS



def soma(x,y):
    op = x + y
    return op

def sub(x,y):
    op = x - y
    return op

def mult(x,y):
    op = x * y
    return op

def div(x,y):
    op = x / y
    return op

try:
    operacao = int(input('Escolha a operação de acordo com o numero: \n1- soma\n2- subtracao\n3- divisao\n4- multiplicacao\n '))
except ValueError: # passando o parametro de ValueError
    print('Algo deu errado!')
else: # é executado somente se o try for atendido
    num1 = int(input('Digite o primeiro numero: '))
    num2 = int(input('Digite o segundo numero: '))


    if operacao == 1:
        print(f'Resultado: {soma(num1,num2)}')
    elif operacao == 2:
        print(f'Resultado: {sub(num1,num2)}')
    elif operacao == 3:
        print(f'Resultado: {div(num1,num2)}')
    elif operacao == 4:
        print(f'Resultado: {mult(num1,num2)}')
finally: # sempre é executado
    print('Processo terminou')

#ou seja, se o try for atendido, resolve o else e depois finaliza pelo finally
# se o try n for atendido, passa para o except , depois da execução do except, o finally finaliza o programa



# PODEMOS TER MAIS DE UM BLOCO DE TRY, EXCEPT, ELSE E FINALLY NO PROGRAMA
# NO CODIGO ANTERIOR TRATAMOS O ERRO DA VARIAVEL OPERACAO, POREM AS VARIAVEIS NUM1 e NUM2 AINDA PODEM RECEBER ERROS, OU SEJA, ELAS PODEM RECEBER TIPOS DE DADOS QUE NÃO SÃO INTEIROS


# VAMOS TRATAR ESSES ERROS


def soma(x,y):
    op = x + y
    return op

def sub(x,y):
    op = x - y
    return op

def mult(x,y):
    op = x * y
    return op

def div(x,y):
    try: # tenta executar a divisao dos numeros (caso algum dos numeros seja 0 entramos no except) (caso não ocorra nenhum erro passamos para o else retornamos o valor de op)
        op = x / y
    except ZeroDivisionError:  # caso algum dos numeros na divisão seja 0 o erro a ser tratado é zeroDivisionError , nesse caso mostramos uma mensagem na tela para o usuario e chamamos a execução da função de novo!
        print('Numero não pode ser divido por 0')
        return div(x, y)
    except TypeError: # caso o erro seja de tipos, ou seja, se recebermos erros de tipo das variaveis(receber strings ou booleanos) entramos no except de TypeError
        print('Devemos receber um numero!')
        return div(x,y)
    else:
        return op

try:
    operacao = int(input('Escolha a operação de acordo com o numero: \n1- soma\n2- subtracao\n3- divisao\n4- multiplicacao\n '))
except ValueError: # passando o parametro de ValueError
    print('Algo deu errado!')
else: # é executado somente se o try for atendido
    try:# trata se o tipo de dado da variavel num1 do tipo inteiro (numerico)
        num1 = int(input('Digite o primeiro numero: '))
    except TypeError:# se nao for do tipo inteiro, o except é executado(passamos o parametro de TypeError pois o erro a ser tratato é um erro de tipos)
        print('Tipo da variavel incorreta!')
    else: # se o try for executado sem problemas, entramos no else
        try: # passamos mais um try, para verificar tipos de erros na variavel num2
            num2 = int(input('Digite o segundo numero: '))
        except TypeError: # se o try n tiver sucesso passamos ao except
            print('tipo da variavel incorreto!')
        else:# caso o try tenha sucesso executamos o else (agora não precisamos verificar mais nenhum dado, podemos prosseguir com a execução normal do codigo)
            if operacao == 1:
                print(f'Resultado: {soma(num1,num2)}')
            elif operacao == 2:
                print(f'Resultado: {sub(num1,num2)}')
            elif operacao == 3:
                print(f'Resultado: {div(num1,num2)}')
            elif operacao == 4:
                print(f'Resultado: {mult(num1,num2)}')
                #por fim, ele é executado com o finally abaixo
finally: # sempre é executado
    print('Processo terminou')


# No caso acima temos 3 estruturas de tratativa de erros
# no primeiro else da primeira estrutura, tivemos necessidade de tratar erros em 2 variaveis, criando assim, mais 2 estruturas de try, except e else

