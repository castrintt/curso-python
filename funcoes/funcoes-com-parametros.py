# podem receber dados  e variaveis como argumentos para utilização em processos internos

#podem ter inumeros parametros, todos separados por virgula

# ja trabalhamos com varias funçoes que recebiam parametros sem saber!

# ex 

# sum()
# max()
# min()
# index()
# ...

# ex de uma funçao com parametros definidos por nós


x = 10

y = 20

def soma(num1,num2):
    return num1 + num2

print(soma(x,y)) # 30 soma dos parametros x e y

lista = list(range(1,11))

#declarando a função
def imparPar(iteravel):
    for num in iteravel: # declarando um loop dentro da função
        if num % 2 == 0: # declarando uma condicional
            print(f'Numero {num} = par')
        elif num % 2 != 0:
            print(f'Numero {num} = impar')


#chamando a função
imparPar(lista)

# Numero 1 = impar                                                
# Numero 2 = par
# Numero 3 = impar                                      
# Numero 4 = par
# Numero 5 = impar                                       
# Numero 6 = par
# Numero 7 = impar                                            
# Numero 8 = par
# Numero 9 = impar
# Numero 10 = par



# PODEMOS DEFINIR OS VALORES DOS ARGUMENTOS NA CHAMADA TBM 

#EX

def escrever(p1,p2):
    return print(p1 + ' ' + p2)
    

escrever(p2 = 'Paulo', p1 = "são") # são Paulo 

#sem definir os argumentos a função respeita a ordem, ou seja, os valores colocados nos argumentos da chamada serão organizados quanto a sua escrita

# def escrever(p1,p2)

# a chamada da função respeita a ordem ou seja, na chamada  --- escrever('ola','mundo') # retorna ola mundo

# ja na chamada --- escrever('mundo','ola') # retorna mundo ola



# PODEMOS PASSAR TBM UM VALOR DEFAULT VIA ARGUMENTO EX


def verificacaoBasica(num1 , num2=60): # passamos como default o valor de num2 como 60, logo na chamada da função não precisamos repetir ele
    if num1 > num2:
        print(f'{num1} é maior que {num2}')
    else:
        print(f'{num1} é menor que {num2}')
        
        
        
verificacaoBasica(80) # 80 é maior que 60

verificacaoBasica(40) # 40 é menor que 60


# porem se nós definirmos ele dentro da chamada o valor que foi definido como default sera subrescrevido
# ex


verificacaoBasica(10,5) # 10 é maior que 5 # nesse caso substituimos o valor default do argumento (num2) que era 60 para 5

 
 
 
# variaveis globais e locias (escopo global e escopo local)


# nome = 'matheus'

# def chamaNome():
#     nome = nome + ' Pinto'
#     return nome


# print(chamaNome()) # local variable 'nome' referenced before assignment  # retorna um erro
# porque a variavel nome declarada globalmente (nome = 'matheus') não é igual a variavel declarada dentro do escopo da função # logo a variavel nome dentro da função nem tem valor nenhum

# o correto seria fazer isso:

user = 'matheus'

def chamaNomeOutraVez(variavel):
    variavel = variavel + ' Pinto'
    return variavel

print(chamaNomeOutraVez(user)) # matheus Pinto 



# VARIAVEIS LOCAIS E VARIAVEIS PARA FUNÇÕES



# 1) - variavel global - PARA DECLARAR UMA VARIAVEL GLOBAL DENTRO DE UM ESCOPO LOCAL, PODEMOS USAR A PALAVRA RESERVADA GLOBAL
# ex


usuario = 'igor'

def verificaUser():
    
    global usuario # declarei que esta variavel é de escopo global e esta sendo usada dentro de um escopo local
    
    usuario = usuario + ' Logado'
    return usuario

print(verificaUser()) # igor Logado



# 2) - variavel nonlocal - PARA FUNÇÔES DENTRO DE FUNÇÔES - (basicamente escopo local (principal) e escopos locais (secundarios))



def funFora():
    total = 0
    def funDentro():
        
        nonlocal total # usando esse comando estamos dizendo para o python que essa variavel total não é uma variavel global, mas sim uma variavel que foi declarada dentro de um escopo local e queremos usar ela novamente dentro de outro escopo
        
        #nesse caso temos o escopo da função principal e o escopo da função secundaria
        
        # usando o nonlocal dizemos que a variavel total declarada no escopo local(principal) pode ser usada dentro do escopo local(secundario)
         
        total = total + 1
        print(total)
    return funDentro()



funFora() # 1 # foi somado 1 na variavel total, graças a declaração do nonlocal
