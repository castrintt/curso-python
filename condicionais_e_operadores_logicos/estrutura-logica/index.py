#                        and

sensor = 68  #pode ficar entre 60 e 70


if sensor >= 60 and sensor <= 70:
    print('tudo ok')
else:
    print('pare a operação!')
    
#------------------  ------------------------

comida = True 
agua = True 

if comida and agua:
    print('cachorro feliz')
else:
    print('cachorro triste')


#                        or

num = 7 

if num % 2 == 0 or num <= 10:
    print('é par ou menor que 10')
else:
    print('é impar e maior que 10')
    
    
#------------------ --------------------------

pizza = True 
batataFrita = False 

if pizza or batataFrita:
    print('hoje a noite vai render!')
else:
    print('temos que pedir algo para comer')
 
    
#                         is

login = True

#como se fosse uma pergunta (login é True??  ||  login é False??)
print(login is False) #print False porque login não é falso

print(login is True) #print True porque login é verdadeiro

if login is True: #como login é True 
    print('Usuario logado') #retorna que o usuario está logado
else:
    print('Deslogado') 



#                      not

login = False


if not login: # NÂO FALSE (negação do boolean 'false'), ou seja, não false é True 
    print('usuario logado')
else:
    print('Deslogado')