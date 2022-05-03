# # 1 ) herança 
# # expande a sua classe / sua classe vai ter mais alcance / utiliza menos codigo e da mais poder a sua classe

# # a classe que herda de uma classe (pai) tem todos os atributos e metodos presentes na classe pai
# # ou seja, uma classe (filho) herda todas os atributos e metodos da classe (pai)

# # ex

# # vamos montar 2 classes (televisao e radio)

# class Televisao:

#     def __init__(self,marca, peso,volume, polegadas):
#         self.__marca = marca
#         self.__peso = peso
#         self.__volume = volume
#         self.__polegadas = polegadas


#     @property
#     def volume(self):
#         return f'O volume esta em {self.__volume}'


    
# class Radio:

#     def __init__(self,marca, peso, volume, frequencia):
#         self.__marca = marca
#         self.__peso = peso
#         self.__volume = volume
#         self.__frequencia = frequencia

#     @property
#     def volume(self):
#         return f'O volume esta em {self.__volume}'


# # agora vamos instanciar as 2 classes

# tv = Televisao('phillips',3.6,30,50)
# radio = Radio('Lg',2.5, 60, 103.53)

# # executando a propriedade (metodo get) para ter acesso ao volume
# print(tv.volume)
# print(radio.volume)

# # O volume esta em 30
# # O volume esta em 60



# note que repetimos 3 atributos de instancia nas 2 classes ( marca, peso e volume)
# estamos perdendo tempo e produtividade com essas repetições!!
# para evitar esse tipo de repetição poderiamos fazer uma classe Radio e uma classe Televisao, que herdam os atributos, propriedades e metodos da classe Aparelho por exemplo
# ex


# classe pai
class Aparelho:

    def __init__(self, marca, peso, volume):
        self.__marca = marca
        self.__peso = peso
        self.__volume = volume

    
    @property
    def volume(self):
        return f'O volume esta em {self.__volume}'


# QUANDO UMA CLASSE É HERDADA DE OUTRA É INDICADO VIA PARENTESES NA CLASSE FILHA QUAL A CLASSE PAI
# ex classe Filho(Pai):
# POREM DESSA FORMA SÓ INDICAMOS QUE filho herda de pai, agora como indicariamos para a classe filha os atributos que estao sendo herdados?

# usamos o  --->> super().__init__(atributos_herdados)

# LEMBRANDO QUE --->> voce deve declarar tanto no constructor --> def __init__(self, atributos) quando no super ---> super().__init__(atributos)


class Televisao(Aparelho): # televisão esta herdando de Aparelho

    def __init__(self,marca, peso, volume, polegadas):
        super().__init__(marca, peso, volume) # indicando para a classe filha quais atributos ela esta herdando! usando super().__init__(atributos)
        self.__polegadas = polegadas

    
class Radio(Aparelho):

    def __init__(self,marca,peso,volume, frequencia):
        super().__init__(marca, peso, volume)
        self.__frequencia = frequencia


# agora vamos instancia-los para ver se mudou alguma coisa.

tv = Televisao('philips',2.4,80,'50 polegadas')
radio = Radio('LG',1,50,'105.3')


print(tv.volume)

print(radio.volume)

# O volume esta em 80
# O volume esta em 50

# continua trabalhando da mesma forma
# note o tanto de linhas de codigo que economizamos fazendo isso!


# resumindo

"""
a classe Aparelho é uma classe (mae / pai / base / génerica / Super classe) onde todos os atributos e metodos estão contidos

as classes Televisao e Radio (classes --> classe filha/ especifica / subclasses ), estão herdando todos os metodos, atributos, setters e propriedades da classe Aparelho

"""



# OverRinding - > reescrever um metodo presente na  super classe (classe pai) em uma sub classe (classe filha)