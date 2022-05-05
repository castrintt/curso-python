# - significa muitas formas

# - poli - mutias

# - morfis - formas


# por exemplo um overriding é uma representação de polimorfismo (basicamente um metodo de uma classe herdada sobreescrevendo o metodo  da classe base( mae ))

# ex

from ctypes import alignment


class Comida:
    
    def __init__(self, alimento):
        self.__alimento = alimento

    
    @property
    def alimento(self):
        return self.__alimento


    def apresentar(self):
        raise NotImplementedError('Esse erro só funciona se a sub classe implementa-lo (sobrescreve-lo)')


class Fruta(Comida):

    def __init(self, alimento):
        super().__init__(alimento)
        # Comida.__ini__(self, alimento)

    def apresentar(self):
        print(f'Sou uma fruta, voce gosta de {self.alimento}?')


    
class Carne(Comida):

    def __init__(self, alimento):
        super().__init__(alimento)
        #Comida.__init__(self, alimento)





fruta = Fruta('Laranja')
fruta.apresentar()

# Sou uma fruta, voce gosta de Laranja?


carne = Carne('Bife')
carne.apresentar() # se não criarmos um metodo apresentar para sobrescrever o metodo da classe mãe retorna o erro abaixo

# raise NotImplementedError('Esse erro só funciona se a sub classe implementa-lo (sobrescreve-lo)')
# NotImplementedError: Esse erro só funciona se a sub classe implementa-lo (sobrescreve-lo)


# porem se a classe Carne tivesse esse metodo 

# def apresentar(self):
    # return f'string'

# ele não retornaria um erro passaria tranquilo!