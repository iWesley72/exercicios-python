ano = 0
populacaoA = 80000
populacaoB = 200000
while populacaoA <= populacaoB:
    populacaoA = round(populacaoA*1.03)
    populacaoB = round(populacaoB*1.015)
    ano += 1
    print('ANO', ano)
    print('População A:', round(populacaoA))
    print('Populaçâo B:', round(populacaoB))
print('Será necessários', ano, 'anos para que a população de A ultrapasse B.')