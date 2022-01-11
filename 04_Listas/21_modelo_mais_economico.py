print('Comparativo de Consumo de Combustível\n')

modelos = []
consumos = []

for i in range(0, 5):
    print(f'Veículo {i+1}')
    modelo = input('Nome: ')
    modelos.append(modelo)
    while True:
        try:
            consumo = float(input('Km por litro: '))
        except:
            print('Valor inválido! Digite novamente.')
            continue
        if (consumo <= 0):
            print('Consumo impossível! Digite novamente.')
            continue
        else: break
    consumos.append(consumo)

print('Relatório Final')

for i in range(0, 5):
    comb1000km = str(round(1000/consumos[i], 2))
    gasto1000km = str(round(float(comb1000km)*2.25, 2))
    print('{:<22} {:<9} {:<16} {:<10}'.format(str(i+1) + ' - ' + modelos[i]+ ' - ', str(consumos[i]) + ' - ', comb1000km + ' litros - ', 'R$ ' + gasto1000km))

indiceMenorConsumo = consumos.index(max(consumos))
print(f'O menor consumo é do {modelos[indiceMenorConsumo]}.')