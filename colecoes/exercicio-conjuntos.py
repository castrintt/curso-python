# # ex 1) Sami e Dudu irão fazer uma competição de quem visita mais Estados no Brasil em um periodo de 6 meses, até então Dudu já visitou ES e SP , enquanto Sami visitou RJ e BA.

# # crie dois conjuntos diferentes para simbolizar os estados que cada um foi. Após 6 meses Dudu visitou BA, AC, ST, SE , equanto Sami visitou BA, MG, AM, PR , atualize cada um dos conjuntos com os novos Estados. RESPONDA:

#  # - 1) Quais estados Dudu Visitou que Sami não foi?
 
#  # - 2) Quais estados ambos foram? 
 
#  # - 3) Sendo 27 estados no Brasil toto, qual porcentagem o vencedor visitou?
 
# dudu = { 'SP','ES' }
# sami = { 'RJ','BA' }

# print('\nATENÇÃO DIGITE OS PAISES SEPARANDO POR ESPAÇOS\n')

# novosLugaresVisitadosPorDudu = input('\nDigite os estados que Dudu visitou: \n').split(' ')
# novosLugaresVisitadosPorSami = input('\nDigite os estados que Sami visitou: \n').split(' ')



# dudu = dudu.union(set(novosLugaresVisitadosPorDudu))
# sami = sami.union(set(novosLugaresVisitadosPorSami))

# #print(dudu) # {'Espirito Santo', 'Santa Catarina', 'Sergipe', 'Acre', 'São Paulo', 'Bahia'}
# #print(sami) # {'Rio de Janeiro', 'Amazonas', 'Minas Gerais', 'Bahia', 'Parana'}


# # pergunta 1


# paisesQueDuduVisitouESamiNao = dudu.difference(sami)

# #print(paisesQueDuduVisitouESamiNao) # {'Acre', 'Espirito Santo', 'Santa Catarina', 'São Paulo', 'Sergipe'}

# print(f'\nPaises que Dudu visitou, mas Sami não foi: {paisesQueDuduVisitouESamiNao}\n')


# print('\n')

# # pergunta 2


# paisesQueAmbosVisitaram = dudu.intersection(sami)

# #print(paisesQueAmbosVisitaram) # {'Bahia'}

# print(f'\nOs paises que ambos visitaram foram {paisesQueAmbosVisitaram}\n')


# print('\n')

# # pergunta 3


# totalPaises = 27
# porcentagemDudu = 0
# porcentagemSami = 0
# porcentagemAmbos = 0

# if len(dudu) > len(sami):
#     porcentagemDudu += ((len(dudu) / 27 ) * 100).__round__()
#     print(f'\nO vencedor foi Dudu com a porcentagem de paises visitados igual a {porcentagemDudu}%\n')
# elif len(dudu) < len(sami):
#     porcentagemSami += ((len(sami) / 27) * 100).__round__()
#     print(f'\nA vencedora foi Sami com a porcentagem de paises visitados igual a {porcentagemSami}%\n')
# else:
#     porcentagemAmbos += ( (len(paisesQueAmbosVisitaram) / 27) * 100 )
#     print(f'\nAmbos visitaram a mesma quantidade de paises a porcentagem foi de : {porcentagemAmbos}\n')



# resolução professor



estados_sami = { 'RJ','BA' }
estados_dudu = { 'ES','SP' }


sair = ''
while sair != 'nao':
    estados_sami.add(input('Qual Estado Sami visitou a Mais? '))
    sair = input('Tem mais Estados a adicionar? ')

sair = ''
while sair != 'nao':
    estados_dudu.add(input('Quais Estados Dudu visitou a mais? '))
    sair = input('Tem mais Estados a adicionar? ')

inter = estados_dudu.intersection(estados_sami)
print(estados_dudu.difference(estados_sami))
print(inter)

if len(estados_sami) > len(estados_dudu):
    print(f'Sami ganhou e visitou {len(estados_sami) * 100 // 27 }%')
elif len(estados_sami) < len(estados_dudu):
    print(f'Dudu ganhou e visitou {len(estados_dudu) * 100 // 27}%')
else:
    print(f'Deu empate e ambos visitaram {len(estados_dudu) * 100 // 27}%')