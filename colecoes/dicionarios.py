# São apresentados por {} (chaves)

# possuem relação chave: elemento  (mesma relação de um objeto em javascript, mas a forma escrita se assemelha a um objeto em JSON)

# dicionarios permitem qualquer tipo de dado (int,float,string...)

# não são ordenados pelas chaves.

# são utilizados para otimizar a busca de dados, basta você saber a chave que irá acessar o elemento.

# como declarar

#                 sintaxe

# 1) forma mais usada



timeFutebol = {
    'RJ': 'Flamengo'
}

print(type(timeFutebol)) # <class 'dict'>

pintura = {
    'cor':'vermelha',
    'pincel': 'fino',
    'tipo':'realista'
}

print(pintura) # {'cor': 'vermelha', 'pincel': 'fino', 'tipo': 'realista'} 




# 2) utilizando o comando  dict()



pintor = dict(cor='vermelho',pincel='fino',tipo='realista')

print(pintor) # {'cor': 'vermelho', 'pincel': 'fino', 'tipo': 'realista'} 



# 3) forma menos usada # fromkeys() #evitar usar
#sintaxe: variavel = {}.fromkeys(iteravel, elemento) # cria um dicionario com cada item dentro do iteravel com o mesmo elemento

pint = {}.fromkeys('chave','dado') # cria uma chave para cada um dos itens iteraiveis

print(pint) # {'c': 'dado', 'h': 'dado', 'a': 'dado', 'v': 'dado', 'e': 'dado'}


#                  Sobre as chaves:

#devem ser unicas  - podem ser de qualquer tipo

time = {
    'rj':'flamengo',
    'rj':'corinthians'  #como existem duas chaves iguais o programa só reconhece a ultima valida
}

print(time) # {'rj': 'corinthians'}


sagas = {
    (1,2):'star wars',
    (3,4):'percy jackson'
}

print(sagas[(1,2)]) # star wars


novasSagas = {
    ('nome','usuario'):'igor'
}

print(novasSagas[('nome','usuario')]) # igor






#                Sobre os dados:

#podem ser duplicados - podem ser de qualquer tipo

tim = {
    'rj':'flamengo',
    'sp':'flamengo'
}


print(tim) # {'rj': 'flamengo', 'sp': 'flamengo'} #aceita dados iguais (diplucados)


#   COMO ACESSAR AOS ELEMENTOS

# 1) podemos acessar as keys(chaves) por colchetes, dessa forma:

cliente = {
    'nome':'igor',
    'idade':23
}

print(cliente['nome']) # igor
print(cliente['idade']) # 23

# 1.1) pense agora num cenario onde temos uma lista de dicionarios.

clientes = [
    {
        'nome':'igor',
        'idade':23
    },
    {
        'nome':'matheus',
        'idade':25
    }
]

#quero acessar o cliente com nome de matheus

print(clientes[1]['nome']) # matheus # acessando a lista de indice 1 chave 'nome' -> assim tenho o elemento 'matheus'


# 2) usando o get.
#sitnaxe:  variavel.get('chave')

cli = dict(nome='matheus',idade=23)
# cli = { 'nome':'matheus' }

print(cli.get('nome')) # matheus

nota = {
    'disciplina':'matematica',
    'nota': 9,
    'status':'passou de ano'
}

print(nota.get('nota')) # 9
print(nota.get('disciplina')) # matematica
print(nota.get('status')) # passou de ano

# 2.1) tratativa de erro usando o metodo get
# caso uma chave não exista você pode pedir para escrever outra coisa no lugar ex:

cubo = {
    'lados': 8,
    'nome': 'cubo magico',
    'valor': 50
}

print(cubo.get('vertices', 'outra coisa')) # outra coisa # nesse caso como a chave vertices não existe o programa escreve "outra coisa" no console

#    VERIFICANDO SE UMA CHAVE EXISTE

cabelo = {
    'cor':'preto',
    'tamanho':'muito grande'
}

print('cor' in cabelo) # True # ja que a chave 'cor' existe dentro do dicionario cabelo ele retorna true

print('coloracao' in cabelo) # False



# oque é o retorno none ???

#é um tipo de dado sem tipo - é um dado indefinido caso você ainda não saiba o valor da variavel

#ex:

variavelNumero = None 

print(variavelNumero) # None

num = 5

variavelNumero = 5

print(variavelNumero) # 5



#          ADICIONANDO UM NOVO ELEMENTO DENTRO DE UM DICIONARIO

# 1) usando a mesma sintaxe que é usada para acessar um elemento: variavel['chave'] = novo elemento

linguagens = {
    'indice1': 'python',
    'indice2':'javascript',
    'indice3':'django'
}
print(linguagens) # {'indice1': 'python', 'indice2': 'javascript', 'indice3': 'django'}

linguagens['indice4'] = 'flask'

print(linguagens) # {'indice1': 'python', 'indice2': 'javascript', 'indice3': 'django', 'indice4': 'flask'}


# 2) usando a função update  - (mais usado para adiconar "concatenar" dicionarios)
# OBS se a chave ja existir dentro de um dicionario, o metodo update vai simplismente atualizar ela 

# sintaxe dicionario.update({chave nova/alterada : valor})

dicionairo1 = {
    'nome':'valor',
    'chave':'outro valor'
}

dicionario2 = {
    'outra chave':'outro valor'
}

dicionairo1.update(dicionario2)

print(dicionairo1) # {'nome': 'valor', 'chave': 'outro valor', 'outra chave': 'outro valor'} 


dicionairo1.update({'chave': 'esse valor foi trocado'})

print(dicionairo1) # {'nome': 'valor', 'chave': 'esse valor foi trocado', 'outra chave': 'outro valor'} 




#          ALTERANDO ELEMENTOS DENTROD E UM DICIONARIO

# 1) acessando a chave e alterando o elemento


rotina = {
    1:'cortar cabelo',
    2:'comer hamburguer com os amigos'
}

print(rotina) # {1: 'cortar cabelo', 2: 'comer hamburguer com os amigos'}

rotina[2] = 'maratona'

print(rotina) # {1: 'cortar cabelo', 2: 'maratona'}


# 2) podemos usar tbm o .update() para alterar

rota = {
    'primeiro':'sair de casa',
    'segundo':'ir ao dentista'
}

print(rota) # {'primeiro': 'sair de casa', 'segundo': 'ir ao dentista'}

rota.update({'primeiro': 'levantar da cama'})

print(rota) # {'primeiro': 'levantar da cama', 'segundo': 'ir ao dentista'}



#                   REMOVENDO VALORES DE UM DICIONARIO

# 1) usando o metodo pop()
#lembrando que o metodo pop() retorna o elemento que foi retirado


pokemon = {
    'agua':'squirtle',
    'fogo':'charmander',
    'grama':'bulbassauro'
}

print(pokemon) # {'agua': 'squirtle', 'fogo': 'charmander', 'grama': 'bulbassauro'}

pokemonRetirado = pokemon.pop('fogo') # remove a chave 'fogo'

print(pokemon) # {'agua': 'squirtle', 'grama': 'bulbassauro'}

print(pokemonRetirado) # charmander


# 2) usando o del
# NÃO É POSSIVEL RETORNAR O DADO RETIRADO POR ESSE METODO , CASO QUEIRA RETORNAR USE O METODO POP()

coisas = {
    'nome':'livro',
    'id': 23,
    'ano': 1999
}

print(coisas)  # {'nome': 'livro', 'id': 23, 'ano': 1999}

del coisas['id']

print(coisas) # {'nome': 'livro', 'ano': 1999}