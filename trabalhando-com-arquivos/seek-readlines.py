# Seek e ReadLine

# -  Seek : movimenta o cursor pelo arquivo (ou seja, não precisamos ficar abrindo o arquivo toda hora que quisermos usar ele de novo)
# porque sempre que usamos o arquivo.read() o cursor vai pro final do arquivo e nao volta

# OBS - nos permite usar varias operações durante a leitura do arquivo
# sintaxe:  arquivo.seek(posicao onde queremos o cursor) # ex arquivo.seek(4) posicao 4 , arquivo.seek(0) volta ao inicio

# ex

arquivo = open('lucros.txt')
print(arquivo.read())
# janeiro - R$ 12.560,00
# fevereiro - R$ 65.987,00
# março - R$ 12.876,00


arquivo.seek(0) # nesse caso como eu coloquei o parametro 0 o cursor volta ao inicio do programa e podemos re-ler o programa

print(arquivo.read())
# janeiro - R$ 12.560,00
# fevereiro - R$ 65.987,00
# março - R$ 12.876,00

arquivo.seek(3) # nesse caso o cursor volto para a linha 3 ou seja, a palavra janeiro, foi lida como eiro (o cursor ignorou o jan)

print(arquivo.read()) 

# eiro - R$ 12.560,00
# fevereiro - R$ 65.987,00
# março - R$ 12.876,00




# ReadLine  - lê o arquivo por linhas
# se não passarmos nenhum parametro ele lê sempre a primeira linha, caso a gente passe parametros ele le a primeira linha até a linha passada no parametro
# ex - arquivo.readline(10) -- le a primeira linha até 10 caracteres

# OBS a cada chamada do readline() ele lê uma linha

novoArquivo = open('lucros.txt')
linha = novoArquivo.readline() # como chamei uma vez só ele le somente a primeira linha

print(linha) # janeiro - R$ 12.560,00

linha = novoArquivo.readline()

print(linha) # fevereiro - R$ 65.987,00



# readlines() - retorna uma lista em que cada elemento é uma linha do arquivo (diferente de readline)

# ex

arquivo = open('lucros.txt')

lista = arquivo.readlines() # dessa forma fizemos uma lista em que cada um dos elementos é uma linha do arquivo txt

print(lista) # ['janeiro - R$ 12.560,00\n', 'fevereiro - R$ 65.987,00\n', 'março - R$ 12.876,00']
