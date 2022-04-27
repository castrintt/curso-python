# 1) faça um programa utilizando um arquivo chamado 'notasEscola.txt' para gerenciar as notas de alunos de uma classe. O main deve conter um menu com as seguintes opções: 

# a)  inserir alunos e notas

# b) exibir os alunos e media final

# c) alunos aprovados e reprovados

# d) Sair.

# produza uma função para cara opção


# minha resolução
# coloquei como parametro para ser aprovado ter nota acima de 6

from curses import nonl
from funcoes.exibir import exibir
from funcoes.inserir import inserir
from funcoes.status_aluno import aprovacoes


def programa():
    global listaAlunos, listaNotas
    condicao = 0
    while condicao != 1:
        try:
            opcao = int(input('Digite uma opção: \n1 -Inserir alunos\n2- Exibir alunos/notas e media final\n3- Alunos aprovados e reprovados\n4- Sair.\n'))
        except:
            print('Valor inserido para as opções deve ser inteiro!')
            print('Tente novamente!')
            return programa()
        else:
            if opcao == 1:
                inserir()
            elif opcao == 2:
                exibir()
            elif opcao == 3:
                aprovacoes()
            elif opcao == 4:
                condicao = 1
    return

programa()
