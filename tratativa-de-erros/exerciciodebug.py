# 1) faça o debug a partir da primeira linha (x = 1) usando o metodo breakpoint() ou importando a biblioteca pdb do seguinte codigo e anote os valores das variaveis em cada linha como resposta

breakpoint()
x = 1 # 1
y = 10 # 10
z = 100 # 100
x = x + (y + z)  // 2 # 56
y = y ** 2 + z * x # 5700
z = (z ** 2) + z + x # 10156
soma = x + y + z # 15912
print(soma) # 15912