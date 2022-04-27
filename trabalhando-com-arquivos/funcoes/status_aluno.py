if __name__ != '__main__':
    def aprovacoes():
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
                if item[1] > 6:
                    print(f'Aluno: {item[0]} Nota : {item[1]}  --> Aprovado')
                elif item[1] <= 6:
                    print(f'Aluno: {item[0]} Nota : {item[1]}  --> Reprovado')
