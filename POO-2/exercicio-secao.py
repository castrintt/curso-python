""" 
   1 ) Crie  uma superclasse chamada 'Pessoa' que recebe como atributo nome, cpf e salario. 
   Após isso, construa a Classe Filha: 'Funcionario', que possui o metodo sem parametros chamado 'promocao', que apenas acrescenta 10% no salario a algum funcionario.
   Por sua vez, a classe 'Funcionario' deve ser Classe Mãe de outras duas classes: 'Gerente' e 'Estagiario', e ambos precisam ter o atributo 'codigo' em seu método construtor.
   Além disso, o gerente precisa do atributo 'numEstagiarios', representando a quantidade de funcionarios que ele é responsavel.
   Ainda na classe gerente deve haver um metodo que possibilite a alteração do codigo dos estagiarios, sendo que os estagiarios não tem acesso a troca de codigo.
   Instancia 3 estagiarios e 1 gerente. Dê promoção para os dois primeiros estagiarios e para o gerente

   # obs - utilize tambem um metodo magico para representar as classes 'Estagiario' e 'Gerente', e propriedades para acessar os atributos de 'Pessoa'.
"""

class Pessoa:

    def __init__(self, nome, cpf , salario):
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = salario

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf


    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def altera_salario(self, aumento):
        self.__salario = aumento


class Funcionario(Pessoa):

    def __init__(self, nome, cpf, salario):
        super().__init__(nome, cpf, salario)

    def promocao(self):
        self.altera_salario *= 1.1
        return self.altera_salario



class Gerente(Funcionario):

    def __init__(self, nome, cpf, salario, codigo, num_estagiarios):
        super().__init__(nome, cpf, salario)
        self.__codigo = codigo
        self.__num_estagiarios = num_estagiarios

    
    @property
    def codigo(self):
        return self.__codigo

    @property
    def num_estagiarios(self):
        return self.__num_estagiarios

    def altera_codigo(self, estagiario, novo_codigo):
        estagiario._Estagiario__codigo = novo_codigo
        return estagiario._Estagiario__codigo

    def __str__(self):
        return f'Nome gerente: {self.nome}\nCpf gerente: {self.cpf}\nSalario gerente: {self.salario}\nCodigo gerente: {self.codigo}\nNumero de estagiarios: {self.num_estagiarios}'





class Estagiario(Funcionario):

    def __init__(self, nome, cpf, salario, codigo):
        super().__init__(nome, cpf, salario)
        self.__codigo = codigo

    
    @property
    def codigo(self):
        return self.__codigo

    def __str__(self):
        return f'Nome estagiario(a): {self.nome}\nCpf estagiario(a): {self.cpf}\nSalario estagiario(a): {self.salario}\nCodigo estagiario(a): {self.codigo}'

# instanciar 3 estagiarios e 1 gerente

# Gerente

tiago = Gerente('tiago de Castro','8080796943',20000.00,'abr1239s',3)

print(tiago)
# Nome gerente: Roberto Antunes
# Cpf gerente: 8080796943
# Salario gerente: 20000.0
# Codigo gerente: abr1239s
# Numero de estagiarios: 3
print('\n')


# Estagiarios

igor = Estagiario('Igor de Castro','2134213231',3200.00,'ss8fkk2')

print(igor)
# Nome estagiario(a): Igor de Castro
# Cpf estagiario(a): 2134213231
# Salario estagiario(a): 3200.0
# Codigo estagiario(a): ss8fkk2
print('\n')

isabela = Estagiario('Isabela de Castro','18927321893',3200.00,'sis12k3')

print(isabela)
# Nome estagiario(a): Isabela de Castro
# Cpf estagiario(a): 18927321893
# Salario estagiario(a): 3200.0
# Codigo estagiario(a): sis12k3
print('\n')

camila = Estagiario('Camila de castro','12312341434',3200.00,'lovd12ss')

print(camila)
# Nome estagiario(a): Camila de castro
# Cpf estagiario(a): 12312341434
# Salario estagiario(a): 3200.0
# Codigo estagiario(a): lovd12ss
print('\n')

tiago.altera_codigo(camila,'hhh32s') # alterando codigo de estagiario

print(camila)

# Nome estagiario(a): Camila de castro
# Cpf estagiario(a): 12312341434
# Salario estagiario(a): 3200.0
# Codigo estagiario(a): hhh32s
print('\n')

# promoção gerente
tiago.promocao()

print(tiago)
# Nome gerente: tiago de Castro
# Cpf gerente: 8080796943
# Salario gerente: 22000.0 # aumentou
# Codigo gerente: abr1239s
# Numero de estagiarios: 3

print('\n')

igor.promocao()

print(igor)
# Nome estagiario(a): Igor de Castro
# Cpf estagiario(a): 2134213231
# Salario estagiario(a): 3520.0 # alterado
# Codigo estagiario(a): ss8fkk2
print('\n')

isabela.promocao()

print(isabela)
# Nome estagiario(a): Isabela de Castro
# Cpf estagiario(a): 18927321893
# Salario estagiario(a): 3520.0 # aumentou
# Codigo estagiario(a): sis12k3

