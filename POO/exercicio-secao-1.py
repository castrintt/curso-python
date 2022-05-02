# 1) Crie uma classe chamada personagem que irá receber como construtor o nome completo, altura, peso e resistencia (0 - 100) do personagem, alem disso, tambem crie um metodo que se chame poder() que conterá todos os atributos de instancia como privado não sendo possivel altera-los.
# sendo eles: 
# magina, persuasão, agilidade e forca
# cada um avaliada de 0 a 100
# por fim retorna apenas a soma de todos os pontos fornecidos. Crie 3 objetos instanciados pela classe personagem e imprima o nome completo e quantidade de poder total do mais forte

# minha resolução

class Personagem:
    def __init__(self, nome,altura, peso , resistencia):
        self.nome = nome
        self.altura = altura
        self.peso = peso
        self.resistencia = resistencia

    def poder(self, magia,persoasao,agilidade, forca):
        self.__magia = magia
        self.__persoasao = persoasao
        self.__agilidade = agilidade
        self.__forca = forca
        return f'A soma de todos os atributos de poder é {sum([self.__magia, self.__persoasao,self.__agilidade, self.__forca])}'
    

barbaro = Personagem('Czar',1.94,'130kg',30)
barbaro.poder(20,15,60,90)

mago = Personagem('Merlin',1.61,'70kg',15)
mago.poder(90,60,40,25)

ladino = Personagem('Creed',1.67,'60kg',20)
ladino.poder(5,80,80,40)

# criando uma lista de dicionarios, com todos os dados de todos objetos instanciados pela classe Personagem
listaDePersonagens = []
listaDePersonagens.extend([barbaro.__dict__,mago.__dict__,ladino.__dict__])

# separando poderes e nomes em listas diferentes
listaPoderesSomados = []
listaDeNomesDePersonagens = []

for valor in listaDePersonagens:
    listaPoderesSomados.append(sum(
        [ 
            valor['_Personagem__magia'],
            valor['_Personagem__agilidade'],
            valor['_Personagem__forca'],
            valor['_Personagem__persoasao'],
        ]
    ))
    listaDeNomesDePersonagens.append(valor['nome'])

# juntando tudo em uma lista de tuplas usando zip, para então comparar o nome do personagem com total de poder
listaPoderNomes = list(zip( listaPoderesSomados, listaDeNomesDePersonagens ))


for indice,valor in enumerate(listaPoderNomes):
    if valor[0] == max(listaPoderesSomados):
        print(f'O personagem mais forte é : {valor[1]} com total de poder: {valor[0]}')
        