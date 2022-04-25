if __name__ != "__main__": # condição para execução
    def somaNumeros(x,y):
        print(x + y)
        
        
# se __name__ for diferente de __main__ ou seja, se voce tiver importado essa função dentro de algum lugar ela funciona, caso contrario, se tentar executar ela aqui ela não funciona


somaNumeros(1,2) # NameError: name 'somaNumeros' is not defined 

# se criarmos uma condição de execução somente se executarmos ela dentro de __main__ ela executa, ex:

if __name__ == '__main__':
    somaNumeros(1,2)  