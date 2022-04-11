# 1) criar um sistema de comando de uma loja de jogos. O programa deve conter pelo menos 6 listas.
    # 1- indicando quais jogos estão disponiveis para venda
    # 2- mostra o preço de cada jogo
    # 3- quantidade de jogos disponiveis 
    # 4- informando o preço de fabrica dos jogos para aumentar o estoque
    # 5- registrar as vendas
    # 6- registrar compra de estoque
#todas as informações de um jogo devem estar no mesmo indice nas listas. Criar um menu interativo com as seguintes opções para o usuario: registrar venda, Compra de estoque, resumo da loja, sair. Ao sair indicar que o caixa está fechado. O usuario deve controlar o sistema da loja, registrando as vendas e as compras de estoque, sem esquecer de alterar os valores da lista de quantidade


print('============Bem vindo a loja de games---------------')


jogosDisponiveis = []
precoJogos = []
quantidadeJogos = []
precoFabrica = []
contador = 1
saldoLoja = 0

while contador != 0:   
    jogos = input('\nCadastro de jogo Disponivel: ').upper()
    if jogos == "pare".upper():
        break
    preco = float(input('\nPreço Jogo: '))
    fabrica = float(input('\nPreço de Fabrica: '))
    print('\nDigite "pare" para parar o cadastro de jogos: ')
    jogosDisponiveis.append(jogos)
    precoJogos.append(preco)
    precoFabrica.append(fabrica)
    contador += 1  
     
quantidadeJogos = len(jogosDisponiveis)
   
for indice, item in enumerate(jogosDisponiveis):
    print(f'Jogo: {jogosDisponiveis[indice]}, preço: R${precoJogos[indice]} reais,  preço de fabrica: R${precoFabrica[indice]} reais')

print(f'\n TOTAL DE JOGOS CADASTRADOS : {quantidadeJogos}')

print('\n------------Sistema de vendas-------------')

listaVendas = []
ListaCompraEstoque = []


for item in jogosDisponiveis:  
    vendas = input('\nQual jogo deseja comprar? ').upper()
    if vendas in jogosDisponiveis: 
        indice = jogosDisponiveis.index(vendas)
        confirmaCompra = input(f'Deseja comprar o jogo {jogosDisponiveis[indice]} ? se SIM digite  " s " , se NÂO digite  " n ": \n').upper()
        if confirmaCompra == 'S':
            listaVendas.append(jogosDisponiveis[indice])
            jogosDisponiveis.pop(indice)
            precoFabrica.pop(indice)
            saldoContagemVenda = precoJogos.pop(indice)
            quantidadeJogos -= 1
            saldoLoja += saldoContagemVenda
            print('\ncompra realizada com sucesso, volte sempre!'.upper())      
            break
        elif confirmaCompra == 'N':
            print("Tente novamente !")
            break                                 
    else:
        print('Jogo indisponivel no momento! Faremos uma requisição para a compra de um novo!')
        break
     
    
             
print(f'\nLista de jogos Vendidos: {listaVendas}')
print(f'\nJogos ainda disponiveis: {jogosDisponiveis}')
print(f'\nPreço dos jogos ainda disponiveis: {precoJogos}')
print(f'\nQuantidade de jogos disponiveis: {quantidadeJogos}')
print(f'\nPreço de fabrica dos jogos disponiveis: {precoFabrica}')  
print(f'\nSaldo final loja : {saldoLoja}')



print('\n------------------------ ESTOQUE ------------------------')


estoque = listaVendas + jogosDisponiveis

print(estoque)

compraEstoque = input('Deseja realizar uma compra para repor estoque? "S" "N"').upper()

for item in estoque:
    if compraEstoque == 'S':
        print(f'\n ------- items no estoque -------')
        print(f'\n{estoque}')
        escolha = input('Qual jogo você deseja recomprar? ').upper()
        if escolha in estoque:
            print(f'\nrecompra jogo: {escolha}, preço: R${precoFabrica[estoque.index(escolha)]} reais')
            saldoLoja -= precoFabrica[estoque.index(escolha)]
            jogosDisponiveis.append(escolha)
            break
        else:
            print('\nJogo não está no estoque')
            break
    else:
        print('Volte sempre!')
        break
    
print(f'\nSaldo final loja: {saldoLoja}, jogos disponiveis: {jogosDisponiveis}')
