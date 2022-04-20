# 1) faça o sistema de uma corrida entre mercurio, papa-leguas, sonic, flash, ligeirinho e super homem (MC , PL, SN, FS, LG, SH).

# crie uma função que receba os 6 corredores em ordem do vencedor até o ultimo (pedir o usuario), sendo os tres primeiros em variaveis obrigatorias e os tres ultimos em kwargs, com as chaves sendo as posições na corrida. Pedir ao usuario se houve trapaça:
     # - se não houve: apresentar a classificação final:
     # - se houve : pedir ao ususario quem trapaceou e quem foi prejudicado. depois, troca-los de posições. Por fim, apresentar a classificação final.
     

def corredores(n1,n2,n3,**kwargs):
    dicionario = {
        'pos1':n1,
        'pos2':n2,
        'pos3':n3
    }
    trapaceiro = input('Digite o trapaceiro: ')
    prejudicado = input('Digite o prejudicado: ')
    
    for chave, valor in kwargs.items():
        if trapaceiro == valor:
            kwargs[chave] = prejudicado       
        elif prejudicado == valor:
            kwargs[chave] = trapaceiro          
        for key, value in dicionario.items():
            if prejudicado == value:
                dicionario[key] = trapaceiro
            elif trapaceiro == value:
                dicionario[chave] = prejudicado     
                
    print(n1,n2,n3,kwargs['pos4'], kwargs['pos5'], kwargs['pos6'])            
                
                
                      

corredores('mercurio','papa leguas','sonic',pos4='flash',pos5='ligeirinho',pos6='super homem')