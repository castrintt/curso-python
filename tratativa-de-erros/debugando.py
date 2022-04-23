# debug é uma forma de voce limpar e analisar todos os problemas ocorridos no seu codigo

# OBS a pratica de usar o print() para tratar erros apresentando aos poucos os dados ao longo do programa é uma pratica ruim

# A PARTIR DA VERSÃO 3.7 DO PYTHON NAO PRECISAMOS IMPORTAR O PDB
# BASTA USAR O COMANDO breakpoint()

# PRINT APENAS VERIFICA

def boas_vindas(nome):
    print(nome) #carlos
    print(f'Seja bem vindo/a {nome}')

boas_vindas('Carlos')


# FORMA PROFISSIONAL / PYTHONICA DE CORRIGIR ERROS DE CODIFICAÇÃO

# 1) pdb - python debugger

# para utiliza-lo devemos importar uma biblioteca chamada pdb e assim usar a função set_trace()

#sintaxe import pdb

import pdb

pdb.set_trace()

# comandos basicos para usar em pdb:

 #1.1) l ( list ) : APRESENTA ONDE VOCE ESTA NO CODIGO

 #1.2 ) n ( next ) : PULAR PARA PROXIMA LINHA

 #1.3 ) p ( print ) : IMPRIME UMA VARIAVEL # sintaxe :  p variavel

 #1.4 ) c ( continue ) : CONTINUAR A EXECUÇÃO DO CODIGO ATÉ O FINAL DO PROGRAMA OU ATÉ O PROXIMO SET_TRACE()

# OBS - recomenda-se chamar o import do pdb perto do local que voce deseja importa-lo
 # ex

x = 2

y = 3
# suponha que esteja acontecendo algum problema na variavel z vamos usar o pdb.set_trace() logo acima dela para verificar o codigo
pdb.set_trace()
z = x * y

nome = 'Clara'

frase = nome * z



# 2) USANDO BREAKPOINT() # MAIS USADO 

# A PARTIR DA VERSÃO 3.7 DO PYTHON NAO PRECISAMOS IMPORTAR O PDB
# BASTA USAR O COMANDO breakpoint()

# os comandos do breakpoint() são os mesmos do import do pdb pois a partir da versão 3.7 do python o pdb passou a ser uma função build_in

# para reforçar vou repassar os comandos

 #1.1) l ( list ) : APRESENTA ONDE VOCE ESTA NO CODIGO

 #1.2 ) n ( next ) : PULAR PARA PROXIMA LINHA

 #1.3 ) p ( print ) : IMPRIME UMA VARIAVEL # sintaxe :  p variavel

 #1.4 ) c ( continue ) : CONTINUAR A EXECUÇÃO DO CODIGO ATÉ O FINAL DO PROGRAMA OU ATÉ O PROXIMO SET_TRACE()

# ex

num1 = 22

num2 = 23

numeros = [num1 + num2]
breakpoint()