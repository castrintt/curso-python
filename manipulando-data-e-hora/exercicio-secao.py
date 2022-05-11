 # 1 ) Dudu é um famosinho do instagram e precisa manter postagens em seu feed regularmente. portanto teve a ideia de criar um programa em Python que agende suas publicações para todas segundas, quartas e sextas ao longo de um mes, a partir desse momento. Alem disso, seus posts iram variar entre os temas:

# saude, vida pessoal e motivacional. Com isso utilize choice() para selecionar cada conteudo aleatoriamente. Faça um programa que implemente a ideia de Dudu, imprimindo o conteudo de cada um dos dias e seus respectivos dias de postagem

# minha resolução!


# from random import choice as ch
# import datetime

# listaDePosts = ['Comer verdura faz bem','Pratique um esporte','Vamos voce consegue, estude!']

# dicionarioDias = {
#     'segunda':[0,7,14,21,28],
#     'terça':[1,8,15,22,29],
#     'quarta':[2,9,16,23,30],
#     'quinta':[3,10,17,24,31],
#     'sexta':[4,11,18,25],
#     'sabado':[5,12,19,26],
#     'domingo':[6,13,20,27]
# }


# for day in range(0,31):
#     # breakpoint()
#     if day in dicionarioDias['segunda']:
#         print(f'Hoje é segunda pessoal! --> mensagem do dia --> {ch(listaDePosts)}')
#     elif day in dicionarioDias['quarta']:
#         print(f'Hoje é quarta pessoal! --> mensagem do dia --> {ch(listaDePosts)}')
#     elif day in dicionarioDias['sexta']:
#         print(f'Hoje é sexta pessoal! --> mensagem do dia --> {ch(listaDePosts)}')
#     else:
#         pass


# resolução professor

import datetime
from random import choice as ch

temas = ['saude','vida pessoal','motivacional']

esteMomento = datetime.datetime.now()

mesQueVem = esteMomento + datetime.timedelta(30)


while (esteMomento.day <= mesQueVem.day) or (esteMomento.month <= mesQueVem.month):
    if esteMomento.weekday() == 0:
        print(f'Mensagem de Segunda é {ch(temas)}')
    elif esteMomento.weekday() == 2:
        print(f'Mensagem de Quarta é {ch(temas)}')

    elif esteMomento.weekday() == 4:
        print(f'Mensagem de sexta {ch(temas)}')
    esteMomento += datetime.timedelta(1)