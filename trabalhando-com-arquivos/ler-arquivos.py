# foi criado o arquivo lucros.txt, com dados:

# janeiro - R$ 12.560,00
# fevereiro - R$ 65.987,00
# março - R$ 12.876,00

# como podemos acessar esse arquivo txt e trabalhar com eles?

# abrir o arquivo: função -> open(endereço em que se encontra o arquivo)
# a abertura padrao é do modulo leitura  (mode 'r' - read)

from binascii import a2b_qp


arquivo = open('lucros.txt')

print(arquivo) 

 #<_io.TextIOWrapper name='lucros.txt' mode='r' encoding='UTF-8'>
   # tipo do arq.    #nome do arq     #modo de abertura   # codificação

#usando o open() nós abrimos o arquivo, agora precisamos ler um arquivo

# LER ARQUIVO - função read() - realiza a leitura do arquivo
#sintaxe arquivo.read()

#ex 

print(arquivo.read())
# janeiro - R$ 12.560,00
# fevereiro - R$ 65.987,00
# março - R$ 12.876,00


# OBS --> quando usamos a função read() ele lê o codigo todo (como se o cursor fosse passando dado a dado, porem ele para no final da leitura e não volta para o inicio)
#portando para lermos um mesmo arquivo de novo, podemos fazer de diversas formas, uma delas é abrindo o arquivo de novo (que não é a melhor forma [porem mais a frente veremos as melhores formas])

arquivo = open('lucros.txt')
#dessa forma podemos novamente usar a função read

print(arquivo.read())
# janeiro - R$ 12.560,00
# fevereiro - R$ 65.987,00
# março - R$ 12.876,00


# ARMAZENANDO A LEITURA DO ARQUIVO EM UMA VARIAVEL
# o metodo read, armazena os dados em forma de string

arquivo = open('lucros.txt')

leitura = arquivo.read()

print(type(leitura)) # <class 'str'> # string

# PODEMOS LIMITAR A QUANTIDADE DE CARACTERES LIDOS NA FUNÇÃO READ PASSANDO COMO PARAMETRO O NUMERO DE CARACTERES 
# delimitando a quantidade de caracteres (avanços do cursor)
# Ex

arquivo = open('lucros.txt')

leituraDe5Caracteres = arquivo.read(5)

print(leituraDe5Caracteres) # janei # ou seja, leu somente 5 caracteres do arquivo



# PARA FECHARMOS UM ARQUIVO PODEMOS USAR A FUNÇÃO CLOSE()

# sintaxe; arquivo.close()

# devemos fechar os arquivos sempre depois do uso, pois quando abrimos um arquivo ele inicia uma conexão com esse arquivo, devemos finalizar essa conexão pós uso!
# ESSA CONEXÃO É CONHECIDA COMO STREAMING

arquivo.close() # fecha o arquivo

# para verificarmos se um arquivo esta de fato fechado basta usar a sintaxe

# print(arquivo.closed) # --> se retornar False o arquivo esta aberto, se retornar True o arquivo esta fechado

print(arquivo.closed) # True







# MODO PYTHONICO DE TRABALHAR COM ARQUIVOS

# palavra reservada with -(com)

#VAMOS USAR O WITH JUNTO AO ALIAS(AS)

#Ele é usado para garantir finalização de recursos adquiridos.

# Um arquivo, por exemplo é aberto. Quem garante que ele será fechado? Mesmo que você coloque no código de forma explícita que ele deve ser fechado, se ocorrer uma exceção, o código sai de escopo sem executar o resto do código que está em escopo, ele pula o fechamento.

# Para evitar isto usamos um try finally. O finally garante a finalização. Como o código fica um pouco longo e este caso é bastante frequente a linguagem providenciou uma forma simplificada com o with.

with open('lucros.txt') as luc:
    print(luc.read())
    # janeiro - R$ 12.560,00
    # fevereiro - R$ 65.987,00
    # março - R$ 12.876,00

# COM O WITH GARANTIMOS O FECHAMENDO DO PROGRAMA AO SAIR DA IDENTAÇÃO DELE
# ou seja enquanto voce estiver dentro do bloco de execução do with, o arquivo esta aberto, a partir do momento que voce sai do bloco ele fecha o arquivo por baixo dos panos com o arquivo.close()