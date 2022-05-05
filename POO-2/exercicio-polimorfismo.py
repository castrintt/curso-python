# 1 ) Crie uma superclasse cha,ada "FormaGeometrica", que possui um metodo 'calcula_area' e recebe o nome de uma figura geométrica em seu método construtor. Após isso, crie duas subclasses ('AreaQuadrado' e 'AreaCirculo') que herdam de 'FormaGeometrica' e calculam a área de sua respectiva forma. O metodo nas classes Filhas deve ter o nome 'calcula_area' , igual em sua Classe Mãe.

from math import pi

class FormaGeometrica:

    def calcula_area(self):
        return f'Area'


class AreaQuadrado(FormaGeometrica):

    def calcula_area(self, base, altura):
        return f'A area de um quadrado de base de {base} m2 e altura de {altura} m2 é igual a {base * altura}'


class AreaCirculo(FormaGeometrica):

    def calcula_area(self, raio):
        return f'A area de um circulo de raio {raio} é igual a {round(pi * (raio ** 2))}'


quadrado = AreaQuadrado()


print(quadrado.calcula_area(10,10))

circulo = AreaCirculo()

print(circulo.calcula_area(3))

