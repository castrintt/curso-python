# MODULOS CUSTOMIZADOS SÃO ENCONTRADOS EM NOSSO ARQUIVO
# são basicamente modulos criados por nós
# importar modulos criados por nos

import moduloTeste 

print(moduloTeste.lista) # [1, 2, 3, 4, 5] # essa lista foi importada do moduloTeste (arquivo criado por mim)

moduloTeste.impar(9) # 9 é impar # a função impar() foi importada do moduloTeste(criado por mim)


# ISSO TORNA SEU PROGRAMA MAIS ORGANIZADO

# MODULOS EXTERNOS
# São modulos que outros programadores criaram

# todos os modulos oficiais externos podem ser encontrador em --> pypi.org

# vamos no site pypi.org e buscar o modulo colorama e instalar ele no console usando o comando pip

# LEMBRE-SE SEMPRE USAR O AMBIENTE VIRTUAL PARA INSTALAR DEPENDENCIAS

# importação

from colorama import init
from colorama import Fore, Back, Style

init()


print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')