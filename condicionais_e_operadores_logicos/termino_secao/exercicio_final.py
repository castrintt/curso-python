print('__________FORMULA DE BHASKARA__________')
print('___________ENTRE COM OS VALORES__________')

a = float(input('Entre com o valor de a: '))
b = float(input('Entre com o valor de b: '))
c = float(input('Entre com o valor de c: '))

delta = (b ** 2) - 4 * a * c


#para evitar numeros complexos
print('#############################################')
if a == 0:
    print('o valor de a, deve ser diferente de 0')
elif delta < 0:
    print('Sem raizes reais')
else:
    x1 = (-b + delta**( 1 / 2)) / ( 2 * a)
    x2 = (-b - delta**( 1 / 2)) / ( 2 * a)
    print(f"x1: {x1}, x2: {x2}") 
