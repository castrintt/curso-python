# 1) Está acontecendo uma gincana na escola e você foi escolhido(a) para realizar o contorle da pontuação! Para isso, crie 4 listas (a primeira com nome das pessoas que participam da gincana). As outras 3 cada uma representando uma prova armazenam valores de 0 a 100, ou seja, as notas que cada participanente obteve. Por fim, utilize zip() para retornar um dicionario com o nome de cada aluno como chave e o somatório de suas notas em cada prova como valor. Após isso imprima o participante vencedor.



# minha resolução 

# criando listas bases
nomes = ['marcelo','igor','beatriz','isabela'] 
prova1 = [50,50,20,80]
prova2 = [70,20,50,60]
prova3 = [100,20,40,90]

#juntando listas de provas 
juntarListas = list(zip(prova1,prova2,prova3))

totalNotas = [] # declarando uma lista vazia para posteriormente guardar a soma das notas de cada aluno

for item in juntarListas:
    totalNotas.append(sum(item))


finalNotasAlunos = dict(zip(nomes,totalNotas))

for chave, valor in finalNotasAlunos.items():
    print(f'Aluno: {chave} // Nota Final: {valor}')

# Aluno: marcelo // Nota Final: 220
# Aluno: igor // Nota Final: 90
# Aluno: beatriz // Nota Final: 110
# Aluno: isabela // Nota Final: 230
    
# print(finalNotasAlunos) # {'marcelo': 220, 'igor': 90, 'beatriz': 110, 'isabela': 230}

for nome, notas in finalNotasAlunos.items():
    if notas == max(finalNotasAlunos.values()):
        print(f'O aluno com mais pontos foi: {nome} com {notas} pontos!') # O aluno com mais pontos foi: isabela com 230 pontos!


# resolução professor


nomes = ['maria joaquina','dom pedro','nopoleão','chaves','jeniffer lopez']

provaCorrida = [2,7.5,9,8.67,6.8]
provaEscalada = [1,8,4,6.3,9,1]
provaOperMatem = [0,8.7,5.8,10,4.3]

listaNotas = []

tabela = zip(provaCorrida,provaEscalada,provaOperMatem)

for notas in tabela:
    listaNotas.append(sum(notas))
    
tabelaFinal = zip(nomes,listaNotas)

dicionarioFinal = dict(tabelaFinal)

vencedor = ''

pontos = 0 

for part, pts in dicionarioFinal.items():
    print(f'Participante: {part}. Pontos: {pts}')
    if pts > pontos:
        pontos = pts
        vencedor = part
        
print(f'\nVencedor : {vencedor}  - Pontos: {pontos} ')