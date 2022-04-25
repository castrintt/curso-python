# 1 ) Crie uma pasta, uma subpasta e em seguida um modulo na subpasta contendo uma função qualquer.
# acesse o modulo no programa inicial e execute a função
# OBS : no modulo criado, estabeleça uma condição para a função ser acessada apenas se o modulo for importado e executado em outro. Ou seja, quando o modulo em questao não é o principal (main)


from dunder.modules.exercicio import somaNumeros as soma


a = 10
b = 20

soma(a,b) # 30

