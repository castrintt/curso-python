"""
1) Desenvolva o sistema de um controle universal para uma casa. O controle deve ser a Classe-Mãe, que contem o metodo liga/desliga e é herdada por outras três classes (equipamentos controlados):

 -- ar-condicionado
 -- microondas
 -- televisão

Que controlam, respectivamente, temperatura, tempo e volume em metodos dentro das classes. Além disso, os metodos construtores das classes filhas recebem a veriavel controlado em seu valor atual por exemplo, temperaturaAtual

# obs Utilize tbm propriedades para realizar o acesso aos atributos
"""


class Controle:

    def __init__(self):
        self.__status = 'desligado'
        

    def liga_desliga(self):
        if self.__status == 'desligado':
            print(f'O aparelho esta {self.__status}\nLigando...')
            self.__status = 'ligado'
            return self.__status
        elif self.__status == 'ligado':    
            print(f'O aparelho está {self.__status}\nDesligando...')
            self.__status = 'desligado'
            return self.__status


    @property
    def status(self):
        return self.__status

    def __str__(self):
        return f'O status é {self.__status}'


class ArCondicionado(Controle):

    def __init__(self, temperatura):
        super().__init__() # mesmo não recebendo parametros no construtor, devemos indicar o super().__init__() para indicar que está recebendo self
        self.__temperatura = temperatura

    @property
    def temperatura(self):
        print(f'A temperatura é de {self.__temperatura} graus')
        return self.__temperatura

    @temperatura.setter
    def mudar_temperatura(self,nova_temperatura):
        self.__temperatura = nova_temperatura
        return self.__temperatura



class Microondas(Controle):

    def __init__(self, tempo):
        super().__init__()
        self.__tempo = tempo

    @property
    def tempo(self):
        return self.__tempo

    @tempo.setter
    def alterar_tempo(self, novo_tempo):
        self.__tempo = novo_tempo
        return self.__tempo


class Televisao(Controle):

    def __init__(self, volume):
        super().__init__()
        self.__volume = volume

    @property
    def volume(self):
        return self.__volume

    
    @volume.setter
    def altera_volume(self, novo_volume):
        self.__volume = novo_volume
        return self.__volume



ar = ArCondicionado(12)
micro = Microondas(2)
tv = Televisao(80)



