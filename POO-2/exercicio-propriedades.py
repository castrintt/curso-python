# 1 ) Crie uma classe contendo atributos privados representando um jogo.
# Apos isso, cria uma propriedade para cada atributo privado. Instancie um objeto e faça acesso a todos os atributos.
# Utilize tbm o setter, para alterar algum valor do objeto


class Diablo:

    def __init__(self, classe):
        self.__classe = classe
        self.__inteligencia = 0
        self.__forca = 0
        self.__destreza = 0

    
    @property
    def inteligencia(self):

        if self.classe == 'barbaro':
            self.__inteligencia = 20
        elif self.classe == 'feiticeiro':
            self.__inteligencia = 80
        elif self.classe == 'caçador':
            self.__inteligencia = 60

        return self.__inteligencia

    
    @property
    def forca(self):

        if self.classe == 'barbaro':
            self.__forca = 80
        elif self.classe == 'feiticeiro':
            self.__forca = 20
        elif self.classe == 'caçador':
            self.__forca = 40

        return self.__forca


    @property
    def destreza(self):

        if self.classe == 'barbaro':
            self.__destreza = 40
        elif self.classe == 'feiticeiro':
            self.__destreza = 30
        elif self.classe == 'caçador':
            self.__destreza = 80

        return self.__destreza


    @property
    def classe(self):
        return self.__classe

    
    @classe.setter
    def altera_classe(self, nova_classe):
        self.__classe = nova_classe
        return self.__classe




czar = Diablo('caçador')

print(czar.classe) # caçador
print(czar.forca) # 40
print(czar.inteligencia) # 60
print(czar.destreza) # 80


czar.altera_classe = 'barbaro'


print(czar.classe) # barbaro
print(czar.forca) # 80
print(czar.inteligencia) # 20
print(czar.destreza) # 40