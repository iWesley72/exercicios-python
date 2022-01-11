idsMouse = []
defeitos = [0]*4
print('Defeitos:')
print('1 - Necessita de esfera')
print('2 - Necessita de limpeza')
print('3 - Necessita troca do cabo ou conector')
print('4 - Quebrado ou inutilizado\n')

while True:
    try:
        id = int(input('ID do mouse: '))
    except:
        print('ID inválido! Digite novamente.')
        continue
    if (id == 0):
        break
    idsMouse.append(id)
    while True:
        try:
            defeito = int(input('Tipo de defeito: '))
        except:
            print('Defeito inválido! Digite novamente.')
            continue
        if (defeito > 4 or defeito < 1):
            print('Defeito inválido! Tente novamente.')
        else:
            defeitos[defeito-1] += 1
            break

print(f'Quantidade de mouses: {len(idsMouse)}\n')
print('{:<40} {:<10} {:<10}'.format('Situação', 'Quantidade', 'Percentual'))
print('{:<40} {:<10} {:<10}'.format('1 - Necessita de esfera', defeitos[0], str(round(defeitos[0]/sum(defeitos)*100, 2) + '%')))
print('{:<40} {:<10} {:<10}'.format('2 - Necessita de limpeza', defeitos[1], str(round(defeitos[1]/sum(defeitos)*100, 2) + '%')))
print('{:<40} {:<10} {:<10}'.format('3 - Necessita troca do cabo ou conector', defeitos[2], str(round(defeitos[2]/sum(defeitos)*100, 2) + '%')))
print('{:<40} {:<10} {:<10}'.format('4 - Quebrado ou inutilizado', defeitos[3], str(round(defeitos[3]/sum(defeitos)*100, 2)) + '%'))
