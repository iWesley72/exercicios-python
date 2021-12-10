area = float(input('Digite a área a ser pintada em m²: '))
tinta = area / 3
latasNecessarias = round((tinta/18))
if (tinta % 18 != 0):
    latasNecessarias += 1
print('Total de latas é', latasNecessarias)
print('Valor total: R$', latasNecessarias*80)