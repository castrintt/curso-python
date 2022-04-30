# são funções como quaisquer outras

# Basicamente metodos são divididos em dois grupos:
# metodos de instancia e metodos de classe.


#   1 ) METODOS DE INSTANCIA (ACESSADOS SOMENTE PELO OBJETO , APÓS SEREM INSTANCIADOS PELA CLASSE)

# eles precisam de uma instancia da classe (instancia e objetos são a mesma coisa) para ser usado.

#  1.1) metodo construtor (constructor)
# conhecido tbm como metodo magico( assim como outros que começam e terminam com dunder [__ __])
# possui esse nome pois controi objetos da classe a que pertence, ou seja, serve para instancia objetos a classe que ele pertence
# instancia o objeto pato pertencente a classe animais


# sintaxe:  def __init__(self, parametros):
                    # bloco

# SELF - é o proprio objeto, self é uma forma de referenciar esse objeto (foque na palavra ESSE) ---> (self tem o mesmo conceito de THIS no javascript)
# SELF é o objeto / instancia --> é convencional pode usar qualquer nome


 # ex

from xml.sax.handler import feature_external_ges


class Carro:
    def __init__(self, portas, cor):
        # atributos(caracteristicas do carro)
        self.portas = portas # publico
        self.cor = cor # publico
        self.__arcondicionado = True # privado
        #ou seja, o meu proprio objeto (self) esta recebendo o atributo portas e cor
# nota a seguinte sintaxe self.__arcondicionado = True, QUANDO PASSAMOS UM ATRIBUTO OU CLASSE COM 2 UNDERLINES QUEREMOS DIZER QUE SÃO ATRIBUTOS OU CLASSES PRIVADOS
# nossa classe foi criada, agora vamos instanciar um objeto criando o objeto ferrari

ferrari = Carro('4 portas','preta')

print(ferrari) #  <__main__.Carro object at 0x7f6d6e364460>


# PARA ACESSAR UM ATRIBUTO DE UMA CLASSE ACESSAMOS USANDO O PONTO ( . ), por exemplo para acessar o atributo portas do objeto ferrari --> ferrari.portas
# A FORMA DE ACESSAR UM OBJETO É IDENTICA A FORMA QUE ACESSAMOS OBJETOS EM JAVASCRIPT
# ex


print(ferrari.portas) # 4 portas # retorna o valor do atributo portas do objeto ferrari

print(ferrari.cor) # preta # retorna o valor do atributo cor do objeto ferrari


# __arcondicionado é um atributo privado da classe Carro, oque aconteceria se tentassemos acessar ele?

# print(ferrari.__arcondicionado) # AttributeError: 'Carro' object has no attribute '__arcondicionado'
# como é um atributo privado ele não pode ser acessado por um objeto



# ATRIBUTO DE CLASSE

# são atributos usados fora do construtor, porem dentro da classe, para acessarmos ele dentro de um metodo (como o constructor por exemplo), devemos chamar a instancia da propria classe
# sintaxe : classe Cliente:
                #servico = 'contratado'
                #def __init__(self,nome,cpf):
                    #Cliente.servico = False    # ---> acessamos a instancia da classe Cliente e seu atributo de classe 'servico'

# LEMBRANDO QUE ATRIBUTOS DE CLASSE PODEM SER ACESSADOS DA MESMA FORMA POR UM OBJETO :  nome_objeto.nome_atributo, são praticamente atributos (estaticos)

# ex

class Sapato:
    qtd = 7 # atributo de classe
    def __init__(self, cor, tamanho, preco, qtdCompra): # atributos dentro do metodo
        self.cor = cor
        self.tamanho = tamanho
        self.preco = preco
        self.qtdCompra = qtdCompra
        Sapato.qtd += self.qtdCompra
# vamos instanciar um objeto agora, usando a classe acima

tamanco = Sapato('preto',40,40.00,2)

print(tamanco.qtd) # 9  # retorna 9 pois declaramos dentro do construtor que o atributo de classe qtd = 7 agora recebe a soma da quantidade comprada (Sapato.qtd += self.qtdCompra)
# e como a qtdCompra do objeto tamanco é 2, 2 + 7 = 9.

print(Sapato.qtd)


# agora vamos supor que nunca tivemos o objeto tamanco sendo instanciado pela classe Sapato

print(Sapato.qtd) # 7 , ainda poderiamos acessar o atributo de classe, usando a propria instancia da classe:   instancia_da_classe.nome_atributo_de_classe



# CRIANDO METODOS --> (que são basicamente atributos que atuam como funções)
# todos os metodos criados dentro da classe pertencem aos objetos instanciados por ela

# lembrando que os metodos criados, são metodos de instancia ou seja, você não consegue chamar uma classe e usar eles, somente depois que instanciamos um objeto com a classe que podemos acessar eles via objeto

class Computador:
    def __init__(self,cor,peso,polegadas,ligado):
        self.cor = cor
        self.peso = peso
        self.polegadas = polegadas
        self.ligado = ligado

    # criando metodos de ligar e desligar o computador
    def ligar(self): 
        self.ligado = True
        return self.ligado

    def desligar(self):
        self.ligado = False
        return self.ligado

    def memoria(self,ram): 
        self.ram = ram


acer = Computador('preto',13,20,False)

print(acer.ligado) # False
# vamos agora chamar o metodo ligar


acer.ligar() # acessando o metodo ligar da classe Computador

print(acer.ligado) # True

 
acer.desligar() # acessando o metodo desligar da classe Computador


print(acer.ligado) # True


# Vamos agora acessar o metodo ram (porem note que o metodo ram tem um parametro ram, logo devemos primeiro acessar esse metodo instanciando esse parametro)

acer.memoria('8gb') # acessando o metodo memoria, e criando uma instancia ram


print(acer.ram) # 8gb # acessando a instancia ram




# OBS -->>  SEMPRE EVITE CRIAR METODOS USANDO DUNDER --> pode haver conflito com alguns metodos internos da linguagem.
# ex: __name__ e __main__

# OBS2 --> nome de metodos possuem APENAS letras minusculas. Em caso de haver mais de uma palavra, separar pelo underline (como a nomenclatura de uma função normal!)
# ex: def controle_remoto() , def mae_pai_filho_filha()



#      2) METODOS DE CLASSE

# - Necessario utilizar um decorador: @classmethod

# - Não há a utilização do self, ele utiliza o parametro 'cls' que se refere a propria classe
# é a mesma ideia do self, porem o self se referencia a propria instancia (ao proprio objeto) , ja o cls se referencia a classe

# sintaxe :
    # @classmethod
    # def nome_metodo(cls):

# o metodo de classe não tem acesso aos atributos dos objetos, pois ele apenas recebe CLS e não SELF
# ou seja, metodod e classe não faz acesso a atributos de objeto/instancia

# ex (usando a mesma classe criada para metodos de instancia --> Computador)

class Computador:
    peixes = 98

    @classmethod
    def conta_peixes(cls):
        print(f'Nome da class: {cls}')
        print(f'Existe {cls.peixes} peixes dentro da classe {cls}') # cls.peixes é como se estivessemos fazendo isso -->> Computador.peixes

    
    def __init__(self,cor,peso,polegadas,ligado):
        self.cor = cor
        self.peso = peso
        self.polegadas = polegadas
        self.ligado = ligado

    def memoria(self,ram): 
        self.ram = ram


Computador.conta_peixes()

# Nome da class: <class '__main__.Computador'>
# Existe 98 peixes dentro da classe <class '__main__.Computador'>







# ___________ SUBTIPOS ______________

# Construtor - constroi um objeto
# publicos - metodos/ atributos acessados pelos objetos instanciados pela classe
# privados - metodos/ atributos que não podem ser acessados pelos objetos instanciados pela classe
# estaticos

# nós ja vimos atributos publicos, construtores, vamos ver agora os privados e estaticos


# 1)  PRIVADOS

# ex usando como exemplo da classe Computador

# atributos ou metodos privados tem como sintaxe: def __nome_metodo(self):   ou self.__nome_atributo = atributo

# acessamos dessa forma
# objeto._NomeClasse__atributo/metodo()

class Computador: 
    def __init__(self,cor,peso,polegadas,ligado):
        self.cor = cor
        self.peso = peso
        self.polegadas = polegadas
        self.ligado = ligado

    def __caracteristicas(self):
        return f'{self.cor} e {self.peso}'


novoComputador = Computador('preto',20,20,True)


# print(Computador.__caracteristicas()) # AttributeError: type object 'Computador' has no attribute '__caracteristicas'

# se tentarmos acessar um atributo privado, vai retornar um erro AttributeError

# PARA ACESSARMOS UM METODO OU ATRIBUTO PRIVADO BASTA ACESSAR O DIR DA CLASSE, que mostra tudo oq podemos fazer com a classe

# ex

print(dir(Computador))

# ['_Computador__caracteristicas', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']

# note que exite  _Computador__caracteristicas --> que é um atributo/metodo privado

# portando para acessar devemos fazer o seguinte

print( novoComputador._Computador__caracteristicas() ) # preto e 20

# dessa forma conseguimos acessa-lo
# essa tecnica se chama # name Mangling


# usando o exemplo da classe Carro


class Carro:
    def __init__(self, portas, cor):
        self.portas = portas
        self.cor = cor 
        self.__arcondicionado = True

ferrari = Carro('4 portas','preta')
 
print(ferrari._Carro__arcondicionado) #True # acessamos um atributo privado



# POR TANTO PARA ACESSAR UM ATRIBUTO/METODO PRIVADO DEVEMOS USAR A SINTAXE:

# objeto._NomeClasse__atributo/metodo()


# 2) ESTATICOS

# Necessario utilizar um decorador: @staticmethod
# basicamente é um metodo que não muda
# a diferença entre metodo de classe e um metodo estatico é que o estatico não recebe parametros (cls, self e etc...)

# - SEM PARAMETROS (METODOS ESTATICOS NÃO RECEBEM PARAMETROS)
# PODEMOS ACESSAR O METODO ESTATICO TANTO PELA CLASSE QUANTO PELO OBJETO INSTANCIADO POR ELA

# ex

class Cliente:
    @staticmethod
    def especial():
        print('Você é um cliente especial')
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade


maria = Cliente('Maria',23)

print(maria.nome) # maria
print(maria.idade) # 23                  

maria.especial() # Você é um cliente especial
Cliente.especial() #  Você é um cliente especial