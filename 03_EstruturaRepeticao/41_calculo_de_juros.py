while True:
    try:
        dividaInicial = float(input('Valor da dívida: R$ '))
    except:
        print('Valor inválido! Tente novamente.')
        continue
    break
print('{:<16} {:<16} {:16} {:16}'.format('Valor da dívida', 'Valor dos Juros', 'Qtd. de Parcelas', 'Valor das Parcelas'))
for i in range(0, 13, 3):
    vDivida = dividaInicial
    if (i == 0):
        parcelas = 1
        juros = 0
    elif (i == 3):
        parcelas = 3
        juros = 0.1
    elif (i == 6):
        parcelas = 6
        juros = 0.15
    elif (i == 9):
        parcelas = 9
        juros = 0.2
    else:
        parcelas = 12
        juros = 0.25
    vJuros = round(vDivida*juros, 2)
    vDivida *= round((1+juros), 2)
    vParcela = round(vDivida/parcelas, 2)
    print('{:<16} {:<16} {:16} {:16}'.format('R$ '+ str(vDivida), vJuros, parcelas, 'R$ ' + str(vParcela)))