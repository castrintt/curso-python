# 1)  crie um arquivo com conteudo aleatorio. Em seguida, abra o arquivo, leia-o 3 vezes a partir dos caracteres 5, 9, 14. Por fim, feche o arquivo

texto = open('arquivo-seek-ex.txt')

texto.seek(5)
print(texto.read())

texto.seek(9)

print(texto.read())

texto.seek(14)

print(texto.read())

texto.close()

print(texto.closed)