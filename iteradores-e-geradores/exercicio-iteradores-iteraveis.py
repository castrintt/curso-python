# 1) um estudante do curso programando ideias acabou de assistir a aula de diferença entre iteraveis e iteradores, para praticar mais, criou um programa que realiza o precosso de um for, porem sem utilizar a ferramente for diretamente, segue o codigo desenvolvido


# def desmembra_iteravel(iteravel):
#     while True:
#         try:
#             print(next(iteravel))
#         except StopIteration:
#             print('Chegamos ao ultimo elemento')
#             break

# desmembra_iteravel([1,2,3,4,5,6,7,8])

        # o estudante percebeu que o codigo estava apresentando o seguinte erro:
        # TypeError: 'list' object is not an iterator

#porem , não sabe como corrigir. Altere o programa do estudade para fazer funcionar corretamente e explique o que aconteceu.


def desmembra_iteravel(iteravel): 
    iterador = iter(iteravel)
    while True:
        try:
            print(next(iterador))
        except StopIteration:
            print('Chegamos ao ultimo elemento')
            break

desmembra_iteravel([1,2,3,4,5,6,7,8])

# o erro foi bem simples, ele não declarou que o 'iteravel' que ele iria receber na função era um iterador, portanto, primeiro eu criei uma variavel que transforma o dado que ele iria mandar em um iterador isando o comando iter():
            # iterador = iter(iteravel)
#logo em seguida substitui no try para que o print() enviasse a variavel que guarda o retorno como iterador:
            # print(next(iterador))
# e pronto! o programa roda normalmente
