# Assertions --> afirmações (uma ferramenta de teste)

# para que serve --> permite encontrar bugs rapidamente

# ele testa se uma afirmação é verdadeira , caso sim roda o codigo, caso não  gera um erro

# pode ser usado no meio do codigo sem perdas

# normalmente é suado para checar tipos de parametros, classes, valores ...

# são usados como complementos dos unittests

# modo de uso
# sintaxe:
# declaracao = valor
# assert condicao (testa se a declaracao é de fato igual a um valor, ou algum tipo de dado )

# ex de aplicação


mensagem = 'tamo junto'

# caso essa afirmação seja verdadeira o codigo continua rodando
assert mensagem == 'tamo junto'

print(mensagem)

# caso a afirmação não seja de fato verdadeira vai nos retornar um erro chamado Assertionerror

# ex

numero = 22

assert type(numero) == str # AssertionError

print(numero) # nesse caso o programa para no assert, o print de numero nem chega a ser executado


# Podemos passar qual o erro que vai ser impresso no console logo após a condição 

# sintaxe --> assert condição , texto

# ex

mensagem = 'ola tudo bem?'

assert mensagem == 'onde estou?', 'Mensagem incorreta' # o console retorna --> AssertionError: Mensagem incorreta

# logo podemos passar uma informação a mais



# Assertion em classes --> teste em classes

class Test:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome


maria = Test('maria')
 
assert isinstance(maria, Test), 'Não é instancia de Teste' # nesse caso estamos testando se maria é uma instancia de Test! caso não for retorna AssertionError: 'Não é instancia de Teste'


# Assertion em funções

# ex

def apaga_arquivos(senha):
    senhaConfirma = 123
    # podemos fazer um assert dentro de uma função se quisermos, veja!
    assert senha == senhaConfirma, 'Não é igual, arquivo não sera deletado' # --> nesse caso sera testado se a senha recebida como argumento da função é igual a variavel senhaConfirma, se não for retorna um AssertionError
    return f'{senha} ok, acesso liberado'


apaga_arquivos(123) # nesse caso temos o retorno da função (segue a execução normal da função)
apaga_arquivos(12341123) # nesse caso temos um AssertionError: Não é igual, arquivo não sera deletado


#  ASSERTION TEM UM PONTO FRACO

# --> se alguem acessar o arquivo python usando o ( -O ) 'traço letra o maiúscula' todos assertions serão cancelados
 
# sintaxe ---> dentro do console digite -->> python3 -O nomeDoArquivo.py

# POR TANTO ---> não é recomendavel usar o assert como principal teste, pois pode ser desabilitado facilmente usando o -O (traço letra o maiúscula) que cancela todos assertions presentes no programa