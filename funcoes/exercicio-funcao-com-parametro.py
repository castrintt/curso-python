# 1) criar uma função recursiva ( que retorna ela mesma ) para armazenar N termos da sequência de Fibonacci em uma lista. N é definido pelo usuario. Ao encontrar os termos, imprimir a lista e finalizar a função


# 2) criar 5 funções: uma para um cadastro, outra para realizar o login, outra para mudar a senha, outra para realizar logout e ainda uma para definir qual opção o usuario deseja escolher. Utilize um loop while para sair do sistema apenas se o usuario desejar ( criar a opção 'sair').
# atente-se as regras:

# Só é possivel realizar um cadastro se não houver nenhum anterior.

# Só é possivel realizar login se houver um cadastro.

# Só é possivel realizar login se o usuario informar corretamente username e senha.

# Só é possivel alterar a senha se o usuario estiver logado.

# Só é possivel alterar a senha se o usuario informar corretamente a senha atual

# Só é possivel realizar logout se o usuario estiver logado.

import pdb


#  resolução exercicio 1

#fibonacci

def fibonacci():
    escolha = int(input('Quantos termos deseja mostrar? '))
    #pdb.set_trace()
    listaFibo = [1 + (n + (n-1)) for n in range(1,(escolha + 1))]
    
    return listaFibo

print(fibonacci())