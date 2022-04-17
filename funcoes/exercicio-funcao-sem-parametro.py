import pdb


# for realizada uma pesquisa de algumas caracteristicas e gostos de quatro habitantes incluindo:
# nome, sexo, esporte favorito (natação, futebol volei e tenis) e idade.
#com esses dados faça:

#função que armazene os dados em uma lista. Dica: use dicionarios dentro da lista.

# calcule a idade média de homens que gostam de natação. Caso não haja homens que gostam de natação chame uma função e imprima um aviso de que não há homens que gostam de natação

# minha resolução


lista = []

def pesquisa(lista):
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite: M para sexo masculino e F para sexo feminino: ')
    sexoEscolhido = sexo.upper()
    esporte = input('Digite seu esporte favorito dentre (natação, futebol volei e tenis) : ')
    esporteEscolhido = esporte.upper()
    candidado = input('Existem mais candidatos? S para sim e N para não: ')
    proximoCandidato = candidado.upper()
    
    dicionario = dict(nome=nome,idade=idade,sexo=sexoEscolhido,esporteFavorito=esporteEscolhido)

    lista.append(dicionario)
    
    if proximoCandidato == 'S':
        pesquisa(lista)
    else:
        return 
   
    
pesquisa(lista)

print(lista)
print('\n')

# mascNatacao =  []

# for item in lista:
#     if item['esporteFavorito'] == 'NATACAO' and item['sexo'] == 'M':
#         mascNatacao.append(item['esporteFavorito'])

# print(mascNatacao.count('NATACAO'))


masc = list(filter(lambda item: item['esporteFavorito'] == 'NATACAO' and item['sexo'] == 'M', lista))


print(f'O total de homens que gostam de natação é igual a {len(masc)}')


soma = sum(n['idade'] for n in masc)

media = soma / len(masc)

print(media)







# resolução professor

def cadastro():
    list = []
    for i in range(4):
        dicionario = dict(nome = input('Digite seu nome: '),
                          sexo = input('digite M para masculino e F para feminino'),
                          esporte = input('Digite seu esporte favorito'),
                          idade = int(input('Digite sua idade: ')))
        list.append(dicionario)
    return list
    
    
lista = cadastro()
    
cont = 0
soma = 0

print(lista)

def aviso():
    print('Nenhum homem gosta de natação!')

for indice,item in enumerate(len(lista)):
    if lista[indice]['sexo'] == 'M' and lista[indice]['esporte'] == "natacao":
        soma = soma + lista[indice]['idade']
        cont += 1

if cont == 0:
    aviso()
else:
    media = soma / cont
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    