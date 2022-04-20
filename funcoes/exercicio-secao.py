# 1) faça uma função que receba um numero inteiro maior que zero e retorne a soma de todos os algorismo.
# caso o valor seja negativo retorne 'numero invalido':

 #ex 251 = 2 + 5 + 1 = 8
 
 
#minha resolução

numeroUsuario = int(input('Digite um numero: '))

def recebeNumero(num):
    if num <= 0:
        print('Numero invalido, tente novamente')
    else:
        stringNumero = str(num)
        lista = []
        for valor in stringNumero:
            lista.append(int(valor))
        for indice,item in enumerate(lista):
            print(f'Item : {indice + 1} // Numero : {item}')
    
    print(f'A soma de todos algorismos de {num} é {sum(lista)} e seus algorismos são ')
    
recebeNumero(numeroUsuario)



# resolução professor


def somaAlgarismos(numero):
    divisor = 1
    num_algarismo = 0
    soma = 0
    while True:
        if (numero // divisor) == 0:
            break
        else:
            num_algarismo += 1
            divisor *= 10    
      
    for valor in range(num_algarismo):
        soma += ((numero // (10 ** valor)) % 10)
    return soma
    
    
numero = int(input('Digite um numero: '))
if numero >= 0:
    print(somaAlgarismos(numero))
else:
    print('Numero invalido')