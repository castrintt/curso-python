# crie dois arquivos:  um CSV e um JSONPICKlE. Escreva os lucros de uma empresa em um balanço trismetral, apresentando o mes e o lucro em milhoes no CSV, e as despesas nos mesmos meses em JSONPICKLE a partir dos objetos criados com uma classse chamada Empresa. Após isso, troque seus conteudos, ou seja, armazene os valores dos lucros no JSONPICKLE e os valores de despesa no CSV

from csv import reader, writer , DictReader, DictWriter
import jsonpickle

with open('empresa.csv','w') as capital:

    balanco = 'mes','lucro'

    escrita = DictWriter(capital, fieldnames=balanco)

    escrita.writeheader()

    condicao = 0

    while condicao != 3:
        mes = input('Digite o mes: ')
        lucro = float(input('Digite o lucro: '))

        escrita.writerow({
            'mes':mes,
            'lucro':lucro,
        })

        condicao += 1



# with open('empresa.csv','r') as capital:
    
#     leitura = DictReader(capital)

#     for item in leitura:
#         print(item)

# {'mes': 'janeiro', 'lucro': '12837192.0', 'despesas': '1283.0'}
# {'mes': 'fevereiro', 'lucro': '123891278.0', 'despesas': '12213.0'}
# {'mes': 'março', 'lucro': '1238.0', 'despesas': '1238127389.0'}


class Empresa:

    def __init__(self, jan, despJan, fev, despFev, mar, despMarc):
        self.jan = jan
        self.despJan = despJan
        self.fev = fev
        self.despFev = despFev
        self.mar = mar
        self.despMarc = despMarc

    

empresa1 = Empresa('janeiro',21391232.231,'fevereiro',12038912903.2,'março',1289038901.210)


with open('capital.json','w') as capital:

    capital.write(jsonpickle.encode(empresa1))


# with open('capital.json','r') as capital:

#     ler = jsonpickle.decode(capital.read())

#     print(ler.jan)
#     print(ler.fev)
#     print(ler.mar)




with open('empresaNovo.csv','w') as capital:

    balanco = 'mes','despesa'

    escrita = DictWriter(capital, fieldnames=balanco)

    escrita.writeheader()

    condicao = 0

    while condicao != 3:
        mes = input('Digite o mes: ')
        despesa = float(input('Digite o despesa: '))

        escrita.writerow({
            'mes':mes,
            'despesa':despesa,
        })

        condicao += 1



class EmpresaLucro:

    def __init__(self, jan, lucroJan, fev, lucroFev, mar, lucroMarc):
        self.jan = jan
        self.lucroJan = lucroJan
        self.fev = fev
        self.lucroFev = lucroFev
        self.mar = mar
        self.lucroMarc = lucroMarc


empresa2 = EmpresaLucro('janeiro',128371289.123,'fevereiro',128937128.2,'março',128937129.22)



with open('capitalLucro.json','w') as capital:

    capital.write(jsonpickle.encode(empresa2))