print('Lojas Tabajara')
valor = []
contador = 1
while True:
    try:
        valor.append(float(input(f'Produto {contador}: R$ ')))
    except:
        print('Valor inválido! Digite novamente')
        continue
    if (valor[contador-1] == 0):
        break
    contador += 1
total = sum(valor)
print(f'Total: R$ {round(total, 2)}')
while True:
    try:
        dinheiro = float(input('Dinheiro: R$ '))
    except:
        print('Valor inválido! Tente novamente.')
        continue
    if(dinheiro < total):
        print(f'Faltam R$ {round(dinheiro-total, 2)}')
        continue
    else:
        break
print(f'Troco: R$ {round(dinheiro-total, 2)}')