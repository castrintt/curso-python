"""
 1 ) Um escritor de livros pretende escrever e lançar edições para atingir a quantia de 1 milhão de reais.

 Simplismente por este motivo, crie uma classe que recebera em seu metodo construtor o nome do livro e o numero de paginas.

 Alem disso, tambem deve ser criado um atributo construtor para a edição do livro, que sera atualizada em uma unidade a cada livro que for publicado.

 Por fim, utilize o randint() para gerar um valor entre 0 e 500 mill, representando a arrecadação das vendas, o ultimo atributo do construtor.

 Crie o metodo magico __repr__ para representar o nome do livro e a edicao. Ainda, utilize o __len__ para determinar o numero de paginas de cada livro. Por fim, verifica se o valor total de arrecadações atingiu 1 milhao de reais
"""

from random import randint as rd

class Livro:
    def __init__(self, nome,paginas,publicacoes):
        self.nome = nome
        self.paginas = paginas
        self.publicacoes = publicacoes
        self.__edicao = self.publicacoes
        self.__arrecadacao = rd(0, 500000)


    def __repr__(self):
        return f'Nome do livro: {self.nome}\nEdição: {self.__edicao}'


    def __len__(self):
        return self.paginas  

    def verifica_valor(self):
        valorTotal = (self.publicacoes * self.__arrecadacao)
        if valorTotal >= 1000000:
            return f'Valor de vendas atingiu 1 milhao!!!'
        else:
            return f'Faltam {1000000 - valorTotal} vendas para completar 1 Milhão de reais! '


senhorDosAneis = Livro('senhor dos aneis',800,30)

print(senhorDosAneis)

print(senhorDosAneis.verifica_valor())

print(len(senhorDosAneis))

# Nome do livro: senhor dos aneis
# Edição: 30
# Valor de vendas atingiu 1 milhao!!!
# 800