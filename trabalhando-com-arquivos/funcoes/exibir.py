if __name__ != '__main__':
    def exibir():
        with open('./notasEscola.txt','r') as alunos:
            leitura = alunos.read()
            separador = leitura.replace(' - ',' ').replace('\n',',').replace(' ',',').split(',')
            separador.pop(separador.index(''))
            alunos = separador[::2]
            notas = separador[1::2]
            notas = [int(nota) for nota in notas]
            media = sum(notas) / len(notas)
            alunosNotas = list(zip(alunos,notas))
            for item in alunosNotas:
                print(f'Aluno: {item[0]} Nota : {item[1]}')
            print(f'Media Global: {round(media)}')