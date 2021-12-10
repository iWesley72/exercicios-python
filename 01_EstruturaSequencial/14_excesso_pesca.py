peso = float(input('Digite o peso total dos peixes em kg: '))
excesso = peso - 50
if (excesso > 0):
    multa = excesso * 4
    print('A multa será de R$', multa, 'por um excesso de', excesso, 'kg.')
else:
    print('Não haverá multa, pois não há excesso.')