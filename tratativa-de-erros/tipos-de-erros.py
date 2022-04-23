# TIPOS DE ERROS MAIS COMUNS EM PYTHON

# Para tratar erros é muito bom prestar atenção na mensagem apresentada no console

# ERROS COMUNS

# 1) AttributeError : ocorre quando há fallha de atribuição


# ex

dicionario = {
    'sp':'sao paulo',
    'mg':'minas gerais'
}



dicionario.add('es') # add não é um atributo de dicionario 
#Oorre attributeError pois o comando add() não existe para dicionarios


# 2) indexError : ocorre quando não existe o indice de acesso dentro da variavel

# ex

lista = [1,2,3,4,5]

print(lista[3]) # 4

print(lista[6]) # IndexError :  o indice 6 não existe dentro da lista


# 3) KeyError : ocorre quando uma chave não é encontrada dentro do dicionario

dicionarioKey = {
    'mae':'Beliria',
    'irma':'Isabela'
}

print(dicionario['avo']) # a Key 'avo' não existe dentro do dicionarioKey


# 4) NameError : ocorre quando uma variavel ou função não é encontrada no codigo

# ex

nome = 'igor'

print(sobreNome) # NameError pois a variavel sobreNome não foi declarada no codigo

somaNumeros(5,1) # NameError pois a função somaNumeros() nunca foi declarada



# 5 ) SintaxeError : ocorre quando há um erro de sintaxe:

# ex

variavel = 
10
break 100

def variavel = 5

# esse tipo de sintaxe o python não reconhece (pois não é valida)



# 6) IndentationError: Ocorre quando há algum erro de indentação no codigo

# ex

numero = 5

if numero < 6:
print(numero)

# retorna indentationError pois a indentação do codigo após o if não esta correta



# 7) TypeError : ocorre quando há uma operação com tipos incorretos

# ex

nome = 'igor'

numero = 10

nome_numero = nome + numero
# só podemos concatenar strings com strings e somar tipos numericos com tipos numericos



# 8 ) ValueError : acontece quando uma função recebe um parametro de tipo certo, mas valor errado


# ex

valor = int(input('Digite um numero de 1 a 10'))

# se o usuario digitar uma string com um dado caracater ('alfabetico') vai retornar um erro de valor , pois não há como converter uma string (alfabetica) em numero

