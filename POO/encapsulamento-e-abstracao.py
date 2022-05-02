# Encapsulamento 
# - uma classe guarda (encapsula) metodos e atributos dentro dela, gera mais segurança dentro do projeto e limita acesso de objetos a determinados atributos

# Com o encapsulamento é possivel a realização da abstracao



# Abstracao 
# -  Disponibilização para o usuario somente de metodos e atributos realmente necessários de serem apresentados. Metodos e atributos privados permanecem ocultos

# ex: voce tem acesso a ver o seu saldo no banco, mas n tem acesso para alterar manualmente o valor dele

# EX

class Jogo:
    
    nivel = 8

    def __init__(self, forca, magia, resistencia):
        self.forca = forca
        self.magia = magia
        self.resistencia = resistencia
        self.nivel = Jogo.nivel
    
    def atacar_raio(self):
        self.resistencia -= 5
        self.magia -= 10

    def atacar_soco(self):
        self.resistencia -= 10
        self.forca -= 10

    def pular_nivel(self):
         self.nivel += 1

    
    def status(self):
        print(f'Forca: {self.forca}\nMagia: {self.magia}\nResistencia: {self.resistencia}\nNivel: {self.nivel}')



player_1 = Jogo(15,50,35)
player_1.status()
# Forca: 15
# Magia: 50
# Resistencia: 35
# Nivel: 8

player_1.atacar_raio()
player_1.status()
# Forca: 15
# Magia: 40
# Resistencia: 30
# Nivel: 8

player_1.atacar_soco()
player_1.status()
# Forca: 5
# Magia: 40
# Resistencia: 20
# Nivel: 8

player_1.pular_nivel()
player_1.status()
# Forca: 5
# Magia: 40
# Resistencia: 20
# Nivel: 9

# dessa forma temos acesso a todos os atributos, logo se qualquer um chegar e mudar os atributos para 100 daria certo
# veja
player_1.forca = 100
player_1.magia = 100
player_1.resistencia = 100
player_1.nivel = 99


player_1.status()

# Forca: 100
# Magia: 100
# Resistencia: 100
# Nivel: 99

# o usuario mudou todos atributos dele
# para deixar nosso sistema do jogo mais seguro, basta tornar os atributos privados, e montar metodos onde o usuario consegue apenas visualizar
# mudando tbm o sistema de nivel 
# ficaria assim

from random import choice as ch

class Jogo:

    def __init__(self, forca, magia, resistencia):
        self.__forca = forca
        self.__magia = magia
        self.__resistencia = resistencia
        self.__nivel_jogador = 10
    
    def atacar_raio(self):
        self.__resistencia -= 5
        self.__magia -= 10

    def atacar_soco(self):
        self.__resistencia -= 10
        self.__forca -= 10

    def subir_nivel(self):
        listaNumeros = list(range(1,101))
        if ch(listaNumeros) <= 50:
            print('Subiu de nivel!')
            self.__nivel_jogador += 1
            return self.__nivel_jogador
        elif ch(listaNumeros) > 50:
            print('Precisa farmar mais!')
            return self.__nivel_jogador
    
    def status(self):
        print(f'Forca: {self.__forca}\nMagia: {self.__magia}\nResistencia: {self.__resistencia}\nNivel: {self.__nivel_jogador}')


player_1 = Jogo(20,50,40)

player_1.status()
# Forca: 20
# Magia: 50
# Resistencia: 40
# Nivel: 8


player_1.__forca = 30

player_1.status()
# Forca: 20
# Magia: 50
# Resistencia: 40
# Nivel: 8

player_1.subir_nivel()
player_1.status()
# Subiu de nivel!
# Forca: 20
# Magia: 50
# Resistencia: 40
# Nivel: 11

# por força ser um atributo privado não podemos altera-lo, somente acessar ele via status()

# Nós vamos fazer as alterações dentro da classe, para que o usuario não possa manipular os dados, SOMENTE nós
