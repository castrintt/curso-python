#faça um programa que calcule o maior palíndromo resultado do produto de dois numeros de 3 digitos

#- palindromo são numeros que lendo da esquerda para a direta o resulta no mesmo numero caso leia da direta para esquerda ex: 52625

n1 = 99
res = 0
while n1 != 0:
    n2 = n1
    while n2 != 0:
        
        numero = str(n1 * n2)
        inverteNumero = numero[::-1]
        
        if inverteNumero == numero:   
            num = int(numero)
            
            if res < num:
                res = num
                n2 -= 1
                
            else:
                n2 -= 1
                
        else:
            n2 -= 1   
    n1 -= 1
print(res)                 