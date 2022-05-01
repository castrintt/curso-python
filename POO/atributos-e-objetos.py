# 1) atributos - são caracteristicas do objeto que a classe ira controlar

# classe Carro pode ter atributos --> potencia, cor, numeros de bancos, teto_solar

# 2)  objeto é justamente o objeto da vida real que sera controlado no programa

# dentro da classe Carro poderiamos ter varias instancias dela, ferrari,bugatti, gol, uno e etc...



#  1) OBJETOS

class Carro:
    def __init__(self):
        print(self) # self é o objeto em si


ferrari = Carro()  # <__main__.Carro object at 0x7f012f3f6040> # criamos o objeto ferrari que sera controlado pela classe Carro

# por baixo dos panos oque acontece?

# por debaixo dos panos depois de referenciar o objeto com a classe Carro. é como se a palavra __ini__ (constructor) fosse substituida por Carro e ferrari passasse a ser o primeiro atributo

# ficaria assim --> ferrari = Carro(ferrari), todo metodo de instancia deve receber a palavra reservada self, para se referenciar ao objeto



# 2) ATRIBUTOS - temos 3 tipos de atributos --> atributos de instancia(só podem ser acessados pelo objeto instanciado pela classe  [ self ]), atributos de classe (só podem ser acessados pela classe[ cls ]) e atributos dinamicos

# OBS PODEMOS ACESSAR ATRIBUTOS (visualizando eles por meio de um dicionario) dunder dict
# sintaxe: nome_objeto.__dict__ --> usando o dunder dict, podemos visualizar o objeto como --> chave = nome_atributo  , valor = valor_atributo

# ex

class ControleRemoto:
    def __init__(self, botoes,ligado,desligado,cor) :
        self.botoes = botoes
        self.ligado = ligado
        self.desligado = desligado
        self.cor = cor


controle = ControleRemoto('4 botoes',True,False,'branca')
# usando dunder dict para visualizar o dicionario criado

print(controle.__dict__) # {'botoes': '4 botoes', 'ligado': True, 'desligado': False, 'cor': 'branca'}






# 2.1) Atributos de instancia -- atributos declarados dentro do metodo constructor

# ex

class Cliente:
    def __init__(self,nome,cpf,idade,corDeCabelo,altura):
        # nesse caso --> nome, cpf, idade, corDeCabelo e altura são atributos de instancia --> foram criados dentro de uma função construtora (que usa o __init__ [ dunder init ] como nome)
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.corDeCabelo = corDeCabelo
        self.altura = altura
        # acima estamos referenciando todas as instancias de Cliente com os parametros, ou seja, toda instancia vai ter um atributo nome (que foi delimitado por self.nome [ ela mesma.atributo  basicamente ])
        self.estado = False
        # estado está checando se o carro esta desligado ou não


# igor = Cliente() # se rodarmos o programa assim ira retornar um erro, pois o objeto igor esta esperando 5 argumentos(nome,cpf,idade,corDeCabelo, altura)
# o correto é usarmos assim

igor = Cliente('igor',12390128390128903,23,'castanho',1.80)
# agora poderemos acessar todas propriedades do objeto igor (nome, cpf e etc...)

print(igor.nome) # igor
print(igor.cpf) # 12390128390128903
print(igor.idade) # 23
print(igor.corDeCabelo) # castanho
print(igor.altura) # 1.8

# Esses são atributos de instancia



# 2.2) Atributos de classe - são atributos que são criados fora de qualquer metodo(função) que ESTEJA DENTRO DA CLASSE (ou seja os atributos ainda são criados dentro da classe)

#A PRINCIPAL CARACTERISTICA DE ATRIBUTOS DE CLASSE É --> que todos os atributos de classe servem para todos os objetos instanciados por ela

# para acessar um atributo de classe devemos usar a seguinte sintaxe: 
# sintaxe: --> NomeDaClasse.atributo_de_classe
#lembrando que podemos acessar dessa forma : NomeDaClasse.atributo_de_classe , dentro e fora da classe

# ex

class Musica:
    # rock e sertanejo nesse caso são atributos de classe
    rock = 'muito bom'
    sertanejo = 'horrivel'

    def __init__(self,nomeMusica,discosVendidos):
        self.nomeMusica = nomeMusica
        self.discosVendidos = discosVendidos



ledZeppelin = Musica('stair away to heaven','milhoes')

print(ledZeppelin.nomeMusica) # stair away to heaven
print(ledZeppelin.discosVendidos) # milhoes


# note que quando acessamos o atributo de classe, ele reflete tanto para a chamada da classe --> NomeDaClasse.atributo_de_classe,   quanto para os objetos instanciados por ela --> objeto.atributo_de_classe

print(Musica.rock) # muito bom
print(Musica.sertanejo) # horrivel

print(ledZeppelin.rock) # muito bom
print(ledZeppelin.sertanejo) # horrivel


# Outro exemplo de atributo de classe # incrementando um atributo de instancia com um atributo de classe


class Carro:

    nitro = 1.1 # sera adicionado 10% na velocidade total do carro

    def __init__(self, velocidade,potencia,num_bancos):
        self.velocidade = velocidade * Carro.nitro # incrementando o atributo de instancia com um atributo de classe --> temos que chama-lo dessa forma, pois estamos nos referenciando a propria classe e não a sua instancia
        self.potencia = potencia
        self.num_bancos = num_bancos


ferrari = Carro(20,20,4)

print(ferrari.velocidade) # 22.0 # --> note que passamos a velocidade como 20, e o retorno foi de 22, logo entendemos que o atributo de classe 'nitro' incrementou de fato o atributo de instancia 'self.velocidade'
print(ferrari.nitro) # 1.1 --> lembrando que independente de ser um atributo de classe, todas suas instancias (objetos) podem acessa-los
#tanto como a propria classe
print(Carro.nitro) # 1.1

# lembrando que podemos acessar dessa forma : NomeDaClasse.atributo_de_classe , dentro e fora da classe

# Agora se tentarmos acessar um atributo de instancia pela classe, não vai dar certo

#print(Carro.potencia) # AttributeError: type object 'Carro' has no attribute 'potencia'



# QUAL A VANTAGEM DE USAR ATRIBUTOS DE CLASSE? 

# -> ele ocupam menos espaço na memoria, pois requer somente 1 espaço para todos os objetos, enquanto atributos de instancia, cada um deles ocupa 1 espaço dentro do objeto



# 2.3) atributos dinamicos: são atributos criados ao longo do programa, ou seja, eles são criados e acessados SOMENTE pelos objetos que o criaram
# está vinculado SOMENTE ao objeto que o criou

# para criarmos um atributo dinamico, primeiro temos que criar uma instancia de uma classe(objeto), logo após isso, podemos referenciar um atributo que ainda não existe, usando a sintaxe:

# nome_do_objeto.novo_atributo = valor_atributo

# ex

class Animal:
    def __init__(self,nome,peloLiso):
        self.nome = nome
        self.peloLiso = peloLiso


pato = Animal('pato',False)

print(pato.nome) # pato
print(pato.peloLiso) # False

# patos não possuem pelo, possuem pena, então nesse caso há a necessidade da criação de um novo atributo para esse objeto

pato.pena = True

# criamos um novo atributo para o objeto pato, chamado pena com valor True
# vamos acessa-lo agora

print(pato.pena) # True # note que oa tributo foi criado

# porem SOMENTE para esse objeto, vamos criar outro objeto e tentar acessar esse mesmo atributo 'pena' (retornara um erro, mas vamos provar)


leao = Animal('leao',True)

print(leao.nome) # leao
print(leao.peloLiso) # True

# agora vamos acessar leao.pena (atributo criado dinamicamente SOMENTE para o objeto pato)

# print(leao.pena) # AttributeError: 'Animal' object has no attribute 'pena'

# isso serve tbm para a classe, a classe não consegue acessar esse atributo, pois ele foi criado SOMENTE para o objeto pato, vejamos:

#print(Animal.pena) # AttributeError: type object 'Animal' has no attribute 'pena'



# PODEMOS TBM CRIAR UM METODO QUE CRIA UM NOVO ATRIBUTO PARA UM OBJETO:
# ex

class Carro:
    def __init__(self, velocidade,potencia,num_bancos):
        self.velocidade = velocidade 
        self.potencia = potencia
        self.num_bancos = num_bancos

    def cria_atributo(self): # somente os objetos que usarem esse metodo terão esse atributo
        self.cor = 'preto'


ferrari = Carro(20,20,4)

print(ferrari.velocidade) # 20
print(ferrari.potencia)  # 20
print(ferrari.num_bancos) # 4

# invocando o metodo cria_atributo para o objeto ferrari

ferrari.cria_atributo()

print(ferrari.cor) # preto, agora ferrari tem um atributo cor

# vejamos agora oque acontece se criarmos um objeto novo, e tentarmos acessar esse mesmo atributo cor (SEM INVOCAR O METODO)

jaguar = Carro(30,30,2)

print(jaguar.velocidade) # 30
print(jaguar.potencia) # 30
print(jaguar.num_bancos) # 2


#print(jaguar.cor) # AttributeError: 'Carro' object has no attribute 'cor # retorna um erro, pois esse atributo não existe para essa instancia (objeto)









# 3) COMO DELETAR ATRIBUTOS --> usamos o metodo del

# sintaxe: --> del nome_objeto.atributo_a_ser_deletado

class Carro:
    lala = 'lala'
    def __init__(self,nome,cor):
        self.nome = nome
        self.cor = cor



ferrari = Carro('ferrari','branca')


print(ferrari.__dict__) # {'nome': 'ferrari', 'cor': 'branca'}

# vamos deletar agora a propriedade cor

del ferrari.cor

print(ferrari.__dict__) # {'nome': 'ferrari'}

# podemos deletar atributos dinamicos

#primeiro vamos criar um atributo novo para ferrari chamado num_portas

ferrari.num_portas = 4

print(ferrari.__dict__) # {'nome': 'ferrari', 'num_portas': 4}

# agora vamos deletar

del ferrari.num_portas

print(ferrari.__dict__) # {'nome': 'ferrari'}

# não podemos deletar atributos de classe, pois todos os objetos tem acesso a eles




# 4) subdivisao : atributos privados x publicos

# na teoria atributos publicos podem ser acessados por todos e privados não,
# porem o python por convensão tem um metodo de acessa-los

# 4.1) declarando atributos publicos

class Carro:
    def __init__(self,nome):
        self.nome = nome # declaramos um atributo publico


# 4.2) atributos privados - para declarar um atributo privado podemos simplismente declara-lo antes de 2 underlines

class Carro:
    def __init__(self):
        self.__nome = 'ferrari' # declaramos um atributo privado

    # não conseguimos acessar esses atributos por meio convensional ( nome_objeto.__atributo_privado ) # retorna um erro AttributeError pois o objeto não tem esse atributo
# e qual seria entao a forma que o python tem de acessar?
# primeiro vamos instancia a classe carro para ficar mais claro

ferrari = Carro()

# se usarmos o metodo dir no objeto ferrari, podemos ver todos os atributos e metodos que esse objeto possui

print(dir(ferrari))

# ['_Carro__nome', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']

# note que temos um metodo chamado '_Carro__nome' esse é o atributo de instancia privado da classe Carro
# e podemos acessar ele da seguinte forma:


print(ferrari._Carro__nome) # ferrari # dessa forma acessamos esse atributo privado

# esse metodo se chama MangLing
