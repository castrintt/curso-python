#3 FORMAS DIFERENTES DE VERIFICAR LOGIN E SENHA DE USUARIO

# loginPrincipal = 'igor'
# senhaPrincipal = 123
# logado = False

# login = str(input('digite o nome de usuario: '))
# senha = int(input('digite uma senha numerica: '))


# if login == loginPrincipal and senha == senhaPrincipal:
#     logado = True
#     print('usuario logado') 
# elif login != loginPrincipal and senha != senhaPrincipal:
#     logado = False
#     print('login e senha incorretos')
# elif login != loginPrincipal:
#     logado = False
#     print('login incorreto')
# elif senha != senhaPrincipal:
#     logado = False

#----------------------------------------------

# logado = False

# print('\n _____ Crie seu usuario____')
# user = input(' \ndigite o nome do usuario: ')
# password = input(' \ndigite a senha do usuario: ')


# print('\n _________LOGIN___________')

# userVerify = input(' \nUsuario :')
# passwordVerify = input(' \nSenha :')


# print('\n __________VERIFICANDO__________')

# if user == userVerify and password == passwordVerify:
#     print('\n Usuario verificado!')
#     logado = True
#     print('\n ___________AREA USUARIO_________')
# else:
#     print('\n Nome de usuario ou senha incorretos!')
#     logado = False
    

# if logado is True:
#     print('\nReunião hoje!')
# else:
#     print('\nUsuario não está logado')

#- --------------------------------------------------------
#forma mais compacta ( pedindo e manipulando um dado por uma estrutura de condição )

login = False

user = input('\n Cadastre um nome de usuario: ')
senha = input('\n Cadastre uma senha: ')

if input('\nLogin: ') == user and input('\nSenha: ') == senha:
    print('\nUsuario logado')
    login = True
else:
    print('\nLogin ou senha incorretos')
    login = False
    
if login is True:
    print('\nBem vindo ao site!')
else:
    print('\nUsuario não está cadastrado: (SEM ACESSO)')