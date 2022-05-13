# aplique assert's no codigo abaixo e descreva o que o programa faz

class ContaCorrente:

    def __init__(self, nome,num_conta,saldo=0.0):
        self.__nome = nome
        self.__num_conta = num_conta
        self.__saldo = saldo
        assert self.__saldo == 0.0 , 'Saldo não pode iniciar com valor diferente de 0.0 reais'

    @property
    def nome(self):
        return self.__nome

    @property
    def saldo(self):
        return self.__saldo

    @property
    def num_conta(self):
        return self.__num_conta

    def deposito(self, valor):
        self.__saldo += valor
        return self.__saldo

    def saque(self,valor):
        self.__saldo -= valor
        assert self.__sado < valor , 'Valor de saque indisponivel'
        return self.__saldo

pessoa1 = ContaCorrente('Sandro',123123)

pessoa2 = ContaCorrente('Vanessa',129382,500.0)

# descrevendo o codigo

# --> o codigo está criando uma classe chamada ContaCorrente, que recebe na sua função construtora(def __init__) os argumentos/ parametros (self) que é sua propria instancia, nome, numero de conta e o saldo que ja foi inicializado com o valor de 0.0 (flutuante), foram criadas propriedades para que o usuario possa acessar os atributos definidos dentro do construtor, porem não podem altera-los. Também foram criados 2 metodos (2 funções) uma de saque, e uma de deposito, ambas alteram o valor de self.__saldo, logo depois disso foram instanciados 2 objetos usando a classe ContaCorrente, são eles pessoa1 e pessoa2 , porem pessoa2 está iniciando o saldo (argumento do construtor) com um valor diferente de 0.0.