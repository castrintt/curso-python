# 1) A partir de uma lista apresentada, criar um generator contendo apenas animais que comecem com "C" ou "A" e que o tamanho de seu nome seja maior que 5. Por fim, itere e imprima o Generator

#lista para o exercicio

listaAnimais = ['Cachorro','Avestruz','Alce','Cavalo','Baleia','Gato','Urso','Abelha','Carneiro','Cabra','Cobra','Coelho','Mosquito','Peixe','Macaco','Aranha']

#resolução

generatorAnimais = (animal for animal in listaAnimais if (animal[0] == 'C' or animal[0] == 'A') and len(animal) > 5)

for animais in generatorAnimais:
    print(animais,end=", ")

#(Cachorro, Avestruz, Cavalo, Abelha, Carneiro, Coelho, Aranha)

print('\n')

#outra forma 

genAnimais = (animal for animal in listaAnimais if ('C' in animal or 'A' in animal) and len(animal) > 5)

for animais in genAnimais:
    print(animais, end=", ")

#(Cachorro, Avestruz, Cavalo, Abelha, Carneiro, Coelho, Aranha)


#resolução professor

genAnimais = (animal for animal in listaAnimais if (animal[0] == 'C' or animal[0] == 'A') and len(animal) > 5)

for animal in genAnimais:
    print(animal, end=" ")