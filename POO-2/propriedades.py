# O metodo pythonico de trabalhar é criando somente atributos privados dentro do construtor, e criar metodos para acessar esses atributos privados

# metodos publicos utilizados para manipular atributos/ metodos privados

# 1 ) propriedades (atuam como getters)  -->  @property

# Propriedades decoram os atributos publicos ( em javascript nós temos os metodos getters e setters ) --> onde get acessa atributo e set altera

#OBS AO DECLARAR O @property NÃO PRECISAMOS MAIS CHAMAR O METODO DA FORMA NORMAL ( objeto.metodo() ) podemos chama-los como se fossem atributos ( objeto.metodo )

# ex py

class Celular:
    
    def __init__(self,data,senha,saldo):
        self.__data = data
        self.__senha = senha
        self.__saldo = saldo
    
    @property
    def data(self):
        return f'Data de hoje: {self.__data}'


    @property
    def senha(self):
        return self.__senha # dessa forma você simplismente apresenta a senha para o usuario sem que ele possa altera-la via programa


    @property
    def saldo(self):
        return self.__saldo # dessa forma não permite o usuario manipular o saldo manualmente (sem depositar ou sacar )


# OU SEJA A IDEIA DE PROPRIEDADES É BASICAMENTE TER ACESSO AOS ATRIBUTOS PRIVADOS!

iphone = Celular('23/02/2023','112358','30 reias de saldo')

print(iphone.senha) # 112358

print(iphone.saldo) # 30 reias de saldo

# UMA PROPRIEDADE PODE MANIPULAR MAIS DE UM ATRIBUTO!


# 2 ) setter (atuam como set) --> altera o valor de uma PROPRIEDADE -->  @propriedade.setter

# DESSA FORMA PODEMOS SOMENTE VISUALIZAR OS DADOS, MAS COMO PODEMOS AGORA ALTERA-LOS????

# para declarar que uma função é um setter usando a seguinte sintaxe como decorador

# @nome_do_atributo_a_ser_alterado.setter
# def nome_funcao(self, parametro de mudança):
    # codigo

# usando o exemplo a cima
# suponha que o usuario queira mudar a senha, como fariamos isso? se o property só acessar ( funciona como getter )?
# criariamos outro metodo 

# veja

class Celular:
    
    def __init__(self,data,senha,saldo):
        self.__data = data
        self.__senha = senha
        self.__saldo = saldo
    
    @property
    def data(self):
        return f'Data de hoje: {self.__data}'


    @property
    def senha(self):
        return self.__senha # dessa forma você simplismente apresenta a senha para o usuario sem que ele possa altera-la via programa


    @property
    def saldo(self):
        return self.__saldo # dessa forma não permite o usuario manipular o saldo manualmente (sem depositar ou sacar )

    
    @senha.setter # nome da PROPRIEDADE a ser alterada. setter
    def altera_senha(self,nova_senha):
        self.__senha = nova_senha
        return self.__senha

# propriedade (get) acessa um atributo

# setter acessa uma propriedade e muda ela 

iphone = Celular('23/02/2022','112358','30 reais')

print(iphone.senha) # 112358

iphone.altera_senha = '40029822'

print(iphone.senha) # 40029822