#1) crie duas listas, uma para o carrinho do supermercado que irá receber produtos comprados e outra para preços dos produtos. Utilizando um loop, preencha as listas com 5 produtos e 5 preços, recebendo esses dados do usuario(input). Por fim, some os preços, imprima o valor total e os produtos do carrinho.





print('------------------- BEM VINDO AO SUPERMERCADO-------------------')

print('--------------ESCOLHA OS ITENS PARA COMPRA------------------')


carrinho = input('Digite os items da compra: ').split(' ')
precos = input('Digite o preço dos produtos em ordem: ').split(' ')
listaFechada = []
totalPrecos = []

for item in carrinho:
    listaFechada.append(item)
        
for valor in precos:
    totalPrecos.append(float(valor))
    listaFechada.append(float(valor))
    
totalCompra = sum(totalPrecos)

print(f'\nconfira por favor o carrinho de compras: items: {carrinho}, valor{precos} TOTAL : R${totalCompra} reais')

confirma = str(input('Digite "S" para confirmar e "N" para cancelar a compra: ')).upper()
compraConfirmada = False

if confirma == 'S':
    print('compra confirmada')
    compraConfirmada = True
else:
    print('recusado')
    compraConfirmada = False
    

if compraConfirmada == True:
    print(f'Total da compra: {totalCompra} ')
    print('------------Compra encerrada, tenha um otimo dia!---------------')
else:
    print('Por favor inicie o processo novamente!')








# resolução professor:


listaCarrinho = []

listaPrecos = []

contProdutos = 0

valorTotal = 0

produto = ''


while contProdutos < 5:
    produto = input('Produto: ')
    listaCarrinho.append(produto)
    preco = float(input('Preço produto: '))
    listaPrecos.append(preco)
    contProdutos += 1
    
print(listaCarrinho)
print(listaPrecos)

for item in range(0,5):
    valorTotal += listaPrecos[item]
    
print(f'Produtos comprados: {listaCarrinho}')
print(f'Valor total: R${valorTotal}')