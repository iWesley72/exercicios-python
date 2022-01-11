temperaturas = list()
for i in range(0, 12):
    while True:
        try:
            temperaturas.append(float(input(f'Temperatuda(°C) do {i+1}° mês: ')))
        except:
            print('Valor inválido! Digite novamente.')
            continue
        break
tempMedia = sum(temperaturas)/len(temperaturas)
print(f'Temperatura média: {tempMedia} °C')
print('Temperaturas acima da média: ')
for i in range(0, 12):
    if (temperaturas[i] > tempMedia):
        if (i == 0): mes = 'Janeiro'
        elif (i == 1): mes = 'Fevereiro'
        elif (i == 2): mes = 'Março'
        elif (i == 3): mes = 'Abril'
        elif (i == 4): mes = 'Maio'
        elif (i == 5): mes = 'Junho'
        elif (i == 6): mes = 'Julho'
        elif (i == 7): mes = 'Agosto'
        elif (i == 8): mes = 'Setembro'
        elif (i == 9): mes = 'Outubro'
        elif (i == 10): mes = 'Novembro'
        elif (i == 11): mes = 'Dezembro'
        print(f'{mes}: {temperaturas[i]} °C')
