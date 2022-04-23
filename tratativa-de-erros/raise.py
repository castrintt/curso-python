# metodo para tratar um erro

# - Raise - significa levantar é utilizado para apresentar erros no codigo que nós mesmos identificamos

# a palavra raise é reservada assim como return, break, continue....

# caso você utilize o raise dentro de uma função, assim que o programa o reconhecer irá acusar o erro e sair da função

# SINTAXE

# raise tipo_erro('mensagem para o usuario')

# ex

# 1) 
# cadastro do site

def cadastrar(login,senha):
    print(f'Login: {login}, senha: {senha}')

cadastrar(123,123) # Login: 123, senha: 123

# suponhamos que você queira que o login seja sempre string e senha seja sempre inteiro
# nos tratariamos o erro de algum cadastro assim cadastrar(123,123) (login numerico)

# ficaria assim

def cadastrar(login,senha):
    if type(login) != str:
        raise TypeError('Login deve ser do tipo string')
    elif type(senha) != int:
        raise TypeError('Senha deve ser numerica')
    else:
        print(f'{login}, {senha}')
         
cadastrar(123,123) # TypeError: Login deve ser do tipo string # erro pois login não é do tipo string

cadastrar('igor','123') # TypeError: Senha deve ser numerica # erro pois senha não é do tipo int

# um cadastro correto ficaria assim

cadastrar('igor',123) # igor, 123


# 2) quando o divisor é 0

def divisao(num1,num2):
    if num2 == 0 or num1 == 0:
        raise ZeroDivisionError('Você não pode dividir um numero por 0')
    else:
        dividir = num1 / num2
        print(dividir)

divisao(0,2) # ZeroDivisionError: Você não pode dividir um numero por 0

divisao(1,0) # ZeroDivisionError: Você não pode dividir um numero por 0

divisao(4,2) # 2 