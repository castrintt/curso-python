# São funções (CHAMADAS DE EXPRESSÕES)

# - São como funções sem nome que funcionam como uma função qualquer.

# - a chamada de uma função normal é igual a de uma função lambda

# sintaxe: lambda parametro(s): retorno

# ex

def pot(x, y):
    print(x ** y)


pot(3,2) # 9
  
 

# ex 1 de expressão lambda

potencia = lambda x, y: print(x ** y)

potencia(3,2) # 9


# OBS expressoes lambdas aceitam qualquer quantidade de parametros de entrada.


# ex 2 lambda

cadastro = lambda nome,idade,cpf: print(f'Nome: {nome}, idade: {idade}, CPF: {cpf}')

cadastro('igor',23,'5032123224234234')  # Nome: igor, idade: 23, CPF: 50321232242342



# ex 3 lambda

segGrau = lambda a,b,c,x : a*x**2 + b*x + c  #(função quadratica ax ao quadrada, + bx + c)


print(segGrau(1,5,8,3)) # 32


# outra forma de fazer a lambda (ex 3)


def grau(a,b,c):
    return lambda x: a * x**2 + b*x + c

segundoGrau = grau(1,5,8) # nesse caso a variavel segundoGrau esta recebendo lambda # só que nesse caso segundoGrau recebe lambda com um parametro (x) que ainda n foi passado, para passarmos esse valor, devemos chamar a função lambda

print(segundoGrau(3)) # 32  # chamando a função lambda passando o parametro 3 para o (X)


# é exatamente a mesma coisa que fizemos em segGrau = lambda a,b,c,x: a*x**2 + b*x + c


# OU SEJA ----- em segundoGrau = grau(1,5,8) - passamos os valores de a b c, porem eles estao atribuidos a uma lambda com parametro x -- return lambda x: a * x**2 + b*x + c (e nesse caso lambda recebe um parametro)
# depois de salvar os valores a b c dentro da chamada (segundoGrau = grau(1,5,8)) podemos agora sim chamar a função lambda passando o parametro x (lambda nesse caso esta dentro de segundograu)