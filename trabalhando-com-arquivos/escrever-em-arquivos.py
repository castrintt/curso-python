# Escrita em Arquivos
# quando abrimos um arquivo o modo padrão é r 'read', para escrevermos nele, precisamos mudar o modo do arquivo para W 'write'
# ao abrir o arquivo pelo modo padrao, é possivel apenas realizar a leitura.
# ex - arquivo = open('lucro.txt')

# PARA FAZER A ESCRITA DEVEMOS MUDAR O MODO DE ABERTURA DE 'r' PARA 'w' 

# PARA MUDAR PARA DIFERENTES MODULOS BASTA PASSAR COMO PARAMETRO NA ABERTURA DO MESMO, 
#  ex ; - sintaxe arquivo = open('arquivo.txt','w') # alteramos para o modo de escrita


# temos duas opções, podemos fazer com que o proprio python crie o arquivo e escreva nele, como tbm podemos alterar o texto de um arquivo ja existente


# 1 ) Alterando a escrita de um arquivo ja existente:
#lembrando que o conteudo é completamente substituido
# para escrevermos mais linhas, ou mais conteudo, basta chamar a função write novamente

arquivo = open('lucros.txt', 'w')

arquivo.write('Janeiro: quebramos!\n')
arquivo.write('Fevereiro: roubamos do povo!')

arquivo.close()

arquivo = open('lucros.txt','r')

print(arquivo.read())

# Janeiro: quebramos!
# Fevereiro: roubamos do povo!


# 2) criando um arquivo --> para isso usamos a mesmo função open() se o arquivo não existir o python automaticamente cria ele
# ex

with open('novo-arquivo-de-texto-criado-pelo-python.txt', 'w') as txt:# acabamos de criar e escrever dentro desse arquivo
    txt.write('Meu nome é igor, seja bem vindo a mais uma aula de python\n')
    txt.write('Acabamos de criar esse arquivo txt usando python')

with open('novo-arquivo-de-texto-criado-pelo-python.txt', 'r') as txt:
    print(txt.read())
    # Meu nome é igor, seja bem vindo a mais uma aula de python
    # Acabamos de criar esse arquivo txt usando python




# 3) podemos escrever em arquivos usando dados: 
# ex

# primeiro vamos criar um novo arquivo de forma pythonica

with open('Novo.txt','w') as new:
    while True:
        frase = input('Digite uma frase, ou digite o comando "sair" para sair do programa: ')
        if frase != 'sair':
            new.write(f'{frase}\n')
        else:
            break

with open('Novo.txt','r') as new:
    print(new.read())
    # dentro do arquivo novo pode ver que eu escrevi a seguinte frase, voce pode alterar ela sempre que quiser, basta executar esse programa para que o loop while faça seu trabalho!
    # ola
    # meu nome é igor
    # estou escrevendo em um arquivo txt usando Python!!
    # olha que coisa legal!