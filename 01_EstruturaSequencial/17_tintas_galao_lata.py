area = float(input('Digite o tamanho da área a ser pintada em m²:  '))
tinta = area/6*1.1
latas = round(tinta/18)
galao = round(tinta/3.6)
if (tinta % 18 != 0):
    latas += 1
if (tinta % 3.6 != 0):
    galao += 1

mLatas = tinta/18
mGaloes = (tinta - mLatas*18)/3.6
if ((tinta - mLatas*18) % 3.6 != 0):
    mGaloes += 1
print('A compra pode ser feita em:')
print(latas, 'latas de 18L: R$', latas*80)
print(galao, 'galões de 3.6L: R$', galao*25)
print(round(mLatas), 'latas de 18L e', round(mGaloes), 'galões de 3.6L: R$', round(mLatas)*80+round(mGaloes)*25)