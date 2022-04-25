# pacotes, Dunder Main e Dunder Name

# - pacotes são um conjunto de modulos

# OBS o modulo __init__.py deve ser criado, porem ele n é usado --> é somente convenção

# basta criar uma pasta e dentrod essa pasta criar um arquivo __init__.py e pronto, podemos criar quantos modulos quisermos dentro dessa pasta e acessa-los

# ex

# --> uma pasta com nome Modules --> dentro dessa pasta temos 10 arquivos, sendo 9 deles modulos com funções e 1 deles __init__.py que é como o python se referencia ou entende que há modulos naquela pasta

# para acessarmos os modulos dentro da pasta basta usar as variadas sintaxes 

# ex , vamos supor que dentro da pasta modules temos 3 modulos com 1 função em cada, um para somar, um para subtrair e um para dividir com os nomes --> somar.py, subtrair.py e dividir.py

# para importarmos esses modulos em uma pasta que esta no mesmo nivel da pasta modules basta usar a sitnaxe

from modules import somar # importa somente o modulo somar

from modules import somar, subtrair, dividir # importar os 3 modulos

from modules import * # importa todos os modulos

import modules.somar # só o modulo somar
import modules.subtrair #só o modulo subtrair
import modules.dividir # só o modulo dividir


# suponha que dentro do modulo dividir temos 2 funções uma que divide e outra que multiplica e queremos somente importar a função que multiplica, a sintaxe ficaria assim

# from modules.dividir import multiplicar


# para melhor entendimento criamos uma pasta chamada pacote1 e dentro dessa pasta criamos 2 arquivos, um chamado __init__.py(convenção) e outro chamado ola.py onde contem uma função que imprime no console ola! {usuario} vamos importa-la para esse arquivo e usa-la

import pacote1.ola

nome = 'igor'

pacote1.ola.apresentacao(nome) # Ola igor


from pacote1 import ola as o

o.apresentacao(nome) # Ola igor

from pacote1.ola import apresentacao as ap # importando a função como ap

ap(nome) # Ola igor



# Dunder significa ( __ ) douber underline

# dunder main = __main__
# dunder name = __name__

# usando o __name__ podemos saber de onde é tal variavel ou função, exemplo, no arquivo principal se digitarmos print(__name__) temos impresso no console __main__ porque estamos no arquivo principal

# agora se usarmos print(__name__) dentro do ola e executarmos ele aqui depois do import ele retornar o caminho da pasta. Veja:

#dentro do arquivo ola temos a seguinte cadeia

# def apresentacao(nome):
#     print(f'Ola {nome}')
# print(__name__)


from pacote1 import ola

ola.apresentacao('igor')

# ^^^-- retorna
# pacote1.ola #mostrando o diretorio de onde colocamos o __name__
# Ola igor

# PODEMOS REALIZAR O CONTROLE DE FUNÇÔES OU VARIAVEIS QUE NÃO QUEREMOS QUE SEJAM EXECUTADAS USANDO O __NAME__ JUNTAMENTE COM O __MAIN__ 
# dentro do arquivo ola.py podemos escrever a condição


if __name__ == '__main___':
    # execute o codigo 
    
# ou seja, se aquele arquivo for o __main__ execute o codigo, como sabemos que ola foi importado para outro lugar ele não é o arquivo main, por isso não sera executado o codigo
