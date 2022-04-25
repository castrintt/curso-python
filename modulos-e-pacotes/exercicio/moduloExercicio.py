def numerosPares(lista):
    for num in lista:
        if num % 2 == 0:
            print(num, end=", ")


def numerosImpares(lista):
    for num in lista:
        if num % 2 != 0:
            print(num, end=', ')
