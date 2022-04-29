# Oque são classes
# conjunto de metodos e atributos que constroem o objeto

# ex : poderiamos criar uma classe chamada controle que controla o objeto ar condicionado tendo como atributo o nivel de temperatura, ligado ou desligado e etc...

# declaração 
# sintaxe: class nome_da_classe:
                # bloco de codigo

# ex

class Controle:
    pass # é usada para apenas passar a class/funcao

# regras de nomenclaturas de classes

# 1) palavras compostas devem ser separadas por letras maiusculas (sem underline)
# ex

#           errado

class Cliente_chato:
    pass

class Controle_remoto:
    pass

#            correto

class ClienteChato:
    pass

class ControleRemoto:
    pass

# 2 ) a primeira letra deve sempre ser maiuscula

#            errado:

class dinheiro:
    pass

class banco:
    pass

class cliente:
    pass

#            correto

class Dinheiro:
    pass

class Banco:
    pass

class Cliente:
    pass

# 3) não devem ter acentos ou caracteres especiais


# errado

class MeuNomeÉigor:
    pass


# correto

class MeuNomeEIgor:
    pass




# as classes imbutidas no python ja vem por padrao com a primeira letra minuscula, por isso é interessante separar nossas funções das nativas no python



# Porque criar uma classes?

# - Para criar novos tipos de dados


class Animal:
    pass

# criamos um novo tipo de dado, criamos um objeto leao e macaco a partir de uma classe
leao = Animal() 
macaco = Animal()

# se usarmos o Dir , podemos identificar todos atributos de uma classe,
# vamos usar por exemplo o dir de conjuntos

# ex

print(dir(set))

# ['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
# esses são todos atributos e metodos de um conjunto

print(dir(dict))

# ['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
# esses são todos atributos e metodos de um dicionario


#               PORTANTO

# HELP - retorna a propria classe

# DIR - retorna os metodos e atributos que estão dentro da classe
