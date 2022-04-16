# 1) para cada numero par em um range de 1 a 9 , adiciona esse numero elevado ao quadrado no conjunto, se o numero for impar adicione 2 elementos, 1 por vez: 'sou','impar'. Qual foi a resposta?

# 2) porque 'sou', 'impar' só apareceu uma vez?

# resposta 2)

# porque set comprehension não aceita valores repetidos, e como foi pedido para escrever 'sou','impar' para cada numero impar de 1 a 9 (oq obviamente é mais do que um unico numero impar), só apareceu uma vez

# minha resposta resposta 1)

conjunto = set()

for numero in range(1, 10):
    if numero % 2 == 0:
        conjunto.add(numero**2)
    else:
        conjunto.add('sou')
        conjunto.add('impar')

print(conjunto)  # {64, 4, 36, 'impar', 'sou', 16}

conj = {
    numero ** 2 
    if numero % 2 == 0 
    else 'sou'
        if num == 0
        else 'impar'
            for num in range(0,2)
    for numero in range(1,10)
}




# resposta professor 2)

conjunto = {numero**2 if numero % 2 == 0 else 'sou' if num == 0 else 'impar' for num in range(0, 2) for numero in range(1, 10)}

print(conj)  # {64, 4, 36, 'impar', 16, 'sou'}


