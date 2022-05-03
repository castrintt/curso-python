# 1) Crie duas classes (uma para um personagem no video game e outra para o controle do console).
# o controle deve ser capaz de fazer o personagem pular, abaixar desviar para esquerda e desviar para direita, sendo comandado, respectivamente pelas teclas W, A, S e D. Use a dica e a função choice() para determinar por onde vira o obstaculo ('cima','baixo','esquerda','direita'), e o tempo para o proximo obstaculo, que deve decair com o aumento dos pontos. Cada obstaculo passado gera + 1 ponto.
# ainda crie um loop infinito do jogo até a pessoa perder. por fim, apresente a pontuação final

# Dica:
# import time
#time.sleep(3) # o programa 'para' por 3 segundos

from time import sleep
from random import choice


class Personagem:
    def __init__(self, nome):
        self.nome = nome


class Controle:
    def pular(cls):
        print('Pulando')

    def baixo(cls):
        print('Desviando pra baixo')

    def esquerda(cls):
        print('Desviando para esquerda')

    def direita(cls):
        print('Desviando para direita')
        

posicoes = ['cima','baixo','esquerda','direita']

print('------- W - cima/ A - esquerda/ S - baixo/ D - direita---------')

jogando = 1
temporizador = 5
while jogando != 0:
    if temporizador == 0:
        temporizador += 0.5
    escolha = choice(posicoes)
    print(escolha)
    sleep(temporizador)
    teclasDeAtalho = input('\n')
    atalho = ''
    if teclasDeAtalho == 'a':
        atalho = 'esquerda'
    elif teclasDeAtalho == 'w':
        atalho = 'cima'
    elif teclasDeAtalho == 's':
        atalho = 'baixo'
    elif teclasDeAtalho == 'd':
        atalho = 'direita'

        
    if atalho != escolha:
        print('Desviou!')
        temporizador -= 0.5
    else:
        print('Perdeu!')
        jogando = 0


print('Tente novamente!')


