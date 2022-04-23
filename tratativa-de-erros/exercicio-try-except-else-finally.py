# 1) aplique o procedimento Try/ except / else / finally no seguinte codigo que realiza um cadastro de formulario para uma pessoa realizar uma viagem:



opcoes_viagem = {
    1:'EUA',
    2:'Franca',
    3:'Japao',
    4:'Brasil'
}
try:
    nome = input('Digite seu nome: ')
    validacao = int(nome)
except ValueError:
    try:
        idade = int(input('Digite sua idade: '))
    except ValueError:
        print('Idade deve receber um valor inteiro!')
    else:
        try:
            lugar = int(input('Digite o numero para escolha do lugar: \n1- EUA\n2- Franca\n3- Japao\n4- Brasil \n'))
        except ValueError:
            print('Lugar deve receber valor inteiro de 1 a 4!')
        else:
            try:
                pais = opcoes_viagem[lugar]
            except KeyError:
                print('Você SOMENTE DEVE digitar um numero de 1 a 4!')
            else:
                print(f'Olá {nome} Você escolheu viajar para {pais}!')
else:
    print('Nome não deve receber valores Numericos')
finally:
    print('cadastro finalizado!')   

    
