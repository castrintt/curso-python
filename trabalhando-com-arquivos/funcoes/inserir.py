if __name__ != '__main__':
    def inserir():
        with open('notasEscola.txt','a') as txt:
            try:
                alunos = input('Digite o nome do aluno: ')
                teste = int(alunos)
            except:
                try:
                    notas = int(input(f'Digite a nota do aluno {alunos}: '))
                except:
                    print('Nota invalida, por favor tente novamente')
                    return inserir()
                else:
                    txt.write(f'{alunos} - {notas}\n')
            else:
                print('Ocorreu algum erro, tente novamente (nome invalido)')
                return inserir()
            finally:
                print('Cadastro finalizado!')
            