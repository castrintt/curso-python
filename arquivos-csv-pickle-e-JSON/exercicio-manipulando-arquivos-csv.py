# 1 ) Um time de futsal formado pelo arquivo atletas.csv, que contem:
#  nome, altura(cm) e peso(kg) de cada esportista 
# deseja fazer uma pesquisa e saber quais atletas tem altura superior a 170cm e que possui peso menor que 80kg, imprima o nome deles.
#  Dois reforços entraram para o time no inicio da temporada:
#  Roberto, 177, 77kg e Adriano. 165,60kg; 
# Atualize o arquivo adicionando os jogadores e leia-o novamente

# a+ - adiciona no final
from csv import DictReader, DictWriter, writer, reader


listaAtletas = []
# adicionando atletas
with open('atletas.csv','w') as arquivo:

    cabecalho = 'nome','altura','peso'
    escrita = DictWriter(arquivo, fieldnames=cabecalho)
    escrita.writeheader() # criando cabecalho

    for item in range(0,3):
        nome = input('Digite o nome: ')
        altura = float(input('Digite a Altura: '))
        peso = float(input('Digite o peso: '))
        listaAtletas.append(
            
                {
                    'nome':nome,
                    'altura':altura,
                    'peso':peso
                }
            
        )
        escrita.writerow(
            {
                'nome':nome,
                'altura':altura,
                'peso':peso
            }
        )
    

    for item in listaAtletas:
        # print(item)
        if item['peso'] <  80 and item['altura'] > 170:
            print(f'Nome: {item["nome"]} , possui altura maior que 170cm e peso menor que 80kg')
    

with open('atletas.csv','a') as arquivo:
    cabecalho = 'nome','altura','peso'
    escrita = DictWriter(arquivo, fieldnames=cabecalho)

    for item in range(1,3):
        nome = input('Digite o nome do reforço: ')
        altura = float(input('Digite a altura do reforço: '))
        peso = float(input('Digite o peso do reforço: '))

        escrita.writerow(
            {
                'nome':nome,
                'altura':altura,
                'peso':peso
            }
        )
    

with open('atletas.csv','r') as arquivo:

    leitura = reader(arquivo)

    for item in leitura:
        print(item)

