# 1) criar um arquivo de texto, inserir o lucr mensal de uma startup entre os meses de janeiro e maio, informando o mês e o valor, atraves da entrada do usuario. apois isso , ler o arquivo e imprimir o mes de maior lucro


# minha resolução

with open('exercicio-escrever.txt','w') as lucros:
    while True:
        lucroMensal = input('Digite aqui o mes e o valor lucrado, caso deseje sair do programa digite "sair": ')
        if lucroMensal != 'sair':
            lucros.write(f'{lucroMensal}\n')
        else:
            break


with open('exercicio-escrever.txt','r') as lucros:
    arquivo = lucros.read()
    lista = arquivo.replace('\n',',').split(',')
    dados = ' '.join(lista).split(' ')
    dados.pop(dados.index(''))
    meses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
    listaMeses = [] # separando os meses
    listaValores = [] # separando os valores para comparar o maior valor posteriormente
    for dado in dados:
        if dado in meses:
            listaMeses.append(dado)
        else:
            listaValores.append(int(dado))
    listaValoresMeses = list(zip(listaMeses,listaValores))
    print(listaValoresMeses) # [('janeiro', 15000), ('fevereiro', 12000), ('março', 40000), ('abril', 42000), ('maio', 57833), ('junho', 70000), ('julho', 22623), ('agosto', 98000), ('setembro', 28383), ('outubro', 29239), ('novembro', 92829), ('dezembro', 12283)]
    for valor in listaValoresMeses:
        if valor[1] == max(listaValores):
            print(f'O mes que mais teve lucro foi: {valor[0]} e o de lucro foi R$ {valor[1]} reais')
            # O mes que mais teve lucro foi: agosto e o de lucro foi R$ 98000 reais



# outra resolução (mais compacta)

listaValores = []
listaMeses = []

with open('exercicio-escrever.txt','w') as arquivo:
    while True:
        mes = input('Digite o mes ou sair : ')
        if mes != 'sair':
            lucro = float(input(f'Digite o lucro do Mes {mes}: '))
            arquivo.write(f'{mes} ')
            arquivo.write(f'{lucro}\n')
            listaMeses.append(mes)
            listaValores.append(lucro)
        else:
            break

mesValor = list(zip(listaMeses,listaValores))
print(mesValor) # [('janeiro', 12390812390.0), ('fevereiro', 123078129.0), ('março', 12487189.0), ('abril', 1201278942.0), ('maio', 1489172289.0), ('junhio', 1219012390.0), ('julho', 1123128937.0), ('agosto', 124017894.0), ('setembro', 12490128902.0), ('outubro', 18902378291.0), ('novembro', 1234901278492.0), ('dezembro', 1249012890.0)]

for item in mesValor:
    if max(listaValores) == item[1]:
        print(f'O mes com maior lucro foi: {item[0]} com um lucro de R${item[1]} reais') # O mes com maior lucro foi: novembro com um lucro de R$1234901278492.0 reais