# 1 ) - Pickle -->> objetivo do pickle é realizar a serialização dos dados ou serialização dos dados recebidos como objeto.
# - seu conteudo não é entendivel para leitura humana

# - obs -> apenas faça leitura de arquivos apenas se a fonte for confiavel, pois pode conter conteudo malicioso

# 1.1)  escrevendo em arquivos pickle

# precisamos da biblioteca pickle 

# vamos importa-la
# sintaxe --> import pickle

# ex

from ctypes import PyDLL
import pickle
from re import A, S
from socket import AI_ADDRCONFIG

class Filme:

    def __init__(self, nome, personagem):
        self.__personagem = personagem
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @property
    def personagem(self):
        return self.__personagem


filme1 = Filme('senhor dos aneis','Frodo')

filme2 = Filme('Jogos vorazes','Katniss')


# para ler ou escrever em um arquivo binario (pickle) devemos usar o modo wb e rb (como vimos antes, w -escreve, r -lê, [write e read], porem para arquivos tipo pickle devemos indicar que a leitura é do tipo binaria ou a escrita é do tipo binaria, isso serve tbm para x e a [outros modos de abertura de arquivos])

with open('filmes.pickle','wb') as filmes:

    pickle.dump((filme1,filme2),filmes) # podem ser passado varios objetos ou somente um se for o caso

    # metodo dump da biblioteca pickle recebe 2 parametros o primeiro é um objeto ou uma tupla de objetos e o segundo é qual arquivo que vai ocorrer o pickle
    # nesse caso os dois objetos foram passados no primeiro parametro (filme1,filme2) e o segundo parametro é o arquivo que estamos abrindo para escrever(que por sua vez está sendo criado agora)

    # metodo dump -->> serializa o conteudo do objeto (basicamente transforma em binario)


# Agora que criamos o arquivo e escrevemos nele usando o modo wb, vamos agora ler o arquivo usando o modo rb (read binary)


import pickle

with open('filmes.pickle','rb') as filmes:

    filme1,filme2 = pickle.load(filmes) # vamos carregar o arquivo pickle (filmes) nos dois objetos (filme1, filme2)
    # load descarrega o arquivo aplicando a desserialização

    print(f'O filme {filme1.nome} teve como personagem o {filme1.personagem}') # O filme senhor dos aneis teve como personagem o Frodo
    print(f'O filme {filme2.nome} teve como personagem a {filme2.personagem}') # O filme Jogos vorazes teve como personagem a Katniss
    


# 2 )  arquivo JSON  - JavaScript Object Notation

# - utilizado em API'S --> interface de programação de aplicativos

# - a estrutura de uma api é sempre constituida por chaves , a notação é identica a um dicionario ( em javascript seria simplismente um objeto normal!  [lembrando que um dicionario tem a mesma notação que um objeto em javascript] )

# - seus dados (chave, valor) são escritos entre aspas duplas sempre

# -- para ver a estrutura  de um arquivo JSON entre no site --> https://jsonapi.org/

# temos que importar uma biblioteca para ler ou escrever em um arquivo JSON ---> import json

#ex

import json

# metodo dumps() --> formata para o formato JSON (aspas duplas) 
# ex

dicionarioEmPython = {
    'nome':'igor',
    'idade':12
}

testeJson = json.dumps(dicionarioEmPython)

print(testeJson) # {"nome": "igor", "idade": 12} # pronto ele transformou em notação json (isso só aconteceu porque importamos a biblioteca json para o python)

print(type(testeJson)) # <class 'str'> --> note que o metodo dumps() transforma um dicionario em uma string com notação JSON

# em python podemos usar o JSON e o pickle juntos! --> para desserializar e serializar objetos
# para isso temos que instalar uma dependência chamada jsonpickle -->> o comando no console é pip install jsonpickle (lembre-se de instalar somente quando estiver em ambiente de desenvolvimento venv!)

# depois de instalar a dependencia da biblioteca jsonpickle podemos simplismente importa-la e usar no nosso programa com --> import jsonpickle


import json
import jsonpickle

class Filme:

    def __init__(self, nome, personagem):
        self.__personagem = personagem
        self.__nome = nome


    @property
    def nome(self):
        return self.__nome

    @property
    def personagem(self):
        return self.__personagem

#  vamos instanciar um objeto pela classe Filme

filme1 =  Filme('Senhor Dos Aneis','Frodo')

# para criar um dicionario no formato JSON usamos o comando ---> jsonpickle.encode(nomeDoObjeto)
# ex

# print(jsonpickle.encode(filme1)) # {"py/object": "__main__.Filme", "_Filme__personagem": "Frodo", "_Filme__nome": "Senhor Dos Aneis"}

# o primeiro elemento mostra qual classe o objeto pertence

# 2.1 ) escrevendo em arquivos jsonpickle

with open('filmes.json','w') as arquivo:

    arquivo.write(jsonpickle.encode(filme1))
    # um arquivo json foi criado com o seguinte conteudo {"py/object": "__main__.Filme", "_Filme__personagem": "Frodo", "_Filme__nome": "Senhor Dos Aneis"}


# 2.2 ) lendo um arquivo jsonpickle

# como nos usamos o metodo encode para formatar um objeto em JSON e depois o escrevemos usando o metodo write , vamos usar agora o decode para converter o arquivo em string e ler usando o metodo read() abrir o programa e ler!

with open('filmes.json','r') as arquivo:
    
    ler = jsonpickle.decode(arquivo.read())
    # podemos agora acessar as propriedades do objeto que foi instanciado pela classe Filme
    print(ler.nome) # Senhor Dos Aneis
    print(ler.personagem) # Frodo
