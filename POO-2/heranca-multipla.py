# uma classe, pode herdar de inumeras outras classes ao mesmo tempo

# - existem dois tipos - porem independente do tipo, a subclasse (classe filha) vai herdar todos os metodos e atributos das superclasses (classes mães)
# diretas e indiretas

# 1) - herança multipla direta

# ex

class Energia:

    def __init__(self,ligado):
        self.__ligado = ligado

    
    @property
    def ligado(self):
        return self.__ligado

    
    def botao(self):
        self.__ligado = not self.__ligado
        return self.__ligado



class Memoria:

    def __init__(self, ram):
        self.__ram = ram


    @property
    def ram(self):
        return self.__ram

    

class Monitor:

    def __init__(self,polegadas):
        self.__polegadas = polegadas


    @property
    def polegadas(self):
        return self.__polegadas


# a classe Computador vai herdar de todas as outras classes
# basta declarar  a classe e passar como parametros todas as classes que ela vai herdar separadas por virgula

# e para acessar os atributos dos 3 construtores (porque temos 3 classes mãe) não vamos usar o super().__init__()
# vamos usar a seguinte sintaxe

# NomeClasse.__init__(self, atributos_de_instancia)

class Computador(Energia, Memoria, Monitor):

    def __init__(self, ligado, ram, polegadas, valor):
        Energia.__init__(self, ligado) # NomeClasse.__init__(self, atributos_de_instancia)
        Memoria.__init__(self, ram) # NomeClasse.__init__(self, atributos_de_instancia)
        Monitor.__init__(self, polegadas) # NomeClasse.__init__(self, atributos_de_instancia)
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    


pc = Computador(False, '4gb de ram','60 polegadas', 3000)

print(pc.__dict__) # {'_Energia__ligado': False, '_Memoria__ram': '4gb de ram', '_Monitor__polegadas': '60 polegadas', '_Computador__valor': 3000}

print(pc.ligado) # False

pc.botao() # metodo da classe herdada Energia

print(pc.ligado) # True

print(pc.ram) # 4gb de ram # propriedade herdada da Classe Memoria

print(pc.polegadas) # 60 polegadas # propriedade herdada da classe Monitor

print(pc.valor) # 3000 # propriedade da classe computador, não foi herdada! 




# 2 ) Metodo de herança indireta

# basicamente funciona como uma 'escada' uma classe vai herdando da outra, e depois outra classe herda da classe que herdou
# ex

# classe filha ---> herda da classe mãe

# classe neta ---> herda da classe filha

# porem todas as propriedades da classe mãe que fora herdadas pela classe filha, serão herdadas tbm pela classe neta!!

#  ex

class Vo:

    def __init__(self, cabelo, olhos):
        self.__cabelo = cabelo
        self.__olhos = olhos

    @property
    def cabelo(self):
        return self.__cabelo

    @property
    def olhos(self):
        return self.__olhos


class Mae(Vo):

    def __init__(self, cabelo, olhos, boca, pele):
        super().__init__(cabelo, olhos)
        self.__boca = boca
        self.__pele = pele


    @property
    def boca(self):
        return self.__boca

    @property
    def pele(self):
        return self.__pele


class Neta(Mae):

    def __init__(self, cabelo, olhos, boca, pele, altura):
        super().__init__(cabelo, olhos, boca, pele)
        self.__altura = altura

    @property
    def altura(self):
        return self.__altura



apolo = Neta('loiro','azuis','carnuda','branca',1.10)

print(apolo.cabelo)
print(apolo.olhos)
print(apolo.boca)
print(apolo.pele)
print(apolo.altura)

# loiro
# azuis
# carnuda
# branca
# 1.1

# classe Mae herdou da classe Vo e classe Neta herdou da classe mae, que herda da classe Vo 
# logo indiretamente Neta herda das duas classes, todos os metodos e atributos




# MRO -- method resolution Order


class Estado:
# vou criar os atributos de forma publica, o intuito é só mostrar como o MRO atua e não criar um sistema
    def __init__(self,nome):
        self.nome = nome


    def apresentar(self):
        return f'Eu sou {self.nome} e estou em algum estado por ai'



class Bahia(Estado):

    def __init__(self, nome):
        super().__init__(nome)


    def apresentar(self):
        return f'Eu sou {self.nome} e estou na bahia'


class Alagoas(Bahia):

    def __init__(self, nome):
        super().__init__(nome)

    def apresentar(self):
        return f'Eu sou {self.nome} e estou em Alagoas'



class Nordeste(Alagoas):

    def __init__(self, nome):
        super().__init__(nome) # quando temos atributos identicos em todas classes que herdam de forma direta, podemos usar o constructor, caso contrario opte por usar a sintaxe  ---> NomeDaClasse.__init__(self, atributos)

    def apresentar(self):
        return f'Eu sou {self.nome} e estou no nordeste'



turista = Nordeste('Gerson')

print(turista.apresentar()) # Eu sou Gerson e estou no nordeste

# podemos acessar a hierarquia de metodos, ocorre um override, ou seja, note que temos os mesmos metodos em todas as classes, se mudarmos o nome do metodo dentro de Nordeste e usar o mesmo comando turista.apresentar() ele vai chamar o proximo metodo na hierarquia que é o metodo apresentar da classe Alagoas, entao turista.apresentar() teria como retorno 'Eu sou gerson e estou em alagoas' e assim por diante, se voce mudar o nome do metodo na classe Alagoas, ele vai chamar o proximo na hierarquia que é o apresentar() da classe Bahia

# para ver qual é essa 'hierarquia' usamos o dunder __MRO__

# print(turista.__mro__) <class '__main__.Nordesde'>, <class '__main__.Alagoas'>, <class '__main__.Bahia'>, <class '__main__.Estado'> # mostra qual a hierarquia da esquerda para direita

