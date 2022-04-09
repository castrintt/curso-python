print('-------------CALCULADORA SIMPLES---------------')

print('-------ESCOLHA A OPERAÇÂO QUE DESEJA FAZER---------')

operacao = str(
    input('digite qual operação você deseja fazer: \n + \n - \n * \n / \n'))

if operacao == '+':
    print('REALIZANDO A OPERAÇÂO...')
    numero1 = float(input('digite o primeiro numero: '))
    numero2 = float(input('digite o segundo numero: '))
    soma = numero1 + numero2
    print(f'A soma entre {numero1} e {numero2} é igual a {soma}')
    print('Operação realizada')
    print('------ PROGRAMA FINALIZANDO...------')
elif operacao == '-':
    print('REALIZANDO A OPERAÇÂO...')
    numero1 = float(input('digite o primeiro numero: '))
    numero2 = float(input('digite o segundo numero: '))
    subtracao = numero1 - numero2
    print(f'a subtracao entre {numero1} e {numero2} é igual a {subtracao}')
    print('Operação realizada')
    print('------ PROGRAMA FINALIZANDO...------')
elif operacao == '*':
    print('REALIZANDO A OPERAÇÂO...')
    numero1 = float(input('digite o primeiro numero: '))
    numero2 = float(input('digite o segundo numero: '))
    multiplicacao = numero1 * numero2
    print(
        f'a multiplicacao entre {numero1} e {numero2} é igual a {multiplicacao}'
    )
    print('Operação realizada')
    print('------ PROGRAMA FINALIZANDO...------')
elif operacao == '/':
    print('REALIZANDO A OPERAÇÂO...')
    numero1 = float(input('digite o primeiro numero: '))
    numero2 = float(input('digite o segundo numero: '))
    divisao = numero1 / numero2
    print(f'a divisao entre {numero1} e {numero2} é igual a {divisao}')
    print('Operação realizada')
    print('------ PROGRAMA FINALIZANDO...------')
else:
    print('operação incorreta, por favor tente novamente')
