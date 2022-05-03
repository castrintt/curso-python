# são metodos que possuem o dunder (__metodo__) em seus nomes.

# ex

# __init__ , __name__ , __main__ e etc...

# METODOS MAGICOS SÃO 'MONTADOS' DENTRO DA CLASSE!!!

# para trabalhar com classes temos alguns metodos magicos 
# são eles

"""
__init__ # - constroi o objeto (instanciado por uma classe)

__repr__ # - monta uma representação para cada objeto que foi instanciado pela classe, quando usamos o print(nome_objeto) ele nos retorna um endereço de memoria, porem, se houver dentro da classe declarado um metodo magico que monta uma representação do objeto, ao usarmos a função print(nome_objeto) ele vai printar na tela a representação montada dentro do __repr__

__str__  # - deve retornar uma representação em forma de string do valor do objeto

__len__ # - ele define qual atributo vai retornar o len() dentro do seu retorno
 
__del__ # praticamente avisa ao usuario que algum objeto foi deletado, ao usar o metodo : del nome_do_objeto

__sub__ para -

__mul__ para *

__truediv__ para /

floordiv para //

__mod__ para %

__pow__ para **

__and__ para &

__or__ para |

__it__ para <

__le__ para <=

__eq__ para ==

__ne__ para !=

__gt__ para >

__ge__ para >=

__len__ para len()

__getitem__ para indexar

__setitem__ para asignar valores indexados

__delitem__ para borrar valores indexados

__iter__ para iteración sobre objetos

__contains__ para in


"""

# esse são os mais usados, obviamente possuem outros

# vamos conhecer esses metodos

# ex

from unittest import result


class Carro:

    # constructor 
    def __init__(self,cor,portas,valor,ano): # metodo magico __init__ (constroi uma instancia da classe -- um objeto)
        self.cor = cor
        self.portas = portas
        self.valor = valor
        self.ano = ano


    def __repr__(self): # # o metodo magico __repr__ é uma forma de visualizar oque contem no objeto -- ele monta uma representação de objetos que foram instanciados pela classe onde ele foi declarado!
       return f'{self.portas} portas e ano {self.ano}'


    def __str__(self): # # tambem é um metodo magico que monta uma representação dos objetos que foram instanciados pela classe, tem o mesmo proposito que o __repr__, porem ele é 'mais forte' que o metodo repr, ou seja ele prevalesse 
        return f' Carro {self.cor} que vale {self.valor}'


    def __add__(self,other):
        return f'{self}.... {other}'


    def __mul__(self,other):
        if isinstance(other,int): # isinstance verifica se a variavel é de algum tipo de dado especifico (no caso verifica se other é um valor inteiro)
            result = ' '
            for i in range(other):
                result += ' ' + str(self)
            return result
        return 'É necessario numero inteiro para multiplicar'


    def __len__(self): # retorna um tamanho para um atributo especifico 
        return len(self.cor)

    def __del__(self):
        print(f'{self} Deletado!')



# instanciando 2 carros
carro_1 = Carro('prata',4,30000,2011)

carro_2 = Carro('vermelho',2,13000,2016)


# ao printar vamos receber no console oque está no retorno do metodo magico __str__ (por conta da ordem de preferencia), caso só tenha o __repr__ é ele que vai ser representado
print(carro_1) 
print(carro_2) 

#  Carro prata que vale 30000
#  Carro vermelho que vale 13000

print(carro_1 + carro_2) # Carro prata que vale 30000....  Carro vermelho que vale 13000  # usando o metodo magico __add__


print(carro_1 * 4) #  Carro prata que vale 30000  Carro prata que vale 30000  Carro prata que vale 30000  Carro prata que vale 30000 # usando metodo magico __mul__

print(len(carro_1)) # 5 # o tamanho da string cor


del carro_1
#  Carro prata que vale 30000 Deletado!
#  Carro vermelho que vale 13000 Deletado!





# TODOS OS METODOS MAGICOS VEM DA CLASSE CHAMADA object, a nossa classe Carro, somente herdou eles
# object é uma classe padrao do python


print(dir(object))

# ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']