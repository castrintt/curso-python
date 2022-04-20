# 1) criar duas listas de mesmo tamanho preenchidas com numeros inteiros e retornar outra lista com a soma das duas listas sendo uma delas invertida (indice 0 com indice 0 para uma lista de tamanho 10), utilizando lambda e comprehensions para iterar ambas



# minha resolução // professor

lista1 = [num for num in range(1,6)]

lista2 = [num for num in range(6,11)]

lista2.reverse()

lista3 = []

soma = lambda l1, l2: [l1[indice] + l2[indice] for indice in range(0,5)]

resultado = soma(lista1,lista2)

lista3.append(resultado)

print(resultado)

print(lista3)