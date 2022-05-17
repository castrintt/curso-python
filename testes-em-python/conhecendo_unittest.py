# uma das ferramentas mais importantes para usar nos nossos testes! 

# oque são ---> é um modulo para testar individualmente a principio, classes, funções e metodos (logicamente pode ser usado para outros fins, porem os mais comuns e mais usados são esses 3)

#           como podemos trabalhar com unittest 
# 1) primeiro vamos importar unittest --> import unittest
# 2) criamos classes que herdam TestCase (test de caso) a partir desse modulo podemos usar todos os assertions contidos nele

# tabela com os assertions contidos em unittest --> http://docs.python.org/pt-br/3/library/unittest.html#assert-methods

# --> logo

# ex ja aplicando nosso metodo TDD --> cria os testes , implementa os testes e refatora

# função que converte o padrao 24hr para 12hrs

def converte_padrao(hora, min):
    if hora >= 12:
        hora = hora -12
        return f'{hora}:{min} P.M'
    return f'{hora}:{min} A.M'




# função que define se é par ou impar, se for par retorna true, se for impar retorna false

def par_impar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


# É SEMPRE CONVENIENTE CRIAR UM MODULO A PARTE PARA EXECUTAR OS TESTES SEPARADAMENTE

