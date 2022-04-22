# 1) Receba numeros inteiros do usuario e armazene-os em uma lista. Crie uma condição para o numero 0 finalizar o processo de preenchimento. Após isso, imprima o maior valor da lista utilizando as funções sorted() e len(). Por fim, utilize reversed() para inverter a lista e obtenha, pelo indice, o valor intermediario da mesma.
#obs - Caso o numero de valores da lista seja par, pegue a media dos dois valores centrais


#minha resolução


lista = []
num = 1
while num != 0:
    num = int(input('Digite um ou mais Numeros : '))
    if num != 0:
        lista.append(num)

print(f'Lista: {lista}')

ordenada = sorted(lista)
print(f'Lista ordenada: {ordenada}')
maiorElementoUsandoLen = ordenada[len(lista) - 1]
print(f'O maior elemento da lista {ordenada} é {maiorElementoUsandoLen}')

reversa = reversed(ordenada)
listaReversa = list(reversa)

print(f'Lista ordenada Reversa: {listaReversa}')

if (len(listaReversa) + 1 ) % 2 == 0:
    indice = (len(listaReversa ) + 1) // 2
    elementoDoMeio = listaReversa[indice - 1]
    print(f'O elemento do meio é : {elementoDoMeio}')
    
elif (len(listaReversa) + 1 ) % 2 != 0:
    indiceOrdenada = (len(ordenada) + 1 ) // 2 
    indiceReversa = (len(listaReversa) + 1) // 2
    print(f'Numero do meio na lista Ordenada  : {ordenada[indiceOrdenada - 1]}')
    print(f'Numero do meio lista reversa : {listaReversa[indiceReversa - 1]}')
    media = ordenada[indiceOrdenada - 1] + listaReversa[indiceReversa - 1] // 2
    print(f'A media dos dois numeros do meio é : {media}')
    
    
    
# resolução professor

numeroInt = 1
listaNumeros = []

while numeroInt != 0:
    numeroInt = int(input('Digite um numero inteiro: '))
    if numeroInt != 0:
        listaNumeros.append(numeroInt)

ordenada = sorted(listaNumeros)
tamanho = len(listaNumeros)

print(f'Maior valor: {ordenada[tamanho - 1]}')

invertida = reversed(ordenada)
listaInvertida = list(invertida)

if tamanho % 2 == 1:
    print(f'Valor intermediario: {listaInvertida[tamanho // 2]}')
else:
    print(f'Media dos valores intermediarios: {(listaInvertida[tamanho // 2] + listaInvertida[(tamanho//2) -1 ]) // 2} ')
    
