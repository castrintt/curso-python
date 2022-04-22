# 1) Crie 3 listas: uma com nome de 3 companhias aéreas,

# e as outras duas representando o numero de passageiros por companhia em dois voos: voo1 e voo2.

# Utilize zip(), lambda e map() para obter o valor maximo de passageiros por companhia nos dois voos e associar estes valores com o nome das companhias formando uma lista de tuplas.

# Por fim, utilizar filter() e lambda para determinar a classificação da companhia, conforme indicado nos dados abaixo

# Dados:
# 0 < passageiros <= 100: 1 estrela.
# 100 < passageiros <= 200: 2 estrelas
# 200 < passageiros <= 300: 3 estrelas


# minha resolução


companhias = ['gol','tap','air canada']

voo1 = [140,120,50]

voo2 = [60,200,260]

voosJuntos = zip(voo1,voo2)

# print(list(voosJuntos)) # [(140, 60), (120, 200), (50, 260)]

resultado = map(lambda voos: max(voos), voosJuntos)

# ------------------------------------------------
#  lambda a cima seria a mesma coisa que:


# def achaMaior(lista):
#     novaLista = []
#     for items in lista:
#         novaLista.append(max(items))
#     return novaLista

# print(achaMaior(voosJuntos)) # [140, 200, 260]
        
# --------------------------------------------------

# print(list(resultado)) # [140, 200, 260]

companhiasEResultados = list(zip(companhias, resultado))

# print(companhiasEResultados) # [('gol', 70), ('tap', 70), ('air canada', 43)]

filtro1 = list(filter(lambda item: item[1] <= 100 and 0 < item[1], companhiasEResultados))
filtro2 = list(filter(lambda item: item[1] <= 200 and 100 < item[1], companhiasEResultados))
filtro3 = list(filter(lambda item: item[1] <= 300 and 200 < item[1], companhiasEResultados))

print(f'{filtro1} é uma estrela')
print(f'{filtro2} tem 2 estrelas')
print(f'{filtro3} tem 3 estrelas')



# --------------------------------------- fazer isso porem com filter ---------------------

# for items in companhiasEResultados:
#     if 0 < items[1] and items[1] <= 100:
#         print(f'{items[0]} é 1 estrela')
#     elif  100 < items[1] and items[1] <= 200:
#         print(f'{items[0]} é 2 estrelas')
#     elif 200 < items[1] and items[1] <= 300:
#         print(f'{items[0]} é 3 estrelas')

# # gol é 1 estrela
# # tap é 1 estrela
# # air canada é 1 estrela

# ---------------------------------------------------------------------------------


# rascunho
# def verifica(lista):
#     global listaVencedores
#     listaLocal = []
#     for indice, valor in enumerate(lista):
#         listaLocal.append(lista[indice][1])
#     for indice,valor in enumerate(lista):
#         if max(listaLocal) == valor[1]:
#             listaVencedores.append(valor)
#     return listaVencedores

 
# numeroPassageirosMax1 = 0

# empresaVencedora1 = ''

# for indice, valor in enumerate(compV1):
#     print(indice, valor)
#     if valor[1] > numeroPassageirosMax1:
#         numeroPassageirosMax1 = valor[1]
#         empresaVencedora1 = valor[0]
        

# print(numeroPassageirosMax1) # 70
# print(empresaVencedora1) # tap


# numeroPassageirosMax2 = 0

# empresaVencedora2 = ''

# for indice, valor in enumerate(compV2):
#     print(indice, valor)
#     if valor[1] > numeroPassageirosMax2:
#         numeroPassageirosMax2 = valor[1]
#         empresaVencedora2 = valor[0]
        
# print(numeroPassageirosMax2) # 70
# print(empresaVencedora2) # gol





#_______________________________________________________________________________________________________



# Resolução professor

companhias = ['gol','tap','air canada']

voo1 = [140,120,50]

voo2 = [60,200,260]


voos1e2 = zip(voo1,voo2) # junta os numeros de passageiros de cada companhia

maxPass = map(lambda voos: max(voos), voos1e2) # determina o valor max de passageiros por companhia entre, os voos 1 e 2

#print(list(maxPass)) # [140, 200, 260]

listaMaxPass = list(maxPass)

compMax = zip(companhias, listaMaxPass)

listaCompMax = list(compMax)

umaEst = list(filter(lambda valMax: valMax[1] <= 100, listaCompMax))
duasEst = list(filter(lambda valMax: valMax[1] <= 200  and 100 < valMax[1], listaCompMax))
tresEst = list(filter(lambda valMax: valMax[1] <= 300  and 200 < valMax[1], listaCompMax))

print(f'Uma estrela: {umaEst[0][0]}')
print(f'Duas estrelas: {duasEst[0][0]}')
print(f'Tres estrelas: {tresEst[0][0]}')