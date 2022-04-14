# 1) Chegou o famoso dia dos namorados, Mateus deixou para decidir o presente em cima da hora.
#ele resolveu comprar um tipo de flor, um presente e escolher um lugar para sairem, ele anotou todas as opções abaixo:

#             flores

# tipo           # preço

#rosas vermelhas     145
#girassois           125
#margaridas          120
#flores do campo     140


#             presente

# tipo         # preço

#urso de pelucia  55
#caixa de bombom  60
#colar            75
#roupas           40


#          lugar

# tipo         # preço
#praia            70
#sair para jantar 150
#parque de divers 120
#hotel            180

# - crie um programa que descubra qual a combinação mais cara, em seguida mais barada e a media opção
# imprima a combinação em cada caso.

# - use um dicionario para cada item (flor, lugar e presente)



flores = {
    'Rosas Vermelhas':145.00,
    'Girassois':125.00,
    'Margaridas':120.00,
    'Flores do Campo': 140.00
}

presente ={
    'Urso de Pelucia': 55.00,
    'Caixa de Bombom': 60.00,
    'Colar': 75.00,
    'Roupas': 40.00
}

lugar = {
    'Praia': 70.00,
    'Sair para Jantar': 150.00,
    'Parque de Diversão': 120.00,
    'Hotel': 180.00
}


combinacaoMaisCara = tuple( [ max(flores.values()), max(presente.values()), max(lugar.values()) ] )
combinacaoMenosCara = tuple( [ min(flores.values()), min(presente.values()), min(lugar.values()) ] )

# print(combinacaoMaisCara) # (145.0, 75.0, 180.0)
# print(combinacaoMenosCara) # (120.0, 40.0, 70.0)


#somando os valores para ver o total
somaCombinacaoMaisCara = sum(combinacaoMaisCara)
somaCombinacaoMenosCara = sum(combinacaoMenosCara)
# print(somaCombinacaoMaisCara) # 400.0
# print(somaCombinacaoMenosCara) # 230.0


florMaisCara = None
florMenosCara = None
valorMedioFlores = []
floresMedia = []

presenteMaisCaro = None
presenteMenosCaro = None
valorMedioPresente = []
presenteMedio = []

lugarMaisCaro = None
lugarMenosCaro = None
valorMedioLugar = []
lugarMedio = []


# achando flor mais cara, mais barata e os valores entre elas
for flor, valor in flores.items():
    if valor in combinacaoMaisCara:
        florMaisCara = flor
    elif valor in combinacaoMenosCara:
        florMenosCara = flor
    elif valor != max(flores.values()) and valor != min(flores.values()):
        valorMedioFlores.append(valor)
        floresMedia.append(flor)
        
    
# print(florMaisCara) # Rosas Vermelhas
# print(florMenosCara) # Margaridas
# print(valorMedioFlores) # [125.0, 140.0]
# print(floresMedia) # ['Girassois', 'Flores do Campo']

# achando presente mais caro, mais barato e os valores entre eles
for gift, valor in presente.items():
    if valor in combinacaoMaisCara:
        presenteMaisCaro = gift
    elif valor in combinacaoMenosCara:
        presenteMenosCaro = gift
    elif valor != max(presente.values()) and valor != min(presente.values()):
        valorMedioPresente.append(valor)
        presenteMedio.append(gift)
        
        
# print(presenteMaisCaro) # Colar
# print(presenteMenosCaro) # Roupas
# print(valorMedioPresente) # [55.0, 60.0]
# print(presenteMedio) # ['Urso de Pelucia', 'Caixa de Bombom']


# achando lugar mais caro e mais barato
for place, valor in lugar.items():
    if valor in combinacaoMaisCara:
        lugarMaisCaro = place
    elif valor in combinacaoMenosCara:
        lugarMenosCaro = place
    elif valor != max(lugar.values()) and valor != min(lugar.values()):
        valorMedioLugar.append(valor)
        lugarMedio.append(place)

# print(lugarMaisCaro) # Hotel
# print(lugarMenosCaro) # Parque de Diversão
# print(valorMedioLugar) # [150.0]
# print(lugarMedio) # ['Sair para Jantar']



print('\n')

print(f'A combinação mais cara de Flores, Presentes e Lugares é : R${somaCombinacaoMaisCara}')
print(f'Flor mais cara é: {florMaisCara} ')
print(f'Presente mais caro é: {presenteMaisCaro}')
print(f'Lugar mais caro é : {lugarMaisCaro}')

print('\n')

print(f'A combinação menos cara é : {somaCombinacaoMenosCara}')
print(f'Flor menos cara é : {florMenosCara}')
print(f'Presente menos caro é : {presenteMenosCaro}')
print(f'Lugar menos caro é: {lugarMenosCaro}')


print('\n')

print(f'A(s) flores com preço mediano são: {floresMedia} -- no valor de {valorMedioFlores}')
print(f'O(s) presentes com preço mediano são: {presenteMedio} -- no valor de {valorMedioPresente}')
print(f'O(s) lugares com preço medio são: {lugarMedio} -- no valor de {valorMedioLugar}')
