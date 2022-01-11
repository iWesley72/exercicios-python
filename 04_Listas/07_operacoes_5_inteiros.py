numeros = list()
produto = 1
for i in range(0, 5):
    while True:
        try:
            numeros.append(int(input(f'Digite o {i+1}° número: ')))
        except:
            print('Valor inválido! Digite novamente.')
            continue
        break
    produto *= numeros[i]
print(f'\nValores digitados: \n {numeros}')
print(f'Soma de todos valores: {sum(numeros)}')
print(f'Produto entre os valores: {produto}')