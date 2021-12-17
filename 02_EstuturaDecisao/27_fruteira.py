try:
    morango = float(input('Digite a quantidade desejada de morango em kg: '))
    maca = float(input('Digite a quantidade desejada de maçãs em kg: '))
except:
    print('Valor inválido!')
    quit()
valorTotal = 0
if (morango > 5):
    valorTotal += 2.2*morango
else:
    valorTotal += 2.5*morango
if (maca > 5):
    valorTotal += 1.5*maca
else:
    valorTotal += 1.8*maca
if (valorTotal > 25):
    valorTotal *= 0.9
print('Valor total: R$', round(valorTotal, 2))