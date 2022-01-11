votos = [0]*23
print('Enquete: Quem foi o melhor jogador?\n')

while True:
    try:
        voto = int(input('Número do jogador (0=fim): '))
    except:
        print('Voto inválido! Tente novamente.')
        continue
    if (voto > 23 or voto < 0):
        print('Voto inválido! Tente novamente.')
        continue
    elif (voto == 0):
        break
    else:
        votos[voto-1] += 1
        continue

print('\nResultado da votação:')
print(f'\nForam computados {sum(votos)} votos.\n')

print('{:<10} {:<10} {:<15}'.format('Jogador', 'Votos', 'Porcentagem (%)'))
for i in range(0, 23):
    porcentagem = round(votos[i]/sum(votos)*100, 2)
    print('{:<10} {:<10} {:<15}'.format(i+1, votos[i], str(porcentagem) + '%'))
votosVencedor = max(votos)
indiceVencedor = votos.index(max(votos))
porcentagem = round(votosVencedor/sum(votos)*100, 2)
print(f'O melhor jogador foi o número {indiceVencedor+1}, com {votosVencedor} votos, correspondendo a {porcentagem}% do total de votos.')