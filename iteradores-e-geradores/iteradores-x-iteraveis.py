# oque é um iterador?

# é um objeto que pode ser iterado e retorna um dado quando utiliza-se a função next()

# oque é um iteravel

# é um objeto que retorna um iterador quando usasse a função iter()

# ex

#TRANSFORMANDO ITERAVEL PARA ITERADOR

nome = 'programando ideias'# strings são iteraveis
lista = [1,'oi',True] # listas são iteraveis


primeiro_iterador = iter(nome)
segundo_iterador = iter(lista)


print(primeiro_iterador) # <str_iterator object at 0x7fe638f94b80> # retornar uma string iteradora
print(segundo_iterador) # <list_iterator object at 0x7fbba6e246d0> # retorna uma lista iteradora

#provamos que iteraveis retornam num iterador quando usar a função iter()
# os dois retornos trazem um objeto iterador (1- string iteradora 2- lista iteradora)



#UTILIZANDO NEXT() EM UM ITERADOR

print(next(primeiro_iterador)) #p # retorna um dado
print(next(primeiro_iterador)) #r # retorna um dado
print(next(primeiro_iterador)) #o # retorna um dado
print(next(primeiro_iterador)) #g # retorna um dado
print(next(primeiro_iterador)) #r # retorna um dado
#se eu continuar chamando o next ele vai continuar imprimindo o restante da string


print(next(segundo_iterador)) # 1
print(next(segundo_iterador)) # oi
print(next(segundo_iterador)) # True
# aqui ja foi impresso todos os dados do segundo_iterador (que é uma lista com 3 dados [um inteiro, uma string e um boolean])
# oque aconteceria se chamassemos esse metodo de novo? tendo em vista que não existem mais elementos para retornar(RETORNA UM ERRO)


#print(next(segundo_iterador)) # StopIteration retorna um erro stopiteration, pois voce ja obteve todos os dados desmembrados da sequencia

# O LOOP FOR TRABALHA EXATAMENTE ASSIM, ELE PEGA UM ITERAVEL, APLICA A ITER() E LOGO DEPOIS APLICA VARIOS NEXT()

for item in segundo_iterador:
    print(item, end=', ') # 1, oi , True



# OU SEJA O FOR POR DEBAIXO DOS PANOS FAZ EXATAMENTE ISSO, TRANSFORMA UM OBJETO EM ITERADOR (usando ITER()) E LOGO DEPOIS APLICA VARIOS NEXT() (PARA RETIRAR TODOS OS DADOS DESSE ITERADOR)

# PARA MELHOR VISUALIZAÇÃO (desmembrando o for)

# 1) TRANSFORMA UM OBJETO EM ITERADOR (usando iter())
# 2) RETIRA OS DADOS DESSE ITERADOR (usando next())




# sabendo como funcionam iteradores e iteraveis, nós podemos criar o nosso proprio loop.

# ao inves de usar o for podemos fazer

listaDeNumeros = [1,2,3,4,5,6,7,8,9,10]

print(type(listaDeNumeros)) # <class 'list'>

#transformando a lista em um iterador

iterador = iter(listaDeNumeros)

print(iterador) # <list_iterator object at 0x7fc6f4cb48e0>

#usando while e tratando o erro StopIteration com o comando break que corta a execução
while True:
    try:
        elemento = next(iterador)
        print(elemento)
    except StopIteration:
        print('Erro, acabaram as iterações')
        break

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# Erro, acabaram as iterações





# #USANDO MAP
# print(list(map( lambda x: x, iterador ))) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # usamos o metodo list() para listar todos os items retornados da função map(), que basicamente recebe uma função e um iteravel

