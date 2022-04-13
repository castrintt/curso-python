# 1- kiko precisa invadir uma prisão de segurança extremamente alta para resgatar Jaiminho. Porém, existem 3 portões protegidos por senhas do TIPO TUPLA. cada portão oferece uma dica para descobrir a senha. A dica é composta por uma tupla contendo algumas dezenas, e uma frase indicando o processo a ser realizado. Kiko deve criar um programa que imprima na tela as três senhas no seguinte formato :
 
 # print(f'portão X : {senha_do_portao_x}')
 
 # DICAS
 
 # portao1 = (29,54,45)  [altere todos numeros para 0]
 
 # portao2 = (12, 28, 37, 54) [a soma dos elementos 2 e 3 é o primeiro elemento da senha, a soma dos elementos 1 e 4 é o segundo elemento da senha]
 
 # portao3 = (16, 86, 78, 32, 85, 12) [o valor minimo é o primeiro elemento da senha, o valor máximo é o segundo elemento da senha]
 
 
portao1 = (29,54,45)
portao2 = (12, 28, 37, 54)
portao3 = (16, 86, 78, 32, 85, 12)

senha1 = list(portao1)

for indice, senha in enumerate(senha1):
    senha1[indice] = 0

portao1 = tuple(senha1) # (0, 0, 0)

portao2 = portao2[1] + portao2[2], portao2[0] + portao2[-1] # (65, 66
    
portao3 = min(portao3), max(portao3) # (12, 86)


print(f'\nPortao 1 : {portao1}\nPortao 2 : {portao2}\nPortao 3 : {portao3}')

# Portao 1 : (0, 0, 0)                                                         
# Portao 2 : (65, 66) 
# Portao 3 : (12, 86) 


#resolução professor

portao1 = (29,54,45)
portao2 = (12, 28, 37, 54)
portao3 = (16, 86, 78, 32, 85, 12)


senha1 = list(portao1)

for id in range(0,3):
    senha1[id] = 0

portao1 = tuple(senha1)


portao2 = portao2[1] + portao2[2], portao2[0] + portao2[3]

portao3 = (min(portao3), max(portao3))


print(f'\nPortao 1 : {portao1}\nPortao 2 : {portao2}\nPortao 3 : {portao3}')


# Portao 1 : (0, 0, 0)                                                         
# Portao 2 : (65, 66) 
# Portao 3 : (12, 86)