notas = list()

while True:
    try:
        nota = float(input('Digite a nota: '))
    except:
        print('Nota inválida! Digite novamente.')
        continue
    if (nota == -1):
        print('')
        break
    else:
        notas.append(nota)
        print('')
media = sum(notas)/len(notas)
print(f'Total de notas registradas: {len(notas)}')
print(f'Notas registradas: \n{notas}')
notas.reverse()
print(f'Notas registradas invertidas {notas}')
print(f'Soma das notas: {sum(notas)}')
print(f'Média das notas: {media}')
qtdAcimaMedia = 0
qtdAbaixo7 = 0
for i in range(0, len(notas)):
    if (notas[i] > media):
        qtdAcimaMedia += 1
    if (notas[i] < 7):
        qtdAbaixo7 += 1
print(f'Total de notas acima da média: {qtdAcimaMedia}')
print(f'Total de notas abaixo de 7: {qtdAbaixo7}')
print('Fim do programa!')