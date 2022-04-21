# 1) calcule o fatorial de n utilizando um loop for e depois utilizando reduce. O resultado é o mesmo?

# 2) realizar o calculo do IMC atravez de uma função utilizando map com os dados fornecidos abaixo sobre peso e altura, e salvar os resultado em outra lista. Após isso, aplicar o filter para separar pessoas obesas(IMC > 25)

# dados 

# indice 0 das tuplas: peso (kg)
# indice 1 das tuplas: altura (m)

# IMC = peso / (altura ** 2) imc igual peso dividido pela altura ao quadrado


# ex 1  resolução professor


from functools import reduce

# fatorial 3 = 3 * 2 * 1

#usando for loop

n = int(input('Fatorial de : '))
fat = 1
fatorados = []

for i in range(1, (n + 1)):
    fatorados.append(i)
    
for numeros in fatorados:
    fat *= numeros
    

print(f'Fatorial de {n} é igual a {fat}')    
print(f'Os numeros fatoriais de {n} São {fatorados}')


# usando reduce

lista = [1]

lista.extend(range(1, ( n + 1 )))

fatorial = reduce(lambda x , y: x * y, lista)

print(f'fatorial usando reduce {fatorial}')




# ex 2 minha resolução



listaAmostras = [(62,1.73),
                 (90,1.86),
                 (76,2.12),
                 (54, 1.56),
                 (69,1.76),
                 (112, 1.63),
                 (98,1.59)]

def imc(*args):
    for item in args:
        return item[0] // (item[1] ** 2)

    
pesos = map(imc,listaAmostras)

#print(list(pesos)) # [20.0, 26.0, 16.0, 22.0, 22.0, 42.0, 38.0]
    
def obeso(num):
    if num > 25:
        return num

obesos = filter(obeso, pesos)

print(list(obesos)) # [26.0, 42.0, 38.0] 

# lambda peso: peso in range(30,41)



# ex 2 resolução professor

listaAmostras = [(62,1.73),
                 (90,1.86),
                 (76,2.12),
                 (54, 1.56),
                 (69,1.76),
                 (112, 1.63),
                 (98,1.59)]


def calculoIMC(amostra):
    imc = amostra[0] / (amostra[1] ** 2)
    return imc

imc = map(calculoIMC, listaAmostras)

resultadoIMC = list(imc)

resultIMC = []

for num in resultadoIMC:
    resultIMC.append(round(num))
    

print(resultIMC)


sobrePeso = filter(lambda imc: imc > 25, resultIMC)

print(list(sobrePeso))