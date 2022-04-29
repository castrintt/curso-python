# busca abstrair um elemento da vida real para ser controlado no codigo

# (a partir da classe é criado o objeto)

# Dentro de programação orientada a objetos, temos algumas definições importantes


# 1) classe : --> conjunto de metodos e tributos que constroem o objeto.

# 2) metodo : --> são como funções, porem estao dentro da classe.
# metodos desempenham um papel de controlar/interagir com o objeto
# metodos são nada mais nada menos --->> atributos que atuam como funções

# 3) atributo : --> Caracteristicas do objeto que a casse ira controle

# 4) objeto : --> Pessoa/animal/(objetos da vida real que serão controlados)


# EX :

# ANIMAL --> classe

# ------------------

# raça  / peso  / tamanho  --> atributos

# -------------------

# comer()   --> metodo


# Objeto cachorro se referencia a classe animal (a partir da classe é criado o objeto)
# ---------------------

# cachorro   --> objeto
 
# husky  20kg   40cm   --> atributos

# ---------------------

# comer()  --> metodo





# PRINCIPIOS DA PROGRAMAÇÃO ORIENTADA A OBJETOS:

# 1) Encapsulamento: promovendo maior segurança do programa, o desenvolvimento do codigo em POO é delimitado por uma classe, limitando o alcance de determinados atributos pelo objeto.

# ENVOLVER ALGO --> encapsula nossos metodos e atributos de cada objeto. A classe envolve tudo


# ex -- >> segurança da conta bancaria, não deixando qualquer usuario alterar o valor do seu saldo na conta


# 2) abstração: ocultação de codigo que não são necessarios para o usuario visualizar. (em javascript usamos setters e getters para limitar)

# ABSTRATA --> (algo que voce não ve)

# ex -- > o usuario não ve toda a logica do programa, apenas a execução dos mecanismos que deseja



# 3) Herança : é possivel criar sub-classes que herdam as caracteristicas da classe 'mae'
#  podendo manter um controle de classes mais importantes controlando classes menores
 
# ex: Conta poupança herda alguns atributos da conta corrente
# outro ex:  Classe filho herda algumas caracteristicas(atributos/ metodos) da Classe pai (cor do cabelo, altura e etc...)



# 4) polimorfismo: Como o proprio nome sugere, os objetos podem assumir mais de uma forma, permitindo usar um mesmo codigo para varios tipos de dados

# poli - varios
# morfismo - formas 
# polimorfismo - varias formas


# ex: Se tem uma classe que calcula a area de uma forma geometrica por diferentes metodos, essa classe pode calcular a area para diferentes figuras geometricas (triangulo, trapezio, circulo)
 