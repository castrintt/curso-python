# 1) Crie uma função que contenha 3 funções dentro:
# - uma delas deixa a string toda maiuscula.
# - outra que soma dois numeros passados pelo usuario.
# - e , a ultima soma um numero passado pelo usuario com um numero aleatorio entre 0 e 15 com o comando randint()
# a função mais externa recebe todos os parametros com *args e deve-se fazer tratamento com try, except caso o usuario passa de forma errada os dados desejados.
#  A função em args deve receber primeiro o nome da função interna que deseja acessar e os parametros necessarios nessa ordem especificamente.
#  Ex: função_externa('soma_num',2,3),
#  no caso está chamando a função interna que soma dois numeros (2,3). Cada função deve imprimir seu resultado

from random import randint as rd

# recebe primeiro uma string e 2 numeros
def principal(*args):
    # breakpoint()
    listaString = []
    numeros = []
    for num in args:
        try:
            if type(int(num)) == int:
                numeros.append(int(num))
        except ValueError:
            listaString.append(args[0])
            pass

    def maiuscula():
        string = ''.join(listaString)
        stringFormatada = string.upper()
        print(f'{stringFormatada}\n')
    
    def soma():
        for indice,num in enumerate(numeros):
            print(f'Numero {indice + 1}: {num}\n')
        print(f'A soma dos numeros {numeros[0]} e {numeros[1]} é {sum([numeros[0], numeros[1]])}\n')


    
    def soma_aleatorio():
        random = rd(0,15)
        print(f'Soma dos numero: {numeros[0]}, e o numero aleatorio: {random}, é igual a {sum([numeros[0], random])}')
    return maiuscula(), soma(), soma_aleatorio()


principal('meu nome é igor',10,20)


# resolução professor

from random import randint as rd

def funcao_externa(*args):
    if args[0] == 'upper_str':
        def upper_str():
            try:
                print(args[1].upper())
            except AttributeError:
                print('segundo parametro deve ser um caracter!')
        return upper_str
    elif args[0] == 'soma':
        def soma():
            try:
                print(f'A soma de {args[1]} e {args[2]} é igual a {sum([args[1], args[2]])}')
            except:
                print('Terceiro e quarto elementos do parametro devem ser Numericos!')
        return soma
    elif args[0] == 'soma_aleatoria':
        def soma_aleatoria():
            numero_aleatorio = rd(0,15)
            try:
                print(f'A soma de {args[1]} e {numero_aleatorio} é {sum([numero_aleatorio,args[1]])}')
            except:
                print('Argumento 3 deve ser numerico!')
        return soma_aleatoria

resultado = funcao_externa('soma',10,5)  

resultado() # A soma de 10 e 5 é igual a 15

resultado = funcao_externa('upper_str','ola meu nome é igor') 

resultado() # OLA MEU NOME É IGOR

resultado = funcao_externa('soma_aleatoria',12) 

resultado() # A soma de 12 e 2 é 14