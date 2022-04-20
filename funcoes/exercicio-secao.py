# 1) faça uma função que receba um numero inteiro maior que zero e retorne a soma de todos os algorismo.
# caso o valor seja negativo retorne 'numero invalido':

 #ex 251 = 2 + 5 + 1 = 8
 
 
#minha resolução
  
def recebeNumero(num):
    stringNumero = str(num)
    lista = []
    for valor in stringNumero:
       lista.append(int(valor))
    
    tamanhoLista = len(lista)
    for indice,item in enumerate(lista):
        print(f'Indice : {indice} // Item : {item}')
    
    print(f'A soma de todos algorismos de {num} é {sum(lista)} e seus algorismos são ')
    
recebeNumero(251)



# resolução professor
