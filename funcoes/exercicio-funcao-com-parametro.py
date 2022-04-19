# 1) criar uma função recursiva ( que retorna ela mesma ) para armazenar N termos da sequência de Fibonacci em uma lista. N é definido pelo usuario. Ao encontrar os termos, imprimir a lista e finalizar a função

# 2) criar 5 funções: uma para um cadastro, outra para realizar o login, outra para mudar a senha, outra para realizar logout e ainda uma para definir qual opção o usuario deseja escolher. Utilize um loop while para sair do sistema apenas se o usuario desejar ( criar a opção 'sair').
# atente-se as regras:

# Só é possivel realizar um cadastro se não houver nenhum anterior.

# Só é possivel realizar login se houver um cadastro.

# Só é possivel realizar login se o usuario informar corretamente username e senha.

# Só é possivel alterar a senha se o usuario estiver logado.

# Só é possivel alterar a senha se o usuario informar corretamente a senha atual

# Só é possivel realizar logout se o usuario estiver logado.





#  resolução exercicio 1


#fibonacci

# 1 1 2 3 5 8 13 21

# (n- 1) + (n - 2) = n

# (n+1) - (n-1) = n

# x = list(range(1,101))
# res = 1
# antecessor = 0

# fibo = [1]

# for numeros in x:
#     if (res + antecessor) == numeros:
#         fibo.append(numeros)
#         antecessor =  res
#         res = numeros

# print(fibo) # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#     # Python 3: Fibonacci series up to n
# >>> def fib(n):
# >>>     a, b = 0, 1
# >>>     while a < n:
# >>>         print(a, end=' ')
# >>>         a, b = b, a+b
# >>>     print()
# >>> fib(1000)

# def fib( n; agregado = []):
#   if n <=1:
#       return [n]
#   else
#       return [fib(n-1) + fib(n-2)] + agregado



#         resolução principal




# fibo = []

# def fibonacci(condicao, a = 1, b= 1, auxiliar = 0):
#     global fibo
#     fibo.append(a)
#     a , b = b , a + b
#     # a = b
#     # b = a + b
#     auxiliar += 1
#     if condicao == auxiliar:
#         print(fibo)
#         return
#     else:
#         fibonacci(condicao, a, b , auxiliar)


# quantia = int(input('Quantos numeros da lista de fibonacci você deseja ver? '))

# fibonacci(quantia)




#                  resolução 1 professor





# listaSF = []

# def fibonacci(stop,a = 1, b = 1, aux = 0):
#     global listaSF 
#     listaSF.append(a)
#     a, b = b, a + b
#     aux += 1
#     if stop == aux:
#         print(listaSF)
#         return 0
#     else:
#         return fibonacci(stop,a,b,aux)


# stop = int(input('Digite a quantidade de termos: '))

# fibonacci(stop)
    





# minha resolução 2 




usuarios = []
logado = False

def cadastro():
    global usuarios
    user = dict(nome=input('Cadastre um nome de usuario: '), senha=input('Cadastre uma senha: ') )    
    usuarios.append(user)
    print('Usuario cadastrado!')
    return usuarios

def login():
    global usuarios, logado
    nomeUsuario = input('Digite login: ')
    senhaUsuario = input('Digite a senha: ')
    for usuario in usuarios:
        if usuario['nome'] == nomeUsuario and usuario['senha'] == senhaUsuario:
            print('Usuario Logado')
            print(f'Bem vindo {nomeUsuario}')
            logado = True
            return logado
        else:
            print('Usuario não encontrado, tente fazer o cadastro!')
            return cadastro(), logado

def alterandoSenha():
    global alterarsenha, usuarios, logado
    if alterarSenha == 1 and logado == True:
        user = input('Digite o nome do usuario a alterar a senha: ')
        senha = input('Digite sua senha antiga: ')
        for usuario in usuarios:
            if usuario['senha'] == senha and usuario['nome'] == user:
                novaSenha = input('Digite sua nova senha: ')
                confirma = input('Confirme a nova senha por favor: ')
                if confirma == novaSenha:
                    print('Senha alterada com sucesso!')
                    usuario['senha'] = novaSenha           
                    return usuario['senha']
                else:
                    print('As senhas não são iguais, por favor tente novamente!')
                    return alterandoSenha()
            else:
                print('Usuario ou senha incorretos')
                return alterandoSenha()
    elif logado == True and alterarSenha == 2:
        return
    elif logado == False and alterarSenha == 1:
        print('Usuario não está Logado!, tente Realizar o login!')
        return login()   
        
def logOut():
    global usuarios, logado
    opcao = int(input('Deseja fazer logout? 1 - sim, 2 - nao: '))
    if opcao == 1:
        logado == False
        log = int('Se deseja fazer login novamente digite 1, caso contrario digite 2')
        if log == 1:
            return login()
        else:
            return          
    else:
        print('Usuario ainda logado!')
        return 
    
    
cadastro()   
print(usuarios)
print(logado)

login()
print(usuarios)
print(logado)

alterarSenha = int(input('Deseja alterar sua senha? 1 - sim,  2 - não: '))
alterandoSenha()     
print(usuarios)
print(logado) 

logOut()
print(usuarios)
print(logado)



# resolução 2 professor


