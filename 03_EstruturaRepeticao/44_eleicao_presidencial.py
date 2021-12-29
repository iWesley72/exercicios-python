print('{:<11}'.format('Candidatos'))
print('{:<11} {:<11} {:<11} {:<11}'.format('1 - José', '2 - João', '3 - Luís', '4 - Sérgio'))
print('Para voto nulo código 5, para voto em branco código 6.\n')

total = 0
c1 = 0
c2 = 0
c3 = 0
c4 = 0
branco = 0
nulo = 0
while True:
    voto = input('Código do candidato: ')
    if (voto == '0'):
        break
    elif (voto == '1'):
        c1 += 1
    elif (voto == '2'):
        c2 += 1
    elif (voto == '3'):
        c3 += 1
    elif (voto == '4'):
        c4 += 1
    elif (voto == '5'):
        nulo += 1
    elif (voto == '6'):
        branco += 1
    else:
        print('Código inválido!')
        continue
    total += 1

print('Resultado final')
print('{:<11} {:<15}'.format('Opções', 'Total de Votos'))
print('{:<11} {:<15}'.format('José', c1))
print('{:<11} {:<15}'.format('João', c2))
print('{:<11} {:<15}'.format('Luís', c3))
print('{:<11} {:<15}'.format('Sérgio', c4))
print('{:<11} {:<15}'.format('Nulo', nulo))
print('{:<11} {:<15}'.format('Branco', branco))
print(f'Total de eleitores: {total}')
print(f'Porcentagem de votos em branco: {round(branco/total*100, 2)}%')
print(f'Porcentagem de votos nulo: {round(nulo/total*100, 2)}%')
