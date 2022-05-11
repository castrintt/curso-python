#  é utilizado o modulo integrado datetime

# o formato padrao de hora é o americano : --> aaaa/mm/dd

# para usar o modulo integrado devemos importa-lo

import datetime

# 1 ) datetime.datetime.now() --> usado para pegar data e hora atual -->> com diferencial de poder trabalhar com fusos horarios

# de primeira instancia vamos imprimir na tela o horario atual usando a classe datetime.now de datetime

horaAtual = datetime.datetime.now() # é possivel trabalhar com fuso horario

print(horaAtual) # 2022-05-11 10:37:31.100482


# 2 ) datetime.datetime.today() ---> usado tbm para pegar adata e horar atual --> porem não podemos trabalhar com fusos horarios

# podemos acessar usando datetime.today() mas usando today não podemos trabalar com fusos horarios ( o retorno é o mesmo do datetime.datetime.now() )

import datetime

horarioAtual = datetime.datetime.today() # diferença claro nos milissegundos

print(horarioAtual) # 2022-05-11 10:39:56.048085


# 3 ) como datetime é uma classe, podemos suar o repr() --> lembrando que __repr__ é um modo de representar na tela os atributos de uma classe!

# logo

import datetime

horaAtual = datetime.datetime.now()

print(repr(horaAtual))

# vamos usar tbm o dir para ver as possibilidades de uso dessa classe datetime

print(dir(datetime))

# ['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']

# 3.1 ) acessando o print(dir(datetime)) vimos 2 constantes MAXYEAR e MINYEAR com essas duas constantes podemos ver o 'avarege' ou distancia em que o python consegue acessar, nesse caso MAXYEAR define 'o ano mais longe que o python consegue alcançar' e MINYEAR define o 'menor ano que o python consegue alcançar'

# ex

print(datetime.MAXYEAR) # 9999
print(datetime.MINYEAR) # 1



# 4 ) podemos acessar diferentes 'instancias' do metodo now() de datetime, podemos acessar somente o dia, o ano, o mes e etc..

# veja

import datetime

horaAtual = datetime.datetime.now() # (em javascript seria --->> new Date())

ano = horaAtual.year
mes = horaAtual.month
dia = horaAtual.day
hora = horaAtual.hour
minutos = horaAtual.minute
segundos = horaAtual.second

print(horaAtual) # 2022-05-11 10:52:08.414122

print(ano) # 2022
print(mes) # 5
print(dia) # 11
print(hora) # 10
print(minutos) # 52
print(segundos) # 8


# conseguimos acessar todos os elementos da data e da hora!!



# 5 ) ajustar data e hora! --> para isso vamos usar a função replace() onde podemos passar via argumentos quais parametros queremos alterar, por exemplo, caso queira alterar o ano, basta passar como parametro do replace (year=ano)

# sintaxe --> variavel = datetime.datetime.now() --->  variavel = variavel.replace(year=21312,month=12,day=12,hour=12 etc...)


import datetime

horaAtual = datetime.datetime.now()
print(horaAtual) # 2022-05-11 10:59:12.644208

horaAtual = horaAtual.replace(year=1500,month=12,day=31,hour=23,minute=59, second=59)
print(horaAtual) # 500-12-31 23:59:59.644208



# 6 ) manipulando datas/ hora enviados pelo usuario

import datetime 


data = input('Digite a data do seu nascimento: (padrao -> dd/mm/aaaa): ')
listaData = data.split('/')

print(listaData) # ['04', '01', '1999'] agora podemos manipular esses dados da forma que quisermos

print(f'O seu ano de nascimento é {listaData[-1]}, mes {listaData[1]} e dia {listaData[0]}') # O seu ano de nascimento é 1999, mes 01 e dia 04

# podemos fazer com que o dado recebido pelo usuario se 'transplante' dentro do datetime usando a função replace como viamos logo acima

dataAtual = datetime.datetime.now()
dataAtual = dataAtual.replace(year=int(listaData[-1]),month=int(listaData[1]), day=int(listaData[0]))

print(dataAtual) # 1999-01-04 11:06:03.348317  ---> pronto recebemos do usuario um dado cru, não formatado com o padrao americano de data e hora do python, usamos o metodo split para transformar o dado recebido em uma lista usando um separador como parametro, e depois usamos o datetime.datetime.now() para então usar o replace com os parametro de year, month e day recebendo os inteiros da lista criada pelo split!



# PODEMOS TBM FAZER DESSA FORMA --> ao inves de definir o datetime.datetime.now() e depois passarmos o replace para alterar a data, podemos usar somente o datetime.datetime() passando como parametros na ordem --> ano, mes, dia, hora, minutos, segundos, microsegundos


# ex

import datetime 


data = input('Digite a data do seu nascimento: (padrao -> dd/mm/aaaa): ')
listaData = data.split('/')

print(listaData) # ['04', '01', '1999'] agora podemos manipular esses dados da forma que quisermos

print(f'O seu ano de nascimento é {listaData[-1]}, mes {listaData[1]} e dia {listaData[0]}') # O seu ano de nascimento é 1999, mes 01 e dia 04

# podemos fazer com que o dado recebido pelo usuario se 'transplante' dentro do datetime usando a função replace como viamos logo acima

dataAtual = datetime.datetime(int(listaData[-1]), int(listaData[1]), int(listaData[0]))

print(dataAtual) # 1999-01-04 00:00:00 --> dessa forma não precisamos escrever mais uma linha de codigo para alterar os parametros (porem ambos tem o mesmo resultado


# 7 ) Delta de data e hora --> Em Python, timedelta denota um intervalo de tempo. É a diferença entre dois date, time, ou objetos datetime.

import datetime 


horaAtual = datetime.datetime.now()

fimDoSeculo = datetime.datetime(2100,12,31,23,59,59)

resultado = fimDoSeculo - horaAtual

print(resultado) # 28723 days, 12:36:52.027180

print(f'faltam exatamente {resultado.days} dias para o fim do seculo!') # faltam exatamente 28723 dias para o fim do seculo!
print(f'faltam exatamente {resultado.days / 365} anos para o fim do seculo!') # faltam exatamente 78.69315068493151 anos para o fim do seculo!

# Vamos agora fazer subtração de datas usando o delta

import datetime


horaAtual = datetime.datetime.now()

print(horaAtual) # 2022-05-11 11:26:00.715773

tempoDeTrabalho = datetime.timedelta(30) #  30 dias

primeiroSalario = horaAtual + tempoDeTrabalho

print(primeiroSalario) # 2022-06-10 11:26:00.715773 --> exatamente um mes depois