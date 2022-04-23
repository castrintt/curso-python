# 1) a partir do seguinte codigo aplique raise para apresentar possiveis erros do seguinte programa que realiza a escolha de uma das opções de lazer para uma pessoa e dependendo da suia escolha, chama uma função que realiza testes especificos




def viagem_exterior(nome,idade,valor):
    if type(nome) == str and type(idade) == int and type(valor) == float:
       print(f'{nome}, {idade} anos, tem {valor} para gastar em viagens')
    else:
        raise TypeError('O tipo de algum dos dados esta incorreto')

def fazer_compras(nome,idade,valor):
    if type(nome) == str and type(idade) == int and type(valor) == float:
        if valor < 200:
            print('seu orçamento esta curto, cuidado!')
    else:
        raise TypeError('O tipo de algum dos dados esta incorreto')
    print(f'{nome}, {idade} anos, tem {valor} para gastar em compras')

def cassino(nome,idade,valor):
    if type(nome) == str and type(idade) == int and type(valor) == float:
        if idade < 18:
            print('Você não pode entrar')
    else:
        raise TypeError('O tipo de algum dos dados esta incorreto')
    print(f'{nome}, {idade} anos, tem {valor} para gastar em compras')


atividade = input('Digite a opção que deseja: viajar_exterior, fazer_compras ou cassino\n Opção: ')
if atividade == 'viajar_exterior':
    viagem_exterior(nome='Bruno',idade=26,valor=300.0)
elif atividade == 'fazer_compras':
    fazer_compras(nome='Isabela',idade=40,valor=150.0)
elif atividade == 'cassino':
    cassino(nome='Eduardo',idade=15,valor=100.0)
elif type(atividade) != str:
    raise TypeError('O tipo de dado deve ser string!')
elif atividade != 'viajar_exterior' or atividade != 'fazer_compras' or atividade != 'cassino':
    raise SyntaxError('A sintaxe deve ser identica às opções disponiveis!')