print('Compara duas strings')
texto1 = input('String 1: ')
texto2 = input('String 2: ')
print(f'Tamanho de "{texto1}": {len(texto1)} caracteres.')
print(f'Tamanho de "{texto2}": {len(texto2)} caracteres.')
if (len(texto1) == len(texto2)): print('As duas strings são do mesmo tamanho.')
else: print('As duas strings são de tamanhos diferentes.')
if (texto1 == texto2): print('As duas strings possuem o mesmo conteúdo.')
else: print('As duas strings possuem conteúdo diferente.')