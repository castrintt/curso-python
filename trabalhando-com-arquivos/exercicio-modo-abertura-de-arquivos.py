# 1) teste se um arquivo chamado livros.txt não exista pela abertura x, caso o arquivo ja exista abre com w+, utilize try/except nessa manipulação.
# Imprima na tela qual foi o modo de abertura, escreva no bloco o nome dos três melhores livros que voce ja leu (um em cada linha) adicionando ao arquivo, feche-o. Abra-o novamente e adiciona mais livros ao final do arquivo sem apaga-lo, por fim, leia a versão final

try:
    with open('livros.txt','x') as li:
        print('Modo de abertura "x"')
except FileExistsError:
    with open('livros.txt','w+') as li:
        print('Modo de abertura w+')
        li.write('Pense e enriqueça\n')
        li.write('ponto de impacto\n')
        li.write('De volta ao monasterio\n')
    if li.closed == True:
        with open('livros.txt','a+') as li:
            print('Modo a+')
            li.write('Gustavo Cerbasi, investimentos inteligentes')
    if li.closed == True:
        with open('livros.txt','r+') as li:
            print(li.read()) 

            # Pense e enriqueça
            # ponto de impacto
            # De volta ao monasterio
            # Gustavo Cerbasi, investimentos inteligentes