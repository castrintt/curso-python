# 1) faça um programa que contabiliza time de herois e vilões da seguinte forma:

# = Crie um dicionario chamado heroi com chave sendo o nome do personagem e o elemento o nivel de poder do personagem entre 1 a 100 EX:  heroi = {'flash': 49 }


#- Crie um dicionario que será as armas que podem ser usadas pelo heroi, sendo a chave o nome da arma e o elemento o nivel de poder da arma EX: arma = {'escudo':49}

# - Crie um ultimo dicionario representando os vilões sendo a chave o nome e o elemento  o nivel de poder de 0  a 200. EX: vilao = {'thanos': 149}

# - Após isso o usuario podera escolher um heroi, a arma soma os pontos de poder e escolher um vilão para lutar, apresente quem foi o vencedor, caso for o heroi imprima a arma usada. Caso for empate iforme a saida.

# observação: pode definir qualquer heroi, vilao e arma que quiser


# Minha resolução

herois = {
    'Luke Skywalker': 70,
    'Princesa Leia':40,
    'Han Solo':90,
    'Obi-Wan Kenobi': 100
}

armas = {
    'Pistola Blaster Pesada Han Solo': 80,
    'Sabre de Luz Negro': 100,
    'Sabre de Luz Branco':80,
    'Rifle Blaster':100,
    'Lança Chamas':60
}

viloes = {
    'Greedo':120,
    'Boba Fett': 100,
    'Darth Vader': 180,
    'Imperador Palpatine': 160
}

heroiEscolhido = input(f'\nEscolha um Heroi: {herois}\n')
print('\n')
armaEscolhida = input(f'\nEscolha uma arma: {armas}\n')
print('\n')
vilaoEscolhido = input(f'\nEscolha o Vilão que deseja enfrentar: {viloes}\n')


poderHeroi = herois[heroiEscolhido] + armas[armaEscolhida]

poderVilao = viloes[vilaoEscolhido]

print(f'\n{heroiEscolhido} e {vilaoEscolhido} Começaram uma batalha sangrenta!')

if poderHeroi > poderVilao:
    print(f'\nO vencedor dessa batalha sangrenta foi {heroiEscolhido}!! A arma usada nessa batalha foi {armaEscolhida}!')
elif poderHeroi < poderVilao:
    print(f'\nO vencedor dessa batalha sangrenta foi {vilaoEscolhido}!!')
elif poderHeroi == poderVilao:
    print(f'{heroiEscolhido} e {vilaoEscolhido} lutaram bravamente, porém ambos guerreiros se encontram no chão! Nenhum lutador saiu vencedor!')
    
    
# resolução professor


herois = {
    'Homem aranha':85,
    'Goku': 100,
    'Flash':90
}

armas = {
    'Martelo do Thor':90,
    'Pistola da Viuva Negra':55,
    'Roupa do Pantera Negra': 80
}

viloes = {
    'Thanos': 180,
    'Venon': 145,
    'Ultron': 160
}

heroiEscolhido = input('Digite o heroi escolhido: ')
armaEscolhida = input('Digite a arma escolhida: ')
vilaoEscolhido = input('Digite o vilao escolhido: ')

nivelPoderHeroiEArma = herois[heroiEscolhido] + armas[armaEscolhida]
nivelPoderVilao = viloes[vilaoEscolhido]

if nivelPoderHeroiEArma > nivelPoderVilao:
    print(f'O vencedor é {heroiEscolhido} com {armaEscolhida}')
elif nivelPoderHeroiEArma == vilaoEscolhido:
    print('Deu empate')
else:
    print(f'O vencedor é {vilaoEscolhido}! Terra em perigo!')