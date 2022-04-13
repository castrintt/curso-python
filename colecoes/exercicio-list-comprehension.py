# a partir de uma lista apresentada, utilizar list comprehension para criar outra lista apenas com animais que comecem com "C" e que o tamanho de seu nome seja menor ou igual a 7. Por fim, imprima a nova lista

#lista para o exercicio
animais = ['Cachorro','Cavalo','Baleia','Gato','Urso','Carneiro','Cabra','Cobra','Coelho','Mosquito','Peixe','Macaco']


#minha resolução

animaisComC = [animal for animal in animais if "C" in animal  and len(animal) <=7] # retorne animal, para todo animal in animais se animal conte a string "C" E a largura da string (animal) for menor ou igual a 7

print(animaisComC) # ['Cavalo', 'Cabra', 'Cobra', 'Coelho']


# fazendo com for nomal , sem o list comprehension

listaNova = []

for animal in animais:
    if 'C' in animal and len(animal) <= 7:
        listaNova.append(animal)
    
print(listaNova) # ['Cavalo', 'Cabra', 'Cobra', 'Coelho']








#resolução do professor


listaAnimais = [animal for animal in animais if animal[0] == "C" and len(animal) <= 7 ]

print(listaAnimais) # ['Cavalo', 'Cabra', 'Cobra', 'Coelho']


#resolvendo a resolução do professor com for normal


listaAnimaisNova = []

for animal in animais:
    if animal[0] == 'C' and len(animal) <= 7:
        listaAnimaisNova.append(animal)
        
print(listaAnimaisNova) # ['Cavalo', 'Cabra', 'Cobra', 'Coelho']