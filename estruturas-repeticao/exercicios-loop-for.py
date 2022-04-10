#1) faça um programa que calcule a soma dos divisores de um numero inteiro definido pelo Usuario

#          ex: usuario escolheu 10 , temos 1 + 2 + 5 +10 = 18

user = int(input('Digite um numero: '))
numeros = range(1, (user + 1))
soma = 0

for numero in numeros:
    if numeros[-1] % numero == 0:  
        #print(f'{numero}', end=" ")
        soma += numero
        print(f'numero: {numero}', end=", ")
               
print(f"\n a soma de todos os numeros divisiveis por {numeros[-1]} é {soma}" )

#       pode ser feito sem armazenar o range em uma variavel tbm

user = int(input('Digite um numero: '))
soma = 0

for numero in range(1, user + 1):
    if user % numero == 0:  
        #print(f'{numero}', end=" ")
        soma += numero
        print(f'numero: {numero}', end=", ")
               
print(f"\n a soma de todos os numeros divisiveis por {user} é {soma}" )


#2) faça um programa que imprima os n primeiros multiplos de 5, sendo n definido pelo usuario

#ex             usuario escolheu n=3, será impresso 5,10,15

n = int(input('Digite um numero  de multiplos de 5 que deseja: '))
for indice, numeros in enumerate(range(1, n + 1)):
    if numeros != 0:
        print(numeros * 5, end=", ")
    #sem enumerate
    # if numeros != 0:
    #     print(numeros * 5, end=", ")
    
    
    
#  pode ser feito armazendando os dados em uma variavel, da seguinte forma


n = int(input('Digite um numero  de multiplos de 5 que deseja: '))
multiplos = range(1, n + 1)

for indice, numeros in enumerate(multiplos):
    print(numeros * 5, end=", ")