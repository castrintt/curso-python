# while

#diferente do for o while precisa de uma condição para executar o codigo

#da mesma forma que condicionais podem ter break e continua o while tbm pode

#sintaxe

while condição: #enquanto a condição for verdadeira faça:
		#processo

#ex de while com condicional break

 cont = 0

while cont <= 5: #enquanto cont for menor ou igual 5 execute o codigo,
    cont += 1 # sempre adiciona 1 no cont para que o loop n seja infinito
    print(cont) 
    if cont == 3: #se o contador for igual a 3 pare
        break

#ex

contador = 0

while contador <= 5:
    print(contador, end="  ") #0  1  2  3  4  5
    contador += 1

#enquanto contador for menor ou igual a 5, printa o contador e adiciona + 1 nele

#outro exemplo

frase = ''

while frase != 'vamos comer pizza':
    frase = str(input('Oque vamos fazer hoje?: '))

#ENQUANTO A FRASE FOR DIFERENTE DE 'vamos comer pizza' o loop sera executado



# while

#diferente do for o while precisa de uma condição para executar o codigo

#da mesma forma que condicionais podem ter break e continua o while tbm pode

#sintaxe

while condição: #enquanto a condição for verdadeira faça:
		#processo

#ex de while com condicional break

 contador = 0

while contador <= 5: #enquanto contador for menor ou igual 5 execute o codigo,
    contador += 1 # sempre adiciona 1 no contador para que o loop n seja infinito
    print(contador) 
    if contador == 3: #se o contador for igual a 3 pare
        break

#ex

contador = 0

while contador <= 5:
    print(contador, end="  ") #0  1  2  3  4  5
    contador += 1

#enquanto contador for menor ou igual a 5, printa o contador e adiciona + 1 nele

#outro exemplo

frase = ''

while frase != 'vamos comer pizza':
    frase = str(input('Oque vamos fazer hoje?: '))

#ENQUANTO A FRASE FOR DIFERENTE DE 'vamos comer pizza' o loop sera executado
