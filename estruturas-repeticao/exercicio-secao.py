# Média dos 5 primeiros numeros primos da sequência fibonacci

#fn = (fn-1) + (fn-2)

anterior = 0 
proximo = 1 #numero posterior da sequencia
parada = 1
soma = 0
while parada <= 5:
    # print(proximo, end=" ") #1 1 2 3 5 
    proximo = proximo + anterior 
    anterior = proximo - anterior
    divisor = 1
    numeroDivisoresInteiros = 0
    while divisor <= proximo: # testa todos os divisores de proximo e incrementa
        if proximo % divisor == 0:
            numeroDivisoresInteiros += 1
        divisor += 1
    if numeroDivisoresInteiros == 2: #se o numero de divisores inteiros for = 2, ou seja ele pode ser divisivel por ele mesmo e um imprima numero
        print(proximo, end=", ")
        soma = soma + proximo 
        parada += 1  
print(f'a media é {soma/5}', end="")