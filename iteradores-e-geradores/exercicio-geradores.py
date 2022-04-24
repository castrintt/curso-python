# 1) crie uma lista que armazene inteiros de um usuario em um loop até que o usuario não deseje mais adicionar, trate o erro com try/except caso o usuario digite uma letra ao inves de um numero. Passe essa lista para uma função geradora que reconhecera quais são os numeros primos dentro da lista passada inicialmente.
# caso seja um numero primo, retorne pelo metodo yield, caso contrario passe para o proximo numero.
#ao final, imprima os valores retornados pelo yield em forma de tupla


listaUsuario = []

condicao = 1

while condicao != 0:
    try:
        numeros = int(input('Digite um numero: '))
    except ValueError:
        print('Erro... Você deve digitar um valor numerico!')
        condicao = 0
    else:
        if numeros == 0:
            condicao = 0
        else:
            listaUsuario.append(numeros)

def geradora(lista):
    for item in lista:
        divisor = 1
        numeros_divisores = 0
        while divisor <= item: # incrementa o divisor sem sair do loop, ou seja, mantem o valor de item e incrementa o divisor, quando o divisor for maior que item ele sai do while
            if item % divisor == 0: # testamos se o resto da divisao do item pelo divisor, se for == 0 incrementamos o divisor e somamos mais 1 em numeros_divisores
                divisor += 1
                numeros_divisores += 1
            else:
                divisor += 1
        if numeros_divisores == 2:
            yield item


tuplaNumerosPrimos = tuple(geradora(listaUsuario))
    
print(tuplaNumerosPrimos)


