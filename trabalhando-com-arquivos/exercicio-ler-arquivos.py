# 1 ) - crie um arquivo de texto na pasta onde está seu programa python. O arquivo deve conter alguns numeros de 4 digitos separados por linha, representando numeros de uma rifa.Após isso, itere no arquivo  para colocar os valores em uma lista. Por fim, utilize a função choice() para determinar o ganhador.

# minha resolução

from random import choice as ch

valores = []
with open('exercicio.txt') as txt:
    ler = txt.read()
    separador = ler.replace('\n',',').split(',') 
    # 1 - trocamos troca de linha por virgula
    # 2 -  transformamos em lista usando a virgula como separador
    for num in separador:
        valores.append(num)
    # esse for poderia ser substituido por um shallow copy ou um simples deepCopy (ambos dão certo)
    #valores = valores.copy(separador)
    #valores = separador

# print(valores)  # ['1234', '4321', '4234', '6433', '5164', '4365', '5234', '6786', '4366', '8388', '2358', '0678', '3456', '5807', '3413', '3485']

#declarando vencedor

print(f'O numero de rifa vencedor foi: {ch(valores)}')
    


# resolução professor

from random import choice as ch

numerosRifa = []

with open('exercicio.txt') as rifa:
    for num in rifa:
        numerosRifa.append(int(num)) # dessa forma o '\n' é ignorado

#print(numerosRifa) # [1234, 4321, 4234, 6433, 5164, 4365, 5234, 6786, 4366, 8388, 2358, 678, 3456, 5807, 3413, 3485]

print(f'O vencedor foi: {ch(numerosRifa)}')
