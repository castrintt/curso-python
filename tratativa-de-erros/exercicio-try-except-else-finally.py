# 1) aplique o procedimento Try/ except / else / finally no seguinte codigo que realiza um cadastro de formulario para uma pessoa realizar uma viagem:



opcoes_viagem = {
    1:'EUA',
    2:'Franca',
    3:'Japao',
    4:'Brasil'
}

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
lugar = int(input('Digite o numero para escolha do lugar: \n1- EUA\n2- Franca\n3- Japao\n4- Brasil \n'))
pais = opcoes_viagem[lugar]
print(f'Olá {nome} Você escolheu viajar para o {pais}!')
print('cadastro finalizado!')   


