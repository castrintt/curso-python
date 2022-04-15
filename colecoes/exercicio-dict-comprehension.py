# 1) para todos os numeros 1 a 99 use Dict comprehension para encontrar o digito unico mais alto em que qualquer um dos numeros é divisivel

#ex : 64 tem o maior divisor de digito unico igual a 8, pois 9 não é divisor de 64


#logica
resultado = {}

for number in range(1,100): # para numeros de 1 a 99
    list = [] # criamos uma lista vazia para anexar os maiores divisores
    for divisor in range(1,10): # para numeros de 1 a 9
        if number % divisor == 0: # se o resto da divisão dos numeros de 1 a 99 pelos numeros de 1 a 9 for igual a 0
            list.append(divisor)  # anexa esses (divisores) dentro da lista vazia
    resultado[number] = max(list) # logo depois anexa dentro de resultado como chave - numeros de 1 a 99 e como valor os valores maximos dentro de list

print(resultado)
 # {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 5, 11: 1, 12: 6, 13: 1, 14: 7, 15: 5, 16: 8, 17: 1, 18: 9, 19: 1, 20: 5, 21: 7, 22: 2, 23: 1, 24: 8, 25: 5, 26: 2, 27: 9, 28: 7, 29: 
# 1, 30: 6, 31: 1, 32: 8, 33: 3, 34: 2, 35: 7, 36: 9, 37: 1, 38: 2, 39: 3, 40: 8, 41: 1, 42: 7, 43: 1, 44: 4, 45: 9, 46: 2, 47: 1, 48: 8, 49: 7, 50: 5, 51: 3, 52: 4, 53: 1, 54: 9, 55: 5, 56: 8, 
# 57: 3, 58: 2, 59: 1, 60: 6, 61: 1, 62: 2, 63: 9, 64: 8, 65: 5, 66: 6, 67: 1, 68: 4, 69: 3, 70: 7, 71: 1, 72: 9, 73: 1, 74: 2, 75: 5, 76: 4, 77: 7, 78: 6, 79: 1, 80: 8, 81: 9, 82: 2, 83: 1, 84: 7, 85: 5, 86: 2, 87: 3, 88: 8, 89: 1, 90: 9, 91: 7, 92: 4, 93: 3, 94: 2, 95: 5, 96: 8, 97: 1, 98: 7, 99: 9}


# usando dict comprehension 



result = {number:max( [ divisor for divisor in range(1,9) if number % divisor == 0 ] ) for number in range(1,100) } # fizemos um dict comprehension onde a chave é o valor recebido por um for no range de 1 a 99 e o valor é um list comprehension onde o sera retornado o divisor num range de 1 a 9 se o resto da divisão do number (range 1 a 99) pelo divisor (range 1 a 9) for igual a 0

print(result)

# {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 3, 10: 5, 11: 1, 12: 6, 13: 1, 14: 7, 15: 5, 16: 8, 17: 1, 18: 6, 19: 1, 20: 5, 21: 7, 22: 2, 23: 1, 24: 8, 25: 5, 26: 2, 27: 3, 28: 7, 29: 
# 1, 30: 6, 31: 1, 32: 8, 33: 3, 34: 2, 35: 7, 36: 6, 37: 1, 38: 2, 39: 3, 40: 8, 41: 1, 42: 7, 43: 1, 44: 4, 45: 5, 46: 2, 47: 1, 48: 8, 49: 7, 50: 5, 51: 3, 52: 4, 53: 1, 54: 6, 55: 5, 56: 8, 
# 57: 3, 58: 2, 59: 1, 60: 6, 61: 1, 62: 2, 63: 7, 64: 8, 65: 5, 66: 6, 67: 1, 68: 4, 69: 3, 70: 7, 71: 1, 72: 8, 73: 1, 74: 2, 75: 5, 76: 4, 77: 7, 78: 6, 79: 1, 80: 8, 81: 3, 82: 2, 83: 1, 84: 7, 85: 5, 86: 2, 87: 3, 88: 8, 89: 1, 90: 6, 91: 7, 92: 4, 93: 3, 94: 2, 95: 5, 96: 8, 97: 1, 98: 7, 99: 3}