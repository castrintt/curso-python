# representados por chaves e possuem a relação chave -> dado

# como declarar

# sintaxe

# dict = {chave: dado (podem ter operações e funções aqui tbm) for chave, dado in iteravel.items()}

#ex

cliente = {
    'nome': 'igor',
    'idade': 23,
    'profissão': 'programador'
}


novoCliente = {chave: dado for chave, dado in cliente.items()}

print(novoCliente) # {'nome': 'igor', 'idade': 23, 'profissão': 'programador'}  # nesse caso só repetiu




pessoas_idade = {
    'ana': 22,
    'matheus': 18,
    'lucas': 24
}

meiaIdade = {chave:valor / 2 for chave, valor in pessoas_idade.items()}
print(meiaIdade) # {'ana': 11.0, 'matheus': 9.0, 'lucas': 12.0} # todas idades divididas por 2
# é a mesma coisa que isso
pessoasMeiaIdade = {}

for chave, valor in pessoas_idade.items():
    pessoasMeiaIdade[chave] = valor / 2

print(pessoasMeiaIdade) # {'ana': 11.0, 'matheus': 9.0, 'lucas': 12.0} # tem o mesmo retorno que a dict comprehension meiaIdade


#                        CONDICIONAIS


# 1) usando condicionais if (só if é sempre depois da iteração for)

idadeMaior = {chave:valor for chave, valor in pessoas_idade.items() if valor > 18}

print(idadeMaior) # {'ana': 22, 'lucas': 24} # retorna todos as chaves e valores que possuem valores maiores que 18

# 1.1) usando if else (quando temos if e else a condição vem antes da iteração)

idadesMultiplicadas = {chave:valor if valor > 18 else valor * 2 for chave, valor in pessoas_idade.items()}

print(idadesMultiplicadas) # {'ana': 22, 'matheus': 36, 'lucas': 24} # para todos valores menores ou iguais a 18 seram multiplicados por 2


