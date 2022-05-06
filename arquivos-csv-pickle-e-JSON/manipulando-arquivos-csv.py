# leitura e escrita CSV

# csv == Comma Separated Values (arquivos separadas por Virgula)
# lembrando que a virgula não é parametro, todo arquivo que tenha um separador, seja ele espaços, ponto e virgula, ponto entram como CSV

# ex  1,2,3,4,5,    1;2;3;4;5; dentre outros...

# o governo disponibiliza dados no  link http://dados.gov.br/dataset um otimo lugar para estudar CSV

#  1 ) como abrir um arquivo CSV para leitura

# forma pythonica de abrir

# temos duas maneiras

# 1.1 ) reader() --> itera as linhas do arquivo como lista ---> retorna lista
# para usar essa função temos que importar do modulo csv

from csv import reader

# vamos usa-lo

# obs --> mesma sintaxe de abertura de arquivos do tipo txt

# sintaxe --> with open('.diretorio.nome_arquivo.extensão','tipo de abertura') alias (as) nome:

# usamos o reader() declarando como parametro o nome do arquivo passado no alias(as) 

# ex

 
with open('filmes.csv','r') as arquivo:
    leitura = reader(arquivo)
    # armazenando em uma variavel a função reader passando como parametro o arquivo csv
    print(type(leitura)) # < class '_csv.reader'>
    # gera um iteravel, (ou seja podemos usar o metodo next(), ou fazer uma iteração normal usando for)
    next(leitura) # itera a primeira linha (pula ela)

    #for indice,item in enumerate(leitura):
        # print(f'linha: {indice}\nItem : {item}')
        # mostra cada indice de linha do arquivo e o item contido nele


# se formos analisar arquivos que tem acentuação ou caracteres especiais, basta passar como parametro do with open  enconding='utf-8'

# dessa forma --> with open('nomearquivo.extensao','tipo de abertura', econding='utf-8')


# DENTRO DE READER() passamos como parametro o arquivo aberto, e fora isso conseguimos passar tbm qual o delimitador (separador), suponha que vc esteja lendo um arquivo que seja separado por '/' o python não identificaria esse delimitador

# por isso, usamos a seguinte sintaxe
# usando o exemplo anterior:

# leitura = reader(arquivo, delimiter='/') e pronto, agora o python sabe que o delimitador é '/', isso serve para qualquer separador

# reader() Por padrao ja vem identificanado o separador como virgula!






# 1.2 ) DictReader - retorna um dicionario --> itera as linhas do arquivo cvs porem retorna um dicionario

# essa é a unica diferença entre reader() e DictReader()

# lembrando sempre de fazer a importação do DictReader() do modulo csv



from csv import DictReader

# ex


with open('filmes.csv','r') as arquivo:
    leitura = DictReader(arquivo, delimiter=';') # caso delimitador seja ;
    next(leitura)
    for item in leitura:
        print(item)
    # {'Pessoa,Filme': 'Tom Holland,Homem Aranha'}
    # {'Pessoa,Filme': 'Emma Watson,Harry Potter'}
    # {'Pessoa,Filme': 'Angelina Jolie,Malevola'}
    # {'Pessoa,Filme': 'Jennifer Aniston,Marley&Eu'}

# TEMOS TODOS OS ATRIBUTOS DO READER, dentro de with open() podemos declarar o enconding

# dentro do DictReader() passamos o nome do arquivo e depois podemos passar o delimitador (delimiter)






# 2 ) escrita -->  Temos duas formas
 
# 2.1)  Writer() --> permite a escrita em csv usando LINHAS

# obs: writerow() --> Para escrever cada uma das linhas (recebe como paramentro listas!)

# temos que importar o writer tbm do modulo csv

from csv import writer

# lembrando que caso o arquivo não exista o modo w vai criar ele!
# e caso exista vai sobrescrever ele!

with open('animais.csv','w',encoding='utf-8') as arquivo:
    escrita = writer(arquivo) # salvando o arquivo em uma variavel
    escrita.writerow(['animal','tipo']) # escrevendo o cabecalho do arquivo
    condicao = 0

    while condicao != 1: # loop para escrever cada uma das linhas
        animal = input('Digite o Animal: ')
        tipo = input('Digite o tipo do animal: ')
        escrita.writerow([animal,tipo])
        parar =  int(input('Digite 1 se deseja parar o cadastro e 0 se deseja continuar!'))
        if parar == 1:
            condicao = 1


# criou um arquivo csv com as informações

# animal,tipo
# camelo,herbivoro
# leao,carnivoro
# pato,herbivoro

# caso o arquivo gerado pule linhas
# basta adicionar o comando newline='' dentro de with open()

# dessa forma

#  with open('nome_arquivo.extensão','modo de abertura', newline='')

# e pronto o arquivo vai sair configurado normalmente

# ESSE ERRO SÓ ACONTECE EM ALGUNS SISTEMAS OPERACIONAIS!


# dentro da escrita podemos passar qual o tipo de delimitador (separador) dentro dos parametros do writer
# ex

# with open('animais.csv','w') as arquivo:
#     escrita = writer(arquivo, delimiter=';') # dessa forma tudo sera delimitado por ponto e virgula!


# 2.2) DictWriter() --> da mesma forma que temos o DictReader temos o DictWriter
# a diferença do writer() para o DictWriter() é que DictWriter recebe como parametro para escrita um dicionario (chave, valor)

# lembrando da importação pelo modulo csv

from csv import DictWriter

# DictWriter recebe como parametros o arquivo e fieldnames que é onde vamos definir o cabecalho,(fieldnames recebe uma lista ou tupla)


with open('doce.csv','w') as doces:

    titulo = 'doce','gosto' # criando uma tupla (lembrando que tuplas não precisam ser criadas necessariamente com os parenteses!)

    escrita = DictWriter(doces, fieldnames=titulo)
    # para escrever o cabecalho, usamos o metodo writeheader() (que não necessitam de parametros!)
    escrita.writeheader()

    # para escrever as linhas do nosso arquivo, nós vamos botar as informações usando o writerow ! --> exatamente como o write()
    # porem o writerow do DictWriter recebe um dicionario como parametro
    # arquivo.writer({ tipo=doce, sabor=gosto })
  

    condicao = 0

    while condicao != 1:
        tipo = input('Nome do doce: ')
        sabor = input('Gosto do doce: ')
        parada = input('Deseja parar? ')
        # lembrando que para usar o writerow do DictWriter() devemos passar como chave o mesmo nome usado na lista do fieldnames
        escrita.writerow({
            'doce':tipo,
            'gosto':sabor
        })
        if parada == 'sim':
            condicao = 1

        # criou o seguinte arquivo:
        # doce,gosto
        # chocolate,doce
        # prestigio,coco

    
    