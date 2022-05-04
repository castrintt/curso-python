# 1 ) Crie duas classes chamadas 'Homem' e 'Urso', que recebem apenas nome como parametro.
#  Estas classes devem herdar de outras dias chamadas 'Carnivoros' e 'herbivoros', que possuem dois metodos cada ('cacar_animal' e 'comer_carne' para carnivoros), ('procurar_arvore' e 'comer_folhas' para herbivoros) e herdam de uma superclasse chamada 'Animal', na qual possui os metodos 'andar' e 'correr' . Por fim, instancie dois objetos, da classe 'Homem' e da classe 'Urso' e execute todos os metodos.

# obs >: crie um metodo para as classes 'Homem' e 'Urso' representando uma ação caracteristica de cada, por exemplo, ler um livro para homem e hibernar para urso

class Animal:

    def andar(self):
        return f'Andando!'


    def correr(self):
        return f'Correndo!'



class Carnivoros(Animal):

    def cacar_animal(self):
        return f'Caçando animais!'
        
    
    def comer_carne(self):
        return f'Comendo carne!'



class Herbivoros(Animal):

    def procurar_arvore(self):
        return f'Procurando arvore!'


    def comer_folhas(self):
        return f'Comendo folhas!'
    


class Homem(Carnivoros, Herbivoros):

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome


    def ler(self, livro):
        return f'O homem {self.__nome} está lendo o livro {livro}'


class Urso(Carnivoros, Herbivoros):

    def __init__(self,nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome


    def hibernar(self):
        return f'Urso {self.__nome} esta hibernando!'




ricardo = Homem('Ricardo')
zeColmeia = Urso('Zé Colmeia')

print(ricardo.andar())
print(ricardo.correr())
print(ricardo.comer_carne())
print(ricardo.cacar_animal())
print(ricardo.comer_folhas())
print(ricardo.procurar_arvore())
print(ricardo.ler('Senhor dos aneis'))
print(ricardo.nome)

print('\n')

print(zeColmeia.andar())
print(zeColmeia.correr())
print(zeColmeia.comer_carne())
print(zeColmeia.cacar_animal())
print(zeColmeia.comer_folhas())
print(zeColmeia.procurar_arvore())
print(zeColmeia.hibernar())
print(zeColmeia.nome)