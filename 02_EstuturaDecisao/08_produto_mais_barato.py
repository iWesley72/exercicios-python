preco1 = float(input('Digite o valor do primeiro produto: '))
preco2 = float(input('Digite o valor do segundo produto: '))
preco3 = float(input('Digite o valor do terceiro produto: '))

if (preco1 < preco2 and preco1 < preco3):
    print('O primeiro produto é o que deve ser comprado.')
elif (preco2 < preco1 and preco2 < preco3):
    print('O segundo produto é o que deve ser comprado.')
else:
    print('O terceiro produto é o que deve ser comprado.')