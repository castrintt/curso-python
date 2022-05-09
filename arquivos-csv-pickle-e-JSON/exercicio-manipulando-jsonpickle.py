# 1 ) deseja-se criar um programa que deixe a formula secreta da coca cola criptografada, para isso crie uma classe FormulaCocaCola com atributos privados: ingrediente, temperatura (Celsius), açucar (gramas) e o nome do proprietario.
# crie uma senha de acesso escolhido pelo usuario, instancia o objeto e passe o mesmo para o arquivo PICKLE.
# apos isso peça a senha para acessar os atributos, caso esteja correta, leia o arquivo e imprima=o na tela, se não , imprima um aviso de acesso negado!

import pickle

class FormulaCocaCola:

    def __init__(self, ingrediente, temperatura, acucar, nome):
        self.__ingrediente = ingrediente
        self.__temperatura = temperatura
        self.__acucar = acucar
        self.__nome = nome
        self.__senha = None
    

    @property
    def ingrediente(self):
        return self.__ingrediente

    @property
    def temperatura(self):
        return self.__temperatura

    @property
    def acucar(self):
        return self.__acucar
    
    @property
    def nome(self):
        return self.__nome

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, criaSenha):
        self.__senha = criaSenha
        return self.__senha


carlos = FormulaCocaCola(['água gaseificada', 'açúcar', 'extrato de noz de cola',' cafeína', 'corante caramelo IV', 'acidulante ácido fosfórico e aroma natural'],39,100,'carlos')

carlos.senha = 'admin'
    
with open('confidencial.pickle','wb') as confidencial:

    pickle.dump(carlos, confidencial)


with open('confidencial.pickle','rb') as confidencial:

    carlos = pickle.load(confidencial)
    
    condicao = 0

    validacao = False

    while condicao != 1:
        verificacao = input('Digite a senha do usuario Carlos: ')
        if verificacao == carlos.senha:
            print('Usuario Verificado')
            condicao = 1
            validacao = True
        else:
            print('Usuario não permitido')
    
    if validacao == True:
        print(f'Ingrediente: {carlos.ingrediente}')
        print(f'Açucar: {carlos.acucar} Gramas')
        print(f'Temperatura: {carlos.temperatura} Celsius')
    
