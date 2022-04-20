# 1) faça o sistema de uma corrida entre mercurio, papa-leguas, sonic, flash, ligeirinho e super homem (MC , PL, SN, FS, LG, SH).

# crie uma função que receba os 6 corredores em ordem do vencedor até o ultimo (pedir o usuario), sendo os tres primeiros em variaveis obrigatorias e os tres ultimos em kwargs, com as chaves sendo as posições na corrida. Pedir ao usuario se houve trapaça:
     # - se não houve: apresentar a classificação final:
     # - se houve : pedir ao ususario quem trapaceou e quem foi prejudicado. depois, troca-los de posições. Por fim, apresentar a classificação final.
     
# MINHA RESOLUÇÃO     


def corredores(corredor1,corredor2,corredor3,**ultimos):
   
    podium = {
        'Primeiro':corredor1,
        'Segundo':corredor2,
        'Terceiro':corredor3
    }
    
    podium.update(ultimos)
    print('\n')
    print(podium)
    print('\n')
    
    confirmacao = int(input('Houve trapaceiro? 1 - sim // 2 - nao: '))
    
    if confirmacao == 1:
        trapaceiro = input('Digite quem foi o trapaceiro: ')
        prejudicado = input('Digite quem foi o prejudicado: ')
        print('\n')
    
        for posicao, corredor in podium.items():
            if corredor == trapaceiro:  
                podium[posicao] = prejudicado

            elif corredor == prejudicado:
                podium[posicao] = trapaceiro
                print(podium)
                print('\n')
                return
    else:
        print(podium)
        print('\n')
        return
      

corredores('flash','papa leguas','super homem',Quarto='sonic',Quinto='ligeirinho',Sexto='mercurio')


# RESOLUÇÂO PROFESSOR


def classParcial(primeiro,segundo,terceiro,**outros):
    op = input('Houve trapaça?: s/n ')
    quarto = ''
    quinto = ''
    ultimo = ''
    if op == 'n':
        for posicao, corredor in outros.items():
            if posicao == '4':
                quarto = corredor
            elif posicao == '5':
                quinto = corredor
            elif posicao == '6':
                ultimo  == corredor
                
        classFinal(primeiro, segundo,terceiro,quarto,quinto,ultimo)
        
    elif op == 's':
        colocacao = [primeiro,segundo,terceiro]
        colocacao.extend(outros.values())
        
        babaca = input('Quem trapaceou? : ')
        vitima = input('Quem foi prejudicado? : ')
        
        posBabaca = colocacao.index(babaca)
        posVitima = colocacao.index(vitima)
        
        colocacao[posBabaca] = vitima
        colocacao[posVitima] = babaca
        
        classFinal(*colocacao)
    else: 
        print('Digite uma opção valida!')
        
    
    
def classFinal(primeiro,segundo,terceiro,quarto,quinto,ultimo):
    print('Classificação final')
    print(f'primeiro: {primeiro}')
    print(f'Segundo: {segundo}')
    print(f'Terceiro: {terceiro}')
    print(f'Quarto: {quarto}')
    print(f'Quinto: {quinto}')
    print(f'Ultimo: {ultimo}')
    
    
    

pri = input('Vencedor:')
seg = input('Segundo: ')
ter = input('Terceiro: ')
qua = input('Quarto: ')
qui = input('Quinto: ')
ult = input('ultimo: ')


outros = {
    '4':qua,
    '5':qui,
    '6':ult
}


    