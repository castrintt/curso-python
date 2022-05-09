# 1 ) - Pickle -->> objetivo do pickle é realizar a serialização dos dados ou serialização dos dados recebidos como objeto.
# - seu conteudo não é entendivel para leitura humana

# - obs -> apenas faça leitura de arquivos apenas se a fonte for confiavel, pois pode conter conteudo malicioso

# 1.1)  escrevendo em arquivos pickle

# precisamos da biblioteca pickle 

# vamos importa-la
# sintaxe --> import pickle

# ex

import pickle

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
    