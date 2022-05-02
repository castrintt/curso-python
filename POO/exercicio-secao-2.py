# 1) Crie uma classe Robo para controlar o objeto R2D2 com os seguintes metodos:

# construtor: Recebe como atributo a bateria que varia entre 0 e 100 e cria um atributo de instancia que apresenta se o robo esta ligado ou desligado

# metodo liga desliga: quando esse metodo é chamado o robô passa a ser ligado caso esteja desligado e vice-versa.

# moveimento: recebe como atributo uma string, que representa qual o lado que o robo ira andar e decresce o atributo bateria em 10 para cada execução desse metodo

# controle_energia: Imprime os atributos estado e bateria atualizados do Robo

# Crei uma interface de menu para o usuario decidir o oque ira fazer com o robo, ou seja, qual metodo ira acessar. Faça tratamento de erros com try, except, else e finally.

# trate tambem as condições especiais como bateria zerada o que irá acontecer com o seu R2D2
# # dentro outros fica a cargo de cada programador

class Robo:

    def __init__(self,bateria):
        self.bateria = bateria
        self.estado = 'Ligado'
    
    def liga_desliga(self):
        if self.estado == 'Ligado':
            print(f'R2D2 está {self.estado}!')
            print('Desligando...')
            self.estado = "Desligado"
        elif self.estado ==  'Desligado':
            print(f'R2D2 está {self.estado}')
            print('Ligando...')
            self.estado = 'Ligado'
        return self.estado
    
    def movimento(self, direcao):
        if self.estado == 'Ligado':
            self.direcao = direcao
            print(f'Direção: {self.direcao}')
            self.bateria -= 10
            return self.bateria
        else:
            print('Você deve primeiro ligar o Robo para poder movimenta-lo!')

    def controle_energia(self):
        print(f'Energia do R2D2: {self.bateria} Estado: {self.estado}')

R2D2 = Robo(100)


print('----------- BEM VINDO A INTERFACE DE CONTROLE DO R2D2-----------')
print('\n')
print('----------ENTRANDO NO PAINEL DE CONTROLE----------')
print('\n')

condicao = 0

while condicao != 1:
    print('---OQUE DESEJA FAZER COM O R2D2----')
    try:
        escolha = int(input('Digite um numero para enviar comandos ao R2D2:\n1 - Ligar ou Desligar\n2 - Movimentar\n3 - Painel de controle de energia\n4 - Sair: \n'))
    except ValueError:
        print('Para controlar o robo deve-se digitar um numero de 1 a 4.\n')
    else:
        if escolha == 1:
            R2D2.liga_desliga()
        elif escolha == 2:
            try:
                direcao = input('Digite uma diração para R2D2 andar\n')
                test = int(direcao)
            except:
                R2D2.movimento(direcao)
            else:
                print('Erro, direção deve receber um valor valido!\n')
        elif escolha == 3:
            R2D2.controle_energia()
        elif escolha == 4:
            print('Saindo do programa!')
            condicao = 1
        else:
            print('Opção invalida, tente novamente!\n')