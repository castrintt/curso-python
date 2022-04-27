# por enquanto ja vimos w - write e o r - read

# O modo padrao de abertura ( open(arquvivo.txt) ) é 'r', quando adicionamos o segundo parametro ao open, podemos escolher qual o tipo de arquivo

# link paras os modos https://docs.python.org/3/library/functions.html#open 

# MODOS

#  1) 'x' -> abre escrita apenas se o arquivo não existir. Se ja existir gera erro

with open('frutas.txt','x') as arq: # se eu executar o programa 2 vezes isso acontece FileExistsError: [Errno 17] File exists: 'frutar.txt'
    arq.write('Banana\n')
    arq.write('Uva\n')

# -->> para evitarmos esse tipo de erro vamos usar nossos conhecimentos de tratativa de erros com try, except, else e finally

try:
    with open('frutas.txt','x') as frutas:
        frutas.write('Banana\n')
        frutas.write('Uva\n')
except FileExistsError:
    print('Arquivo ja existe!')

# ao executar esse codigo 2 vezes ao inves de gerar um erro de FileExistsError ele simplismente retorna a mensagem do print no except



#  2) 'a' -->  o modo 'a' ele sempre adiciona uma escrita, ele não sobrescreve como vimos no modo 'w', (isso se o arquivo existir é claro), pois se ele não existir o modo 'a' simplismente cria um!

# NESSE MODO NÃO TEMOS O CONTROLE DO CURSOR, OU SEJA, NÃO PODEMOS USAR O SEEK() --> o 'a' sempre imprime no final

# ex

with open('profissionais.txt','a') as jobs: #nesse caso criamos o arquivo profissionais.txt
    jobs.write('\nProgramador')
    jobs.write('\nconfeiteiro')
    jobs.write('\nvendedor')

# agora vamos só adicionar conteudo a um ja existente
# o arquivo que vamos adicionar texto se chama 'novo-arquivo-de-texto-criado-pelo-python' e dentro dele temos o seguinte texto

# Meu nome é igor, seja bem vindo a mais uma aula de python
# Acabamos de criar esse arquivo txt usando python

# vamos adicionar mais algumas informações nele

with open('novo-arquivo-de-texto-criado-pelo-python.txt','a') as new:
    new.write('\nTenho 23 anos')
    new.write('\nE sou solteiro')

# agora dentro do arquivo temos o seguinte conteudo

# Meu nome é igor, seja bem vindo a mais uma aula de python
# Acabamos de criar esse arquivo txt usando python
# Tenho 23 anos
# E sou solteiro


#  3) '+' --> modo 'a' abre para ATUALIZAÇÃO DE LEITURA OU ESCRITA
# sintaxe :   with open('arquivo.txt','+r') as tata --> ou seja, o '+' nunca vem sozinho, ele sempre é acompanhado de algum outro modo
# sintaxe :   with open('arquivo.txt','+w') as tata --> ou seja, o '+' nunca vem sozinho, ele sempre é acompanhado de algum outro modo

# 3.1) 'r+': --> o arquivo ja deve EXISTIR, lembrando que mesmo abrindo como r+ podemos usar comandos de write, temos tbm controle do cursor

with open('profissionais.txt','r+') as pro: # ele só atualiza o arquivo
    pro.write('\npolicial')
    pro.seek(0)
    pro.write('\npolicial')
    pro.write('\npolicial')

# 3.2) 'w+': --> se o arquivo não existir ele cria , POREM ELE SOBRESCREVE OQUE JA FOR ESCRITO SE O ARQUIVO EXISTIR, TEMOS CONTROLE DO CURSOR TBM, e podemos usar comandos de leitura e de escrita

with open('herois.txt','w+') as hr:
    hr.write('\nBatman')
    hr.write('\nSuperHomen')


# 3.3) 'a+': --> se o arquivo não existir ele cria um novo --> ele simplismente escreve no final da linha tbm, Realiza leitura , porem não se pode controlar o cursor, ele sempre adiciona texto no final


with open('programas.txt','a+') as tv:
    tv.write('\nsilvio santos')
    tv.write('\nsherlock holmes')
    tv.write('\nchicago pd')
    print(tv.read())


# 3.4) 'x+': --> Cria um arquivo novo se não existir. Caso ja existir da erro (como o modo 'x' normal), temos controle de leitura e escrita, se usarmos o comando de cursor para escrever ele sobrescreve.(logo temos controle do cursor para escrita e leitura)

with open('novos-titas.txt','x+') as titas:
    titas.write('mutano')
    titas.write('robin')
    titas.write('ravena')
    titas.seek(0)
    print(titas.read())