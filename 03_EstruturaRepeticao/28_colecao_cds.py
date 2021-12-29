try:
    qtdCD = int(input('Digite a quantidae de CD\'s na coleção: '))
except:
    print('Valor inválido!')
    quit()
valorTotal = 0
for i in range(1, qtdCD+1):
    while True:
        try:
            valorTotal += float(input((f'Digite o valor do {i}° CD: ')))
        except:
            print('Valor inválido! Tente novamente.')
            continue
        break
print(f'Valor total investido R${valorTotal}.')
media = round(valorTotal/qtdCD)
print(f'Valor médio por CD é de R${media}.')